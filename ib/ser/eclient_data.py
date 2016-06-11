ECLIENTS = [[['reqMktData'],
             ['TickerId id', 'const Contract contract', 'const std::string genericTicks', 'bool snapshot',
              'const TagValueListSPtr mktDataOptions']], [['cancelMktData'], ['TickerId id']],
            [['placeOrder'], ['OrderId id', 'const Contract contract', 'const Order order']],
            [['cancelOrder'], ['OrderId id']], [['reqOpenOrders'], ['']],
            [['reqAccountUpdates'], ['bool subscribe', 'const std::string acctCode']],
            [['reqExecutions'], ['int reqId', 'const ExecutionFilter filter']], [['reqIds'], ['int numIds']],
            [['reqContractDetails'], ['int reqId', 'const Contract contract']], [['reqMktDepth'], ['TickerId tickerId',
                                                                                                   'const Contract contract',
                                                                                                   'int numRows',
                                                                                                   'const TagValueListSPtr mktDepthOptions']],
            [['cancelMktDepth'], ['TickerId tickerId']], [['reqNewsBulletins'], ['bool allMsgs']],
            [['cancelNewsBulletins'], ['']], [['setServerLogLevel'], ['int level']],
            [['reqAutoOpenOrders'], ['bool bAutoBind']], [['reqAllOpenOrders'], ['']], [['reqManagedAccts'], ['']],
            [['requestFA'], ['faDataType pFaDataType']],
            [['replaceFA'], ['faDataType pFaDataType', 'const std::string cxml']], [['reqHistoricalData'],
                                                                                    ['TickerId id',
                                                                                     'const Contract contract',
                                                                                     'const std::string endDateTime',
                                                                                     'const std::string durationStr',
                                                                                     'const std::string  barSizeSetting',
                                                                                     'const std::string whatToShow',
                                                                                     'int useRTH', 'int formatDate',
                                                                                     'const TagValueListSPtr chartOptions']],
            [['exerciseOptions'],
             ['TickerId tickerId', 'const Contract contract', 'int exerciseAction', 'int exerciseQuantity',
              'const std::string account', 'int override']], [['cancelHistoricalData'], ['TickerId tickerId ']],
            [['reqRealTimeBars'],
             ['TickerId id', 'const Contract contract', 'int barSize', 'const std::string whatToShow', 'bool useRTH',
              'const TagValueListSPtr realTimeBarsOptions']], [['cancelRealTimeBars'], ['TickerId tickerId ']],
            [['cancelScannerSubscription'], ['int tickerId']], [['reqScannerParameters'], ['']],
            [['reqScannerSubscription'], ['int tickerId', 'const ScannerSubscription subscription',
                                          'const TagValueListSPtr scannerSubscriptionOptions']],
            [['reqCurrentTime'], ['']],
            [['reqFundamentalData'], ['TickerId reqId', 'const Contract', 'const std::string reportType']],
            [['cancelFundamentalData'], ['TickerId reqId']], [['calculateImpliedVolatility'],
                                                              ['TickerId reqId', 'const Contract contract',
                                                               'double optionPrice', 'double underPrice']],
            [['calculateOptionPrice'],
             ['TickerId reqId', 'const Contract contract', 'double volatility', 'double underPrice']],
            [['cancelCalculateImpliedVolatility'], ['TickerId reqId']],
            [['cancelCalculateOptionPrice'], ['TickerId reqId']], [['reqGlobalCancel'], ['']],
            [['reqMarketDataType'], ['int marketDataType']], [['reqPositions'], ['']], [['cancelPositions'], ['']],
            [['reqAccountSummary'], ['int reqId', 'const std::string groupName', 'const std::string tags']],
            [['cancelAccountSummary'], ['int reqId']],
            [['verifyRequest'], ['const std::string apiName', 'const std::string apiVersion']],
            [['verifyMessage'], ['const std::string apiData']], [['verifyAndAuthRequest'], ['const std::string apiName',
                                                                                            'const std::string apiVersion',
                                                                                            'const std::string opaqueIsvKey']],
            [['verifyAndAuthMessage'], ['const std::string apiData', 'const std::string xyzResponse']],
            [['queryDisplayGroups'], ['int reqId']], [['subscribeToGroupEvents'], ['int reqId', 'int groupId']],
            [['updateDisplayGroup'], ['int reqId', 'const std::string contractInfo']],
            [['unsubscribeFromGroupEvents'], ['int reqId']],
            [['reqPositionsMulti'], ['int reqId', 'const std::string account', 'const std::string modelCode']],
            [['cancelPositionsMulti'], ['int reqId']], [['reqAccountUpdatessMulti'],
                                                        ['int reqId', 'const std::string account',
                                                         'const std::string modelCode', 'bool ledgerAndNLV']],
            [['cancelAccountUpdatesMulti'], ['int reqId']], [['reqSecDefOptParams'],
                                                             ['int reqId', 'const std::string underlyingSymbol',
                                                              'const std::string futFopExchange',
                                                              'const std::string underlyingSecType',
                                                              'int underlyingConId']]]