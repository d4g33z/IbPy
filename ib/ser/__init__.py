from .ewrapper_data import  EWRAPPERS   as ews
from .eclient_data  import  ECLIENTS    as ecs

from copy import copy
def flatten(x):
    l = copy(x)
    while l:
        while l and isinstance(l[0], list):
            l[0:1] = l[0]
        if l: yield l.pop(0)


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

IBClasses = [
    CommissionReport,Contract,ContractDetails,Execution,
    UnderComp,Order,OrderState,ComboLeg,OrderComboLeg,
    ScannerSubscription,ExecutionFilter]

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
    'ComboLeg'          :ComboLeg,
    'OrderComboLeg'     :OrderComboLeg,
    'ScannerSubscription':ScannerSubscription,
#from ECLIENT_DATA
    'ExecutionFilter'   :ExecutionFilter,
    'std::string'       :str,
    'tickerId'          :int
}

def make_serializer(kls):
    ks = [x for x in filter(lambda x:x[:2]=='m_',kls.__dict__.keys())]
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
    ks = [x for x in filter(lambda x:x[:2]=='m_' in x,kls.__dict__.keys())]
    #summary attribute is a Contract type
    if kls is ContractDetails:
        return lambda x:IBObjectFactory(kls)(**{k:v if k != 'summary' \
            else make_deserializer(Contract)(**v) for k,v in x.items()})
    elif kls is Contract:
        return lambda x:IBObjectFactory(kls)(**{k:v if k != 'comboLegs' \
            else [make_deserializer(ComboLeg)(y) for y in v] for k,v in x.items()})
    else:
        return lambda x:IBObjectFactory(kls)(**x)

EWRAPPER_SERIALIZERS = {}
for ew in ews:
    sers = {}
    for type_info in ew[1]:
        if type_info != '':
            try:
                _,ib_type,argument = type_info.split(' ')
            except ValueError:
                ib_type,argument = type_info.split(' ')
            if ib_type not in type_models.keys():
                if ew[0][0] == 'openOrder':
                    if argument != 'orderId':
                        ib_type = argument
                        argument = argument[0].lower() + argument[1:]
                else:
                    print("{} is broken :-()".format(ew[0][0]))
                    break
            if ib_type in ['TickType','IBString','OrderId','TickerId','bool','double','faDataType','int','long']:
               sers.update({argument:lambda x:x})
            else:
                sers.update({argument:make_serializer(type_models[ib_type])})

    EWRAPPER_SERIALIZERS[ew[0][0]] = sers

try:
    from inspect import Signature,Parameter
except ImportError:
    from funcsigs import Signature,Parameter

ECLIENT_SIGNATURES = {}
for ec in ecs:
    parameters = []
    for type_info in ec[1]:
        if type_info != '':
            try:
                _,ib_type,argument = \
                [x for x in filter(lambda x:x is not '',type_info.split(' '))]
            except ValueError:
                ib_type,argument = \
                    [x for x in filter(lambda x:x is not '',type_info.split(' '))]
            if ib_type not in type_models.keys():
                if ec[0][0] == 'reqMktData':
                    if argument == 'mktDataOptions': #ignore it
                        continue
                elif ec[0][0] == 'reqFundamentalData':
                    if argument == 'Contract': #ignore it
                        ib_type = argument
                        argument = argument[0].lower() + argument[1:]
                elif ec[0][0] == 'reqMktDepth':
                    if argument == 'mktDepthOptions': #ignore it
                        continue
                elif ec[0][0] == 'reqHistoricalData':
                    if argument == 'chartOptions': #ignore it
                        continue
                elif ec[0][0] == 'reqRealTimeBars':
                    if argument == 'realTimeBarsOptions': #ignore it
                        continue
                elif ec[0][0] == 'reqScannerSubscription':
                    if argument == 'scannerSubscriptionOptions': #ignore it
                        continue
                else:
                    print("{} is broken now too:-()".format(ec[0][0]))
                    break
            parameters.append(Parameter(
                argument,Parameter.POSITIONAL_OR_KEYWORD,annotation=type_models[ib_type]))

    ECLIENT_SIGNATURES[ec[0][0]] = Signature(parameters)

from ib.opt.connection import Connection
from ib.opt import message
import json
def setup(clientId=0):
    def _watch_factory(ewrapper):
        def _watch(msg):
            for k,v in EWRAPPER_SERIALIZERS.get(ewrapper).items():
                try:
                    print('\n'+ewrapper+':'+k+'\n'+json.dumps(v(getattr(msg,k)),indent=2))
                except TypeError:
                    print('\n'+ewrapper+':'+k+'\n'+"{0}".format(str(msg)))
        return _watch,getattr(message,ewrapper)

    ibcon = Connection.create(clientId=clientId)
    [ibcon.register(*_watch_factory(x)) \
        if x in message.__dict__.keys() else None for x in EWRAPPER_SERIALIZERS.keys()]
    ibcon.connect()

    def _work(eclient_method, **arguments):
        #type check
        assert all([type(arguments.get(x))==\
            ECLIENT_SIGNATURES.get(eclient_method).parameters.get(x).annotation for x in arguments.keys()])
        try:
            getattr(ibcon,eclient_method).__call__(
                *[arguments.get(x) for x in map(lambda x:list(x).pop(0),
                        getattr(message,eclient_method)().items())])
        except ConnectionResetError as e:
            print("Connection Refused:\n"+e.strerror)
    return _work

#-----------------------------------------------------------------------------------------------------------
#simple api applications
#-----------------------------------------------------------------------------------------------------------

def describe_ib_api(eclient_method=None):
    if not eclient_method:
        for k,v in ECLIENT_SIGNATURES.items():
            print('\n'+k+':\n'+str(v))
    else:
        print('\n'+eclient_method+':\n'+str(ECLIENT_SIGNATURES.get(eclient_method)))

#look at this to create type_models
def describe_ib_types():
    for ib_type in\
        set([x for x in filter(lambda x:x!='',
            [x for x in flatten(
            [[x.split(' ')[:-1] for x in e[1]] for e in ews+ecs])])]):
        if ib_type in type_models.keys():
            print("{0:24} \t\tmodeled by \t\t{1}".format(ib_type,str(type_models[ib_type])))
        elif ib_type == 'const':
            pass#not a type
        else:
            print("{0} may require a python object model unless we can ignore it".format(ib_type))

import sys,time
def example(acctCode,clientId=1):
    ibworker = setup(clientId=clientId)
    #acctCode can be None, but let's be strict
    ibworker('reqAccountUpdates',subscribe=True,acctCode=acctCode)
    time.sleep(5)
    #example of type checking
    try:
        ibworker('reqAccountUpdates',subscribe=0,acctCode=acctCode)
    except AssertionError:
        ibworker('reqAccountUpdates',subscribe=False,acctCode=acctCode)


