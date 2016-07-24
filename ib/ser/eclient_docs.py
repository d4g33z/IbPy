
ECLIENT_DOCS = {'Close': ('Terminates the connection and notifies the EWrapper '
           'implementing class.',
           [''],
           [],
           {}),
 'IsConnected': ('Notifies whether or not the API client is connected to '
                 'the Host.',
                 [''],
                 [],
                 {}),
 'calculateImpliedVolatility': ('Calculate the volatility for an option. '
                                'Request the calculation of the implied '
                                'volatility based on hypothetical option '
                                'and its underlying prices. The calculation '
                                "will be return in EWrapper's "
                                'tickOptionComputation callback.',
                                ['reqId',
                                 'contract',
                                 'optionPrice',
                                 'underPrice',
                                 'impliedVolatilityOptions'],
                                ['int',
                                 'Contract',
                                 'double',
                                 'double',
                                 'TagValue'],
                                {'contract': "the option's contract for "
                                             'which the volatility wants '
                                             'to be calculated.',
                                 'optionPrice': 'hypothetical option price.',
                                 'reqId': 'unique identifier of the '
                                          'request.',
                                 'underPrice': "hypothetical option's "
                                               'underlying price.'}),
 'calculateOptionPrice': ("Calculates an option's price. Calculates an "
                          "option's price based on the provided volatility "
                          "and its underlying's price. The calculation will "
                          "be return in EWrapper's tickOptionComputation "
                          'callback.',
                          ['reqId',
                           'contract',
                           'volatility',
                           'underPrice',
                           'optionPriceOptions'],
                          ['int', 'Contract', 'double', 'double', 'TagValue'],
                          {'contract': "the option's contract for which "
                                       'the price wants to be calculated.',
                           'reqId': "request's unique identifier.",
                           'underPrice': "hypothetical underlying's price.",
                           'volatility': 'hypothetical volatility.'}),
 'cancelAccountSummary': ("Cancels the account's summary request. After "
                          "requesting an account's summary, invoke this "
                          'function to cancel it.',
                          ['reqId'],
                          ['int'],
                          {'reqId': 'the identifier of the previously '
                                    'performed account request'}),
 'cancelAccountUpdatesMulti': ('Cancels account updates request for account '
                               'and/or model.',
                               ['requestId'],
                               ['int'],
                               {}),
 'cancelCalculateImpliedVolatility': ("Cancels an option's implied "
                                      'volatility calculation request.',
                                      ['reqId'],
                                      ['int'],
                                      {'reqId': 'the identifier of the '
                                                "implied volatility's "
                                                'calculation request.'}),
 'cancelCalculateOptionPrice': ("Cancels an option's price calculation "
                                'request.',
                                ['reqId'],
                                ['int'],
                                {'reqId': "the identifier of the option's "
                                          "price's calculation request."}),
 'cancelFundamentalData': ('Cancels Fundamental data request.',
                           ['reqId'],
                           ['int'],
                           {'reqId': "the request's idenfier."}),
 'cancelHistoricalData': ('Cancels a historical data request.',
                          ['reqId'],
                          ['int'],
                          {'reqId': "the request's identifier."}),
 'cancelMktData': ('Cancels a RT Market Data request.',
                   ['tickerId'],
                   ['int'],
                   {'tickerId': "request's identifier"}),
 'cancelMktDepth': ("Cancel's market depth's request.",
                    ['tickerId'],
                    ['int'],
                    {'tickerId': "request's identifier."}),
 'cancelNewsBulletin': ("Cancels IB's news bulletin subscription.",
                        [''],
                        [],
                        {}),
 'cancelOrder': ('Cancels an active order.',
                 ['orderId'],
                 ['int'],
                 {'orderId': "the order's client id"}),
 'cancelPositions': ("Cancels all account's positions request.", [''], [], {}),
 'cancelPositionsMulti': ('Cancels positions request for account and/or '
                          'model.',
                          ['requestId'],
                          ['int'],
                          {'requestId': '- the identifier of the request '
                                        'to be canceled.'}),
 'cancelRealTimeBars': ("Cancels Real Time Bars' subscription.",
                        ['tickerId'],
                        ['int'],
                        {'tickerId': "the request's identifier."}),
 'cancelScannerSubscription': ('Cancels Scanner Subscription.',
                               ['tickerId'],
                               ['int'],
                               {'tickerId': "the subscription's unique "
                                            'identifier.'}),
 'exerciseOptions': ('Exercises your options.',
                     ['tickerId',
                      'contract',
                      'exerciseAction',
                      'exerciseQuantity',
                      'account',
                      'ovrd'],
                     ['int', 'Contract', 'int', 'int', 'string', 'int'],
                     {'account': 'destination account',
                      'contract': 'the option Contract to be exercised.',
                      'exerciseAction': 'set to 1 to exercise the option, '
                                        'set to 2 to let the option lapse.',
                      'exerciseQuantity': 'number of contracts to be '
                                          'exercised',
                      'ovrd': 'Specifies whether your setting will '
                              "override the system's natural action. For "
                              'example, if your action is "exercise" and '
                              'the option is not in-the-money, by natural '
                              'action the option would not exercise. If '
                              'you have override set to "yes" the natural '
                              'action would be overridden and the '
                              'out-of-the money option would be exercised. '
                              'Set to 1 to override, set to 0 not to.',
                      'tickerId': "exercise request's identifier"}),
 'placeOrder': ('Places an order.',
                ['id', 'contract', 'order'],
                ['int', 'Contract', 'Order'],
                {'contract': "the order's contract",
                 'id': "the order's unique identifier. Use a sequential id "
                       'starting with the id received at the nextValidId '
                       'method. If a new order is placed with an order ID '
                       'less than or equal to the order ID of a previous '
                       'order an error will occur.',
                 'order': 'the order'}),
 'replaceFA': ("Replaces Financial Advisor's settings A Financial Advisor "
               'can define three different configurations:',
               ['faDataType', 'xml'],
               ['int', 'string'],
               {'faDataType': 'the configuration to change. Set to 1, 2 or '
                              '3 as defined above.',
                'xml': 'the xml-formatted configuration string'}),
 'reqAccountSummary': ("Requests a specific account's summary. This method "
                       'will subscribe to the account summary as presented '
                       "in the TWS' Account Summary tab. The data is "
                       'returned at EWrapper::accountSummary '
                       'https://www.interactivebrokers.com/en/software/tws/accountwindowtop.htm.',
                       ['reqId', 'group', 'tags'],
                       ['int', 'string', 'string'],
                       {'group': 'set to "All" to return account summary '
                                 'data for all accounts, or set to a '
                                 'specific Advisor Account Group name that '
                                 'has already been created in TWS Global '
                                 'Configuration.',
                        'reqId': 'the unique request identifier.',
                        'tags': 'a comma separated list with the desired '
                                'tags:\n'
                                'AccountType — Identifies the IB account '
                                'structure\n'
                                'NetLiquidation — The basis for '
                                'determining the price of the assets in '
                                'your account. Total cash value + stock '
                                'value + options value + bond value\n'
                                'TotalCashValue — Total cash balance '
                                'recognized at the time of trade + futures '
                                'PNL\n'
                                'SettledCash — Cash recognized at the time '
                                'of settlement - purchases at the time of '
                                'trade - commissions - taxes - fees\n'
                                'AccruedCash — Total accrued cash value of '
                                'stock, commodities and securities\n'
                                'BuyingPower — Buying power serves as a '
                                'measurement of the dollar value of '
                                'securities that one may purchase in a '
                                'securities account without depositing '
                                'additional funds\n'
                                'EquityWithLoanValue — Forms the basis for '
                                'determining whether a client has the '
                                'necessary assets to either initiate or '
                                'maintain security positions. Cash + '
                                'stocks + bonds + mutual funds\n'
                                'PreviousEquityWithLoanValue — Marginable '
                                'Equity with Loan value as of 16:00 ET the '
                                'previous day\n'
                                'GrossPositionValue — The sum of the '
                                'absolute value of all stock and equity '
                                'option positions\n'
                                'RegTEquity — Regulation T equity for '
                                'universal account\n'
                                'RegTMargin — Regulation T margin for '
                                'universal account\n'
                                'SMA — Special Memorandum Account: Line of '
                                'credit created when the market value of '
                                'securities in a Regulation T account '
                                'increase in value\n'
                                'InitMarginReq — Initial Margin '
                                'requirement of whole portfolio\n'
                                'MaintMarginReq — Maintenance Margin '
                                'requirement of whole portfolio\n'
                                'AvailableFunds — This value tells what '
                                'you have available for trading\n'
                                'ExcessLiquidity — This value shows your '
                                'margin cushion, before liquidation\n'
                                'Cushion — Excess liquidity as a '
                                'percentage of net liquidation value\n'
                                'FullInitMarginReq — Initial Margin of '
                                'whole portfolio with no discounts or '
                                'intraday credits\n'
                                'FullMaintMarginReq — Maintenance Margin '
                                'of whole portfolio with no discounts or '
                                'intraday credits\n'
                                'FullAvailableFunds — Available funds of '
                                'whole portfolio with no discounts or '
                                'intraday credits\n'
                                'FullExcessLiquidity — Excess liquidity of '
                                'whole portfolio with no discounts or '
                                'intraday credits\n'
                                'LookAheadNextChange — Time when '
                                'look-ahead values take effect\n'
                                'LookAheadInitMarginReq — Initial Margin '
                                'requirement of whole portfolio as of next '
                                "period's margin change\n"
                                'LookAheadMaintMarginReq — Maintenance '
                                'Margin requirement of whole portfolio as '
                                "of next period's margin change\n"
                                'LookAheadAvailableFunds — This value '
                                'reflects your available funds at the next '
                                'margin change\n'
                                'LookAheadExcessLiquidity — This value '
                                'reflects your excess liquidity at the '
                                'next margin change\n'
                                'HighestSeverity — A measure of how close '
                                'the account is to liquidation\n'
                                'DayTradesRemaining — The Number of '
                                'Open/Close trades a user could put on '
                                'before Pattern Day Trading is detected. A '
                                'value of "-1" means that the user can put '
                                'on unlimited day trades.\n'
                                'Leverage — GrossPositionValue / '
                                'NetLiquidation\n'
                                '$LEDGER — Single flag to relay all cash '
                                'balance tags*, only in base currency.\n'
                                '$LEDGER:CURRENCY — Single flag to relay '
                                'all cash balance tags*, only in the '
                                'specified currency.\n'
                                '$LEDGER:ALL — Single flag to relay all '
                                'cash balance tags* in all currencies.'}),
 'reqAccountUpdates': ("Subscribes to an specific account's information and "
                       "portfolio Through this method, a single account's "
                       'subscription can be started/stopped. As a result '
                       "from the subscription, the account's information, "
                       'portfolio and last update time will be received at '
                       'EWrapper::updateAccountValue, '
                       'EWrapper::updateAccountPortfolio, '
                       'EWrapper::updateAccountTime respectively. Only one '
                       'account can be subscribed at a time. A second '
                       'subscription request for another account when the '
                       'previous one is still active will cause the first '
                       'one to be canceled in favour of the second one. '
                       'Consider user reqPositions if you want to retrieve '
                       "all your accounts' portfolios directly.",
                       ['subscribe', 'acctCode'],
                       ['bool', 'string'],
                       {'acctCode': 'the account id (i.e. U123456) for '
                                    'which the information is requested.',
                        'subscribe': 'set to true to start the '
                                     'subscription and to false to stop it.'}),
 'reqAccountUpdatesMulti': ('Requests account updates for account and/or '
                            'model.',
                            ['requestId',
                             'account',
                             'modelCode',
                             'ledgerAndNLV'],
                            ['int', 'string', 'string', 'bool'],
                            {}),
 'reqAllOpenOrders': ('Requests all open orders submitted by any API client '
                      'as well as those directly placed in the TWS. The '
                      'existing orders will be received via the openOrder '
                      'and orderStatus events.',
                      [''],
                      [],
                      {}),
 'reqAutoOpenOrders': ('Requests all order placed on the TWS directly. Only '
                       'the orders created after this request has been made '
                       'will be returned.',
                       ['autoBind'],
                       ['bool'],
                       {'autoBind': 'if set to true, the newly created '
                                    'orders will be implicitely associated '
                                    'with this client.'}),
 'reqContractDetails': ('Requests contract information. This method will '
                        'provide all the contracts matching the contract '
                        'provided. It can also be used to retrieve complete '
                        'options and futures chains. This information will '
                        'be returned at EWrapper:contractDetails. Though it '
                        'is now (in API version > 9.72.12) advised to use '
                        'reqSecDefOptParams for that purpose.',
                        ['reqId', 'contract'],
                        ['int', 'Contract'],
                        {'contract': 'the contract used as sample to query '
                                     'the available contracts. Typically, '
                                     'it will contain the '
                                     'Contract::Symbol, '
                                     'Contract::Currency, '
                                     'Contract::SecType, Contract::Exchange',
                         'reqId': 'the unique request identifier.'}),
 'reqCurrentTime': ("Requests the server's current time.", [''], [], {}),
 'reqExecutions': ("Requests all the day's executions matching the filter. "
                   "Only the current day's executions can be retrieved. "
                   'Along with the executions, the CommissionReport will '
                   'also be returned. The execution details will arrive at '
                   'EWrapper:execDetails.',
                   ['reqId', 'filter'],
                   ['int', 'ExecutionFilter'],
                   {'filter': 'the filter criteria used to determine which '
                              'execution reports are returned.',
                    'reqId': "the request's unique identifier."}),
 'reqFundamentalData': ("Requests the contract's Reuters' global "
                        'fundamental data. Reuters funalmental data will be '
                        'returned at EWrapper::fundamentalData.',
                        ['reqId',
                         'contract',
                         'reportType',
                         'fundamentalDataOptions'],
                        ['int', 'Contract', 'String', 'TagValue'],
                        {'contract': "the contract's description for which "
                                     'the data will be returned.',
                         'reportType': 'there are three available report '
                                       'types:\n'
                                       'ReportSnapshot: Company overview\n'
                                       'ReportsFinSummary: Financial '
                                       'summary\n'
                                       'ReportRatios: Financial ratios\n'
                                       'ReportsFinStatements: Financial '
                                       'statements\n'
                                       'RESC: Analyst estimates\n'
                                       'CalendarReport: Company calendar',
                         'reqId': "the request's unique identifier."}),
 'reqGlobalCancel': ('Cancels all the active orders. This method will '
                     'cancel ALL open orders included those placed directly '
                     'via the TWS.',
                     [''],
                     [],
                     {}),
 'reqHistoricalData': ("Requests contracts' historical data. When "
                       'requesting historical data, a finishing time and '
                       'date is required along with a duration string. For '
                       'example, having:',
                       ['tickerId',
                        'contract',
                        'endDateTime',
                        'durationString',
                        'barSizeSetting',
                        'whatToShow',
                        'useRTH',
                        'formatDate',
                        'chartOptions'],
                       ['int',
                        'Contract',
                        'string',
                        'string',
                        'string',
                        'string',
                        'int',
                        'int',
                        'TagValue'],
                       {'barSizeSetting': 'the size of the bar:\n'
                                          '1 sec\n'
                                          '5 secs\n'
                                          '15 secs\n'
                                          '30 secs\n'
                                          '1 min\n'
                                          '2 mins\n'
                                          '3 mins\n'
                                          '5 mins\n'
                                          '15 mins\n'
                                          '30 mins\n'
                                          '1 hour\n'
                                          '1 day',
                        'contract': 'the contract for which we want to '
                                    'retrieve the data.',
                        'durationString': 'the amount of time for which '
                                          'the data needs to be '
                                          'retrieved:\n'
                                          '" S (seconds)\n'
                                          '     - " D (days)\n'
                                          '" W (weeks)\n'
                                          '     - " M (months)\n'
                                          '" Y (years)',
                        'endDateTime': "request's ending time with format "
                                       'yyyyMMdd HH:mm:ss {TMZ}',
                        'formatDate': "set to 1 to obtain the bars' time "
                                      'as yyyyMMdd HH:mm:ss, set to 2 to '
                                      'obtain it like system time format '
                                      'in seconds',
                        'tickerId': "the request's unique identifier.",
                        'useRTH': 'set to 0 to obtain the data which was '
                                  'also generated outside of the Regular '
                                  'Trading Hours, set to 1 to obtain only '
                                  'the RTH data',
                        'whatToShow': 'the kind of information being '
                                      'retrieved:\n'
                                      'TRADES\n'
                                      'MIDPOINT\n'
                                      'BID\n'
                                      'ASK\n'
                                      'BID_ASK\n'
                                      'HISTORICAL_VOLATILITY\n'
                                      'OPTION_IMPLIED_VOLATILITY\n'
                                      'FREE_RATE\n'
                                      'REBATE_RATE'}),
 'reqIds': ('Requests the next valid order id.',
            ['numIds'],
            ['int'],
            {'numIds': 'deprecated- this parameter will not affect the '
                       'value returned to nextValidId'}),
 'reqManagedAccts': ('Requests the accounts to which the logged user has '
                     'access to.',
                     [''],
                     [],
                     {}),
 'reqMarketDataType': ('indicates the TWS to switch to "frozen", "delayed" '
                       'or "delayed-frozen" market data. The API can '
                       'receive frozen market data from Trader Workstation. '
                       'Frozen market data is the last data recorded in our '
                       'system. During normal trading hours, the API '
                       'receives real-time market data. If you use this '
                       'function, you are telling TWS to automatically '
                       'switch to frozen market data after the close. Then, '
                       'before the opening of the next trading day, market '
                       'data will automatically switch back to real-time '
                       'market data.',
                       ['marketDataType'],
                       ['int'],
                       {'marketDataType': 'set to 1 for real time '
                                          'streaming, set to 2 for frozen '
                                          'market data, set to 3 for '
                                          'delayed market data, set to 4 '
                                          'for delayed-frozen market data. '
                                          'Note: At the present time, only '
                                          'data types 1 and 2 are '
                                          'supported.'}),
 'reqMktData': ('Requests real time market data. This function will return '
                "the product's market data. It is important to notice that "
                'only real time data can be delivered via the API.',
                ['tickerId',
                 'contract',
                 'genericTickList',
                 'snapshot',
                 'mktDataOptions'],
                ['int', 'Contract', 'string', 'bool', 'TagValue'],
                {'contract': 'the Contract for which the data is being '
                             'requested',
                 'genericTickList': 'comma separated ids of the available '
                                    'generic ticks:\n'
                                    '100 Option Volume (currently for '
                                    'stocks)\n'
                                    '101 Option Open Interest (currently '
                                    'for stocks)\n'
                                    '104 Historical Volatility (currently '
                                    'for stocks)\n'
                                    '106 Option Implied Volatility '
                                    '(currently for stocks)\n'
                                    '162 Index Future Premium\n'
                                    '165 Miscellaneous Stats\n'
                                    '221 Mark Price (used in TWS P&L '
                                    'computations)\n'
                                    '225 Auction values (volume, price and '
                                    'imbalance)\n'
                                    '233 RTVolume - contains the last '
                                    'trade price, last trade size, last '
                                    'trade time, total volume, VWAP, and '
                                    'single trade flag.\n'
                                    '236 Shortable\n'
                                    '256 Inventory\n'
                                    '258 Fundamental Ratios\n'
                                    '411 Realtime Historical Volatility\n'
                                    '456 IBDividends',
                 'snapshot': 'when set to true, it will provide a single '
                             'snapshot of the available data. Set to false '
                             'if you want to receive continuous updates.',
                 'tickerId': "the request's identifier"}),
 'reqMktDepth': ("Requests the contract's market depth (order book). Note "
                 'this request must be direct-routed to an exchange and not '
                 'smart-routed. The number of simultaneous market depth '
                 'requests allowed in an account is calculated based on a '
                 'formula that looks at an accounts equity, commissions, '
                 'and quote booster packs.',
                 ['tickerId', 'contract', 'numRows', 'mktDepthOptions'],
                 ['int', 'Contract', 'int', 'TagValue'],
                 {'contract': 'the Contract for which the depth is being '
                              'requested',
                  'numRows': 'the number of rows on each side of the order '
                             'book',
                  'tickerId': "the request's identifier"}),
 'reqNewsBulletins': ("Subscribes to IB's News Bulletins.",
                      ['allMessages'],
                      ['bool'],
                      {'allMessages': 'if set to true, will return all the '
                                      'existing bulletins for the current '
                                      'day, set to false to receive only '
                                      'the new bulletins.'}),
 'reqOpenOrders': ('Requests all open orders places by this specific API '
                   'client (identified by the API client id)',
                   [''],
                   [],
                   {}),
 'reqPositions': ('Requests all positions from all accounts.', [''], [], {}),
 'reqPositionsMulti': ('Requests positions for account and/or model.',
                       ['requestId', 'account', 'modelCode'],
                       ['int', 'string', 'string'],
                       {'account': '- If an account Id is provided, only '
                                   "the account's positions belonging to "
                                   'the specified model will be delivered  '
                                   "modelCode - The code of the model's "
                                   'positions we are interested in.',
                        'requestId': "- Request's identifier"}),
 'reqRealTimeBars': ('Requests real time bars Currently, only 5 seconds '
                     'bars are provided. This request is subject to the '
                     'same pacing as any historical data request: no more '
                     'than 60 API queries in more than 600 seconds. Real '
                     'time bars subscriptions are also included in the '
                     'calculation of the number of Level 1 market data '
                     'subscriptions allowed in an account.',
                     ['tickerId',
                      'contract',
                      'barSize',
                      'whatToShow',
                      'useRTH',
                      'realTimeBarsOptions'],
                     ['int', 'Contract', 'int', 'string', 'bool', 'TagValue'],
                     {'barSize': 'currently being ignored',
                      'contract': 'the Contract for which the depth is '
                                  'being requested',
                      'tickerId': "the request's unique identifier.",
                      'useRTH': 'set to 0 to obtain the data which was '
                                'also generated ourside of the Regular '
                                'Trading Hours, set to 1 to obtain only '
                                'the RTH data',
                      'whatToShow': 'the nature of the data being '
                                    'retrieved:\n'
                                    'TRADES\n'
                                    'MIDPOINT\n'
                                    'BID\n'
                                    'ASK'}),
 'reqScannerParameters': ('Requests all possible parameters which can be '
                          'used for a scanner subscription.',
                          [''],
                          [],
                          {}),
 'reqScannerSubscription': ('Starts a subscription to market scan results '
                            'based on the provided parameters.',
                            ['reqId',
                             'subscription',
                             'scannerSubscriptionOptions'],
                            ['int', 'ScannerSubscription', 'TagValue'],
                            {'reqId': "the request's identifier",
                             'subscription': 'summary of the scanner '
                                             'subscription including its '
                                             'filters.'}),
 'reqSecDefOptParams': ('Requests security definition option parameters for '
                        "viewing a contract's option chain  reqId the ID "
                        'chosen for the request  underlyingSymbol  '
                        'futFopExchange The exchange on which the returned '
                        'options are trading. Can be set to the empty '
                        'string "" for all exchanges.  underlyingSecType '
                        'The type of the underlying security, i.e. STK  '
                        'underlyingConId the contract ID of the underlying '
                        'security.',
                        ['reqId',
                         'underlyingSymbol',
                         'futFopExchange',
                         'underlyingSecType',
                         'underlyingConId'],
                        ['int', 'string', 'string', 'string', 'int'],
                        {}),
 'requestFA': ('Requests the FA configuration A Financial Advisor can '
               'define three different configurations:',
               ['faDataType'],
               ['int'],
               {'faDataType': 'the configuration to change. Set to 1, 2 or '
                              '3 as defined above.'}),
 'updateDisplayGroup': ('Updates the contract displayed in a TWS Window '
                        'Group  requestId is the ID chosen for this '
                        'request  contractInfo is an encoded value '
                        'designating a unique IB contract. Possible values '
                        'include:',
                        ['requestId', 'contractInfo'],
                        ['int', 'string'],
                        {})}
