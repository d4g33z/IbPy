from .ewrapper_data import EWRAPPERS as ews
from .eclient_data import ECLIENTS as ecs

from copy import copy
def flatten(x):
    l = copy(x)
    while l:
        while l and isinstance(l[0], list):
            l[0:1] = l[0]
        if l: yield l.pop(0)

#look at this to create type_models
types_to_model = \
    set([x for x in flatten([[x.split(' ')[:-1] for x in e[1]] for e in ews+ecs])])

from ib.ext.CommissionReport    import CommissionReport
from ib.ext.Contract            import Contract
from ib.ext.ContractDetails     import ContractDetails
from ib.ext.Execution           import Execution
from ib.ext.UnderComp           import UnderComp
from ib.ext.Order               import Order
from ib.ext.OrderState          import OrderState
from ib.ext.ComboLeg            import ComboLeg
from ib.ext.OrderComboLeg       import OrderComboLeg
from ib.ext.ScannerSubscription import ScannerSubscription
from ib.ext.ExecutionFilter     import ExecutionFilter

def IBObjectFactory(ibcls):
    class IBGeneric(object):
        _ibcls = ibcls
        def __new__(cls,**kwargs):
            obj = cls._ibcls()
            [setattr(obj,'m_'+k,v) for k,v in kwargs.items()]
            return obj

        def get_property(self,name):
            return getattr(self,'m_'+name)
    return IBGeneric

type_models = {
#from EWRAPPER_DATA
    'CommissionReport'  :CommissionReport,
    'Contract'          :Contract,
    'ContractDetails'   :ContractDetails,
    'Execution'         :Execution,
    'UnderComp'         :UnderComp,
    'Order'             :Order,
    'OrderState'        :OrderState,
    'TickType'          :int, 
    'IBString'          :str,
    'OrderId'           :int,
    'TickerId'          :int,
    'bool'              :bool,
    'double'            :float,
    'faDataType'        :int,
    'int'               :int,
    'long'              :int,
#potentially needed as attributes to be serializad
    'ComboLeg'          :ComboLeg,
    'OrderComboLeg'     :OrderComboLeg,
    'ScannerSubscription':ScannerSubscription,

#from ECLIENT_DATA
    'ExecutionFilter'   :ExecutionFilter,
    'std::string'       :str,
    'tickerId'          :int
}

def make_serializer(kls):
    ks = [x for x in filter(lambda x:'m_' in x,kls.__dict__.keys())]
    #summary attribute is a Contract type
    if kls is ContractDetails:
        return lambda x:{k[2:]:getattr(x,k) if k[2:] != 'summary' \
            else make_serializer(Contract)(getattr(x,k)) for k in ks}
    elif kls is Contract:
        return lambda x:{k[2:]:getattr(x,k) if k[2:] != 'comboLegs' \
            else [make_serializer(ComboLeg)(y) for y in getattr(x,k)] for k in ks}
    else:
        return lambda x:{k[2:]:getattr(x,k) for k in ks}

def make_deserializer(kls):
    ks = [x for x in filter(lambda x:'m_' in x,kls.__dict__.keys())]
    #summary attribute is a Contract type
    if kls is ContractDetails:
        return lambda x:IBObjectFactory(kls)(**{k:v if k != 'summary' \
            else make_deserializer(Contract)(**v) for k,v in x.items()})
    elif kls is Contract:
        return lambda x:IBObjectFactory(kls)(**{k:v if k != 'comboLegs' \
            else [make_deserializer(ComboLeg)(y) for y in v] for k,v in x.items()})
    else:
        return lambda x:IBObjectFactory(kls)(**x)

from eliot import MessageType,Field,add_destination
ELIOT_MESSAGE_TYPES = {}
EC_ELIOT_MESSAGE_TYPES = {}

for ew in ews:
    fields = []
    for type_info in ew[1]:
        if type_info != '':
            try:
                _,ib_type,argument = type_info.split(' ')
            except ValueError:
                ib_type,argument = type_info.split(' ')
            if ib_type not in type_models.keys():
                if ew[0][0] == 'openOrder':
                    if argument != 'orderId': #orderId is ok
                        ib_type = argument
                        argument = argument[0].lower() + argument[1:]
                else:
                    print("{} is broken now too:-()".format(ew[0][0]))
                    break 

            if ib_type in ['TickType','IBString','OrderId','TickerId','bool','double','faDataType','int','long']:
                fields.append(Field.for_types(argument,[type_models[ib_type]],description=''))
            else:
                fields.append(Field(argument,make_serializer(type_models[ib_type]),description=''))

    ELIOT_MESSAGE_TYPES[ew[0][0]] = \
            MessageType('ib_message',fields)

for ec in ecs:
    fields = []
    for type_info in ec[1]:
        if type_info != '':
            try:
                _,ib_type,argument = \
                [x for x in filter(lambda x:x is not '',type_info.split(' '))]
            except ValueError:
                ib_type,argument = \
                    [x for x in filter(lambda x:x is not '',type_info.split(' '))]
            if ib_type not in type_models.keys():
                if ec[0][0] == 'reqFundamentalData':
                    if argument != 'orderId': #orderId is ok
                        ib_type = argument
                        argument = argument[0].lower() + argument[1:]
                else:
                    print("{} is broken now too:-()".format(ec[0][0]))
                    break

            if ib_type in \
                    ['TickType','IBString','OrderId','TickerId',
                     'bool','double','faDataType','int','long',
                     'std::string','tickerId']:
                fields.append(Field.for_types(argument,[type_models[ib_type]],description=''))
            elif ib_type not in ['TagValueListSPtr']:
                fields.append(Field(argument,make_serializer(type_models[ib_type]),description=''))

    EC_ELIOT_MESSAGE_TYPES[ec[0][0]] = \
            MessageType('ib_message',fields)



#__all__ = [IBContract,ELIOT_MESSAGE_TYPES,make_serializer]
#example usage #notice the assignment!!!
#import sys,json
#def write_log(message):
#    sys.stdout.write(json.dumps(message)+'\n')
#add_destination(write_log)
#m = ELIOT_MESSAGE_TYPES['execDetails']()
#m = m.bind(reqId=1,contract=Contract(),execution=Execution())
#m.write()
