
IBCLASS_DOCS = {'ComboLeg': {'Action': ('string', 'The side (buy or sell) of the leg: .'),
              'ConId': ('int', "The Contract's IB's unique id."),
              'DesignatedLocation': ('string',
                                     'When ShortSaleSlot is 2, this field '
                                     'shall contain the designated '
                                     'location.'),
              'Exchange': ('string',
                           'The destination exchange to which the order '
                           'will be routed.'),
              'ExemptCode': ('int', 'DOC_TODO.'),
              'OpenClose': ('int',
                            'Specifies whether an order is an open or '
                            'closing order. For instituational customers '
                            'to determine if this order is to open or '
                            'close a position. 0 - Same as the parent '
                            'security. This is the only option for retail '
                            'customers.\n'
                            ' 1 - Open. This value is only valid for '
                            'institutional customers.\n'
                            ' 2 - Close. This value is only valid for '
                            'institutional customers.\n'
                            ' 3 - Unknown.'),
              'Ratio': ('int',
                        'Select the relative number of contracts for the '
                        'leg you are constructing. To help determine the '
                        'ratio for a specific combination order, refer to '
                        "the Interactive Analytics section of the User's "
                        'Guide.'),
              'ShortSaleSlot': ('int',
                                'For stock legs when doing short selling. '
                                'Set to 1 = clearing broker, 2 = third '
                                'party.')},
 'CommissionReport': {'Commission': ('double', 'the commissions cost.'),
                      'Currency': ('string', 'the reporting currency.'),
                      'ExecId': ('string',
                                 "the execution's id this commission "
                                 'belongs to.'),
                      'RealizedPNL': ('double',
                                      'the realised profit and loss'),
                      'Yield': ('double', 'The income return.'),
                      'YieldRedemptionDate': ('int',
                                              'date expressed in yyyymmdd '
                                              'format.')},
 'Contract': {'ComboLegs': ('List< ComboLeg >',
                            'The legs of a combined contract definition.'),
              'ComboLegsDescription': ('string',
                                       'Description of the combo legs.'),
              'ConId': ('int', 'The unique IB contract identifier.'),
              'Currency': ('string', "The underlying's cuurrency."),
              'Exchange': ('string', 'The destination exchange.'),
              'IncludeExpired': ('bool',
                                 'If set to true, contract details '
                                 'requests and historical data queries can '
                                 'be performed pertaining to expired '
                                 'contracts. Note: Historical data queries '
                                 'on expired contracts are limited to the '
                                 'last year of the contracts life, and are '
                                 'initially only supported for expired '
                                 'futures contracts.'),
              'LastTradeDateOrContractMonth': ('string',
                                               "The contract's last "
                                               'trading day or contract '
                                               'month (for Options and '
                                               'Futures). Strings with '
                                               'format YYYYMM will be '
                                               'interpreted as the '
                                               'Contract Month whereas '
                                               'YYYYMMDD will be '
                                               'interpreted as Last '
                                               'Trading Day.'),
              'LocalSymbol': ('string',
                              "The contract's symbol within its primary "
                              'exchange.'),
              'Multiplier': ('string',
                             "The instrument's multiplier (i.e. options, "
                             'futures).'),
              'PrimaryExch': ('string', "The contract's primary exchange."),
              'Right': ('string',
                        'Either Put or Call (i.e. Options). Valid values '
                        'are P, PUT, C, CALL.'),
              'SecId': ('string', 'Identifier of the security type.'),
              'SecIdType': ('string',
                            "Security's identifier when querying "
                            "contract's details or placing orders SIN - "
                            'Example: Apple: US0378331005 CUSIP - Example: '
                            'Apple: 037833100 SEDOL - Consists of 6-AN + '
                            'check digit. Example: BAE: 0263494 RIC - '
                            'Consists of exchange-independent RIC Root and '
                            'a suffix identifying the exchange. Example: '
                            'AAPL.O for Apple on NASDAQ.'),
              'SecType': ('string',
                          "The security's type: STK - stock (or ETF) OPT - "
                          'option FUT - future IND - index FOP - futures '
                          'option CASH - forex pair BAG - combo WAR - '
                          'warrant BOND- bond CMDTY- commodity NEWS- news '
                          'FUND- mutual fund.'),
              'Strike': ('double', "The option's strike price."),
              'Symbol': ('string', "The underlying's asset symbol."),
              'TradingClass': ('string',
                               'The trading class name for this contract. '
                               'Available in TWS contract description '
                               "window as well. For example, GBL Dec '13 "
                               'future\'s trading class is "FGBL".'),
              'UnderComp': ('UnderComp',
                            'Delta and underlying price for Delta-Neutral '
                            'combo orders. Underlying (STK or FUT), delta '
                            'and underlying price goes into this attribute.')},
 'ContractDetails': {'BondType': ('string',
                                  'The type of bond, such as "CORP.".'),
                     'Callable': ('bool',
                                  'If true, the bond can be called by the '
                                  'issuer under certain conditions. For '
                                  'Bonds only.'),
                     'Category': ('string',
                                  'The industry category of the '
                                  'underlying. For example, InvestmentSvc.'),
                     'ContractMonth': ('string',
                                       'Typically the contract month of '
                                       'the underlying for a Future '
                                       'contract.'),
                     'Convertible': ('bool',
                                     'Values are True or False. If true, '
                                     'the bond can be converted to stock '
                                     'under certain conditions. For Bonds '
                                     'only.'),
                     'Coupon': ('double',
                                'The interest rate used to calculate the '
                                'amount you will receive in interest '
                                'payments over the course of the year. For '
                                'Bonds only.'),
                     'CouponType': ('string',
                                    'The type of bond coupon. For Bonds '
                                    'only.'),
                     'Cusip': ('string',
                               'The nine-character bond CUSIP or the '
                               '12-character SEDOL. For Bonds only.'),
                     'DescAppend': ('string',
                                    'A description string containing '
                                    'further descriptive information about '
                                    'the bond. For Bonds only.'),
                     'EvMultiplier': ('double',
                                      'Tells you approximately how much '
                                      'the market value of a contract '
                                      'would change if the price were to '
                                      'change by 1. It cannot be used to '
                                      'get market value by multiplying the '
                                      'price by the approximate multiplier.'),
                     'EvRule': ('string',
                                'Contains the Economic Value Rule name and '
                                'the respective optional argument. The two '
                                'values should be separated by a colon. '
                                'For example, '
                                'aussieBond:YearsToExpiration=3. When the '
                                'optional argument is not present, the '
                                'first value will be followed by a colon.'),
                     'Industry': ('string',
                                  'The industry classification of the '
                                  'underlying/product. For example, '
                                  'Financial.'),
                     'IssueDate': ('string',
                                   'The date the bond was issued. For '
                                   'Bonds only.'),
                     'LiquidHours': ('string',
                                     'The liquid hours of the product. '
                                     'This value will contain the liquid '
                                     'hours of the current day as well as '
                                     "the next's. For example, "
                                     '20090507:0700-1830,1830-2330;20090508:CLOSED.'),
                     'LongName': ('string',
                                  'Descriptive name of the product.'),
                     'MarketName': ('string',
                                    'The market name for this product.'),
                     'Maturity': ('string',
                                  'he date on which the issuer must repay '
                                  'the face value of the bond. For Bonds '
                                  'only.'),
                     'MinTick': ('double',
                                 'The minimum allowed price variation. '
                                 'Note that many securities vary their '
                                 'minimum tick size according to their '
                                 'price. This value will only show the '
                                 'smallest of the different minimum tick '
                                 "sizes regardless of the product's price."),
                     'NextOptionDate': ('string',
                                        'Only if bond has embedded '
                                        'options. Refers to callable bonds '
                                        'and puttable bonds. Available in '
                                        'TWS description window for bonds.'),
                     'NextOptionPartial': ('bool',
                                           'Only if bond has embedded '
                                           'options. For Bonds only.'),
                     'NextOptionType': ('string',
                                        'Type of embedded option. Only if '
                                        'bond has embedded options.'),
                     'Notes': ('string',
                               "If populated for the bond in IB's "
                               'database. For Bonds only.'),
                     'OrderTypes': ('string',
                                    'Supported order types for this '
                                    'product.'),
                     'PriceMagnifier': ('int',
                                        'Allows execution and strike '
                                        'prices to be reported '
                                        'consistently with market data, '
                                        'historical data and the order '
                                        'price, i.e. Z on LIFFE is '
                                        'reported in Index points and not '
                                        'GBP.'),
                     'Putable': ('bool',
                                 'Values are True or False. If true, the '
                                 'bond can be sold back to the issuer '
                                 'under certain conditions. For Bonds only.'),
                     'Ratings': ('string',
                                 'Identifies the credit rating of the '
                                 'issuer. For Bonds only. A higher credit '
                                 'rating generally indicates a less risky '
                                 'investment. Bond ratings are from '
                                 "Moody's and S&P respectively."),
                     'SecIdList': ('List< TagValue >',
                                   'A list of contract identifiers that '
                                   'the customer is allowed to view. '
                                   'CUSIP/ISIN/etc.'),
                     'Subcategory': ('string',
                                     'The industry subcategory of the '
                                     'underlying. For example, Brokerage.'),
                     'Summary': ('Contract',
                                 'A Contract object summarising this '
                                 'product.'),
                     'TimeZoneId': ('string',
                                    'The ID of the time zone for the '
                                    'trading hours of the product. For '
                                    'example, EST.'),
                     'TradingHours': ('string',
                                      'The trading hours of the product. '
                                      'This value will contain the trading '
                                      'hours of the current day as well as '
                                      "the next's. For example, "
                                      '20090507:0700-1830,1830-2330;20090508:CLOSED.'),
                     'UnderConId': ('int', "Underlying's contract Id."),
                     'ValidExchanges': ('string',
                                        'Exchanges on which this product '
                                        'is traded.')},
 'Execution': {'AcctNumber': ('string',
                              'The account to which the order was '
                              'allocated.'),
               'AvgPrice': ('double',
                            'Average price. Used in regular trades, combo '
                            'trades and legs of the combo. Includes '
                            'commissions.'),
               'ClientId': ('int',
                            'The API client identifier which placed the '
                            'order which originated this execution.'),
               'CumQty': ('int',
                          'Cumulative quantity. Used in regular trades, '
                          'combo trades and legs of the combo.'),
               'EvMultiplier': ('double',
                                'Tells you approximately how much the '
                                'market value of a contract would change '
                                'if the price were to change by 1. It '
                                'cannot be used to get market value by '
                                'multiplying the price by the approximate '
                                'multiplier.'),
               'EvRule': ('string',
                          'The Economic Value Rule name and the respective '
                          'optional argument. The two values should be '
                          'separated by a colon. For example, '
                          'aussieBond:YearsToExpiration=3. When the '
                          'optional argument is not present, the first '
                          'value will be followed by a colon.'),
               'Exchange': ('string',
                            'The exchange where the execution took place.'),
               'ExecId': ('string', "The execution's identifier."),
               'Liquidation': ('int',
                               'Identifies whether an execution occurred '
                               'because of an IB-initiated liquidation.'),
               'ModelCode': ('string', 'model code'),
               'OrderId': ('int', "The API client's order Id."),
               'OrderRef': ('string',
                            'Allows API client to add a reference to an '
                            'order.'),
               'PermId': ('int',
                          'The TWS order identifier. The PermId can be 0 '
                          'for trades originating outside IB.'),
               'Price': ('double',
                         "The order's execution price excluding "
                         'commissions.'),
               'Shares': ('double', 'The number of shares filled.'),
               'Side': ('string',
                        'Specifies if the transaction was buy or sale BOT '
                        'for bought, SLD for sold.'),
               'Time': ('string', "The execution's server time.")},
 'ExecutionFilter': {'AcctCode': ('string',
                                  'The account to which the order was '
                                  'allocated to.'),
                     'ClientId': ('int',
                                  'The API client which placed the order.'),
                     'Exchange': ('string',
                                  'The exchange at which the execution was '
                                  'produced.'),
                     'SecType': ('string',
                                 "The Contract's security's type (i.e. "
                                 'STK, OPT...)'),
                     'Side': ('string', "The Contract's side (Put or Call)."),
                     'Symbol': ('string', "The instrument's symbol."),
                     'Time': ('string',
                              'Time from which the executions will be '
                              'brough yyyymmdd hh:mm:ss Only those '
                              'executions reported after the specified '
                              'time will be returned.')},
 'Order': {'Account': ('string',
                       'The account the trade will be allocated to.'),
           'Action': ('string',
                      'Identifies the side. Possible values are BUY, SELL, '
                      'SSHORT.'),
           'ActiveStartTime': ('string', 'for GTC orders.'),
           'ActiveStopTime': ('string', 'for GTC orders.'),
           'AdjustableTrailingUnit': ('int',
                                      'Adjusted Stop orders: specifies '
                                      'where the trailing unit is an '
                                      'amount (set to 0) or a percentage '
                                      '(set to 1)'),
           'AdjustedOrderType': ('string',
                                 'Adjusted Stop orders: the parent order '
                                 'will be adjusted to the given type when '
                                 'the adjusted trigger price is penetrated.'),
           'AdjustedStopLimitPrice': ('double',
                                      'Adjusted Stop orders: specifies the '
                                      'stop limit price of the adjusted '
                                      '(STPL LMT) parent.'),
           'AdjustedStopPrice': ('double',
                                 'Adjusted Stop orders: specifies the stop '
                                 'price of the adjusted (STP) parent.'),
           'AdjustedTrailingAmount': ('double',
                                      'Adjusted Stop orders: specifies the '
                                      'trailing amount of the adjusted '
                                      '(TRAIL) parent.'),
           'AlgoId': ('string', ''),
           'AlgoParams': ('List< TagValue >',
                          'The list of parameters for the IB algorithm. '
                          "For more information about IB's API algorithms, "
                          'refer to '
                          'https://www.interactivebrokers.com/en/software/api/apiguide/tables/ibalgo_parameters.htm.'),
           'AlgoStrategy': ('string',
                            'The algorithm strategy. As of API verion 9.6, '
                            'the following algorithms are supported:\n'
                            ' ArrivalPx - Arrival Price \n'
                            ' DarkIce - Dark Ice \n'
                            ' PctVol - Percentage of Volume \n'
                            ' Twap - TWAP (Time Weighted Average Price) \n'
                            ' Vwap - VWAP (Volume Weighted Average '
                            'Price) \n'
                            " For more information about IB's API "
                            'algorithms, refer to '
                            'https://www.interactivebrokers.com/en/software/api/apiguide/tables/ibalgo_parameters.htm.'),
           'AllOrNone': ('bool',
                         'Indicates whether or not all the order has to be '
                         'filled on a single execution.'),
           'AuctionStrategy': ('int',
                               'For BOX orders only. Values include: 1 - '
                               'match \n'
                               ' 2 - improvement \n'
                               ' 3 - transparent'),
           'AuxPrice': ('double',
                        'Generic field to contain the stop price for STP '
                        'LMT orders, trailing amount, etc.'),
           'BasisPoints': ('double', 'DOC_TODO For EFP orders only.'),
           'BasisPointsType': ('int', 'DOC_TODO For EFP orders only.'),
           'BlockOrder': ('bool',
                          'If set to true, specifies that the order is an '
                          'ISE Block order.'),
           'ClearingAccount': ('string',
                               'Specifies the true beneficiary of the '
                               'order. For IBExecution customers. This '
                               'value is required for FUT/FOP orders for '
                               'reporting to the exchange.'),
           'ClearingIntent': ('string',
                              'For exeuction-only clients to know where do '
                              'they want their shares to be cleared at. '
                              'Valid values are: IB, Away, and PTA (post '
                              'trade allocation).'),
           'ClientId': ('int', 'The API client id which placed the order.'),
           'Conditions': ('List< OrderCondition >',
                          'Conditions determining when the order will be '
                          'activated or canceled.'),
           'ConditionsCancelOrder': ('bool',
                                     'Conditions can determine if an order '
                                     'should become active or canceled.'),
           'ConditionsIgnoreRth': ('bool',
                                   'Indicates whether or not conditions '
                                   'will also be valid outside Regular '
                                   'Trading Hours.'),
           'ContinuousUpdate': ('int',
                                'Specifies whether TWS will automatically '
                                'update the limit price of the order as '
                                'the underlying price moves. VOL orders '
                                'only.'),
           'Delta': ('double', "The stock's Delta. For orders on BOX only."),
           'DeltaNeutralAuxPrice': ('double',
                                    'Use this field to enter a value if '
                                    'the value in the '
                                    'deltaNeutralOrderType field is an '
                                    'order type that requires an Aux '
                                    'price, such as a REL order. VOL '
                                    'orders only.'),
           'DeltaNeutralClearingAccount': ('string', 'DOC_TODO'),
           'DeltaNeutralClearingIntent': ('string', 'DOC_TODO'),
           'DeltaNeutralConId': ('int', 'DOC_TODO'),
           'DeltaNeutralDesignatedLocation': ('string',
                                              'Used only when '
                                              'deltaNeutralShortSaleSlot = '
                                              '2.'),
           'DeltaNeutralOpenClose': ('string',
                                     'Specifies whether the order is an '
                                     'Open or a Close order and is used '
                                     'when the hedge involves a CFD and '
                                     'and the order is clearing away.'),
           'DeltaNeutralOrderType': ('string',
                                     'Enter an order type to instruct TWS '
                                     'to submit a delta neutral trade on '
                                     'full or partial execution of the VOL '
                                     'order. VOL orders only. For no hedge '
                                     'delta order to be sent, specify NONE.'),
           'DeltaNeutralSettlingFirm': ('string', 'DOC_TODO'),
           'DeltaNeutralShortSale': ('bool',
                                     'Used when the hedge involves a stock '
                                     'and indicates whether or not it is '
                                     'sold short.'),
           'DeltaNeutralShortSaleSlot': ('int',
                                         'Has a value of 1 (the clearing '
                                         'broker holds shares) or 2 '
                                         '(delivered from a third party). '
                                         'If you use 2, then you must '
                                         'specify a '
                                         'deltaNeutralDesignatedLocation.'),
           'DesignatedLocation': ('string',
                                  'Used only when shortSaleSlot is 2. For '
                                  'institutions only. Indicates the '
                                  'location where the shares to short come '
                                  'from. Used only when short sale slot is '
                                  'set to 2 (which means that the shares '
                                  'to short are held elsewhere and not '
                                  'with IB).'),
           'DiscretionaryAmt': ('double',
                                'The amount off the limit price allowed '
                                'for discretionary orders.'),
           'DisplaySize': ('int',
                           'The publicly disclosed order size, used when '
                           'placing Iceberg orders.'),
           'ETradeOnly': ('bool', 'Trade with electronic quotes.'),
           'ExemptCode': ('int', ''),
           'ExtOperator': ('string',
                           'This is a regulartory attribute that applies '
                           'to all US Commodity (Futures) Exchanges, '
                           'provided to allow client to comply with CFTC '
                           'Tag 50 Rules.'),
           'FaGroup': ('string',
                       'The Financial Advisor group the trade will be '
                       'allocated to. Use an empty string if not '
                       'applicable.'),
           'FaMethod': ('string',
                        'The Financial Advisor allocation method the trade '
                        'will be allocated to. Use an empty string if not '
                        'applicable.'),
           'FaPercentage': ('string',
                            'The Financial Advisor percentage concerning '
                            "the trade's allocation. Use an empty string "
                            'if not applicable.'),
           'FaProfile': ('string',
                         'The Financial Advisor allocation profile the '
                         'trade will be allocated to. Use an empty string '
                         'if not applicable.'),
           'FirmQuoteOnly': ('bool', 'Trade with firm quotes.'),
           'GoodAfterTime': ('string',
                             'Specifies the date and time after which the '
                             'order will be active. Format: yyyymmdd '
                             'hh:mm:ss {optional Timezone}.'),
           'GoodTillDate': ('string',
                            'The date and time until the order will be '
                            'active. You must enter GTD as the time in '
                            'force to use this string. The trade\'s "Good '
                            'Till Date," format "YYYYMMDD hh:mm:ss '
                            '(optional time zone)".'),
           'HedgeParam': ('string',
                          'DOC_TODO Beta = x for Beta hedge orders, ratio '
                          '= y for Pair hedge order'),
           'HedgeType': ('string',
                         'For hedge orders. Possible values include:\n'
                         ' D - delta \n'
                         ' B - beta \n'
                         ' F - FX \n'
                         ' P - Pair \n'
                         '.'),
           'Hidden': ('bool',
                      'If set to true, the order will not be visible when '
                      'viewing the market depth. This option only applies '
                      'to orders routed to the ISLAND exchange.'),
           'IsPeggedChangeAmountDecrease': ('bool',
                                            'Pegged-to-benchmark orders: '
                                            "indicates whether the order's "
                                            'pegged price should increase '
                                            'or decreases.'),
           'LmtPrice': ('double',
                        'The LIMIT price. Used for limit, stop-limit and '
                        'relative orders. In all other cases specify zero. '
                        'For relative orders with no limit price, also '
                        'specify zero.'),
           'LmtPriceOffset': ('double', 'DOC_TODO'),
           'MinQty': ('int', 'Identifies a minimum quantity order type.'),
           'ModelCode': ('string', 'model code'),
           'NbboPriceCap': ('double',
                            'Maximum smart order distance from the NBBO.'),
           'NotHeld': ('bool',
                       'Orders routed to IBDARK are tagged as “post only” '
                       "and are held in IB's order book, where incoming "
                       'SmartRouted orders from other IB customers are '
                       'eligible to trade against them. For IBDARK orders '
                       'only.'),
           'OcaGroup': ('string', 'One-Cancels-All group identifier.'),
           'OcaType': ('int',
                       'Tells how to handle remaining orders in an OCA '
                       'group when one order or part of an order executes. '
                       'Valid values are:\n'
                       '  1 = Cancel all remaining orders with block.\n'
                       '  2 = Remaining orders are proportionately reduced '
                       'in size with block.\n'
                       '  3 = Remaining orders are proportionately reduced '
                       'in size with no block.\n'
                       ' If you use a value "with block" gives your order '
                       'has overfill protection. This means that only one '
                       'order in the group will be routed at a time to '
                       'remove the possibility of an overfill.'),
           'OpenClose': ('string',
                         'For institutional customers only. Available for '
                         'institutional clients to determine if this order '
                         'is to open or close a position. Valid values are '
                         'O (open), C (close).'),
           'OptOutSmartRouting': ('bool',
                                  'Use to opt out of default SmartRouting '
                                  'for orders routed directly to ASX. This '
                                  'attribute defaults to false unless '
                                  'explicitly set to true. When set to '
                                  'false, orders routed directly to ASX '
                                  'will NOT use SmartRouting. When set to '
                                  'true, orders routed directly to ASX '
                                  'orders WILL use SmartRouting.'),
           'OrderComboLegs': ('List< OrderComboLeg >',
                              'The attributes for all legs within a combo '
                              'order.'),
           'OrderId': ('int', "The API client's order id."),
           'OrderMiscOptions': ('List< TagValue >', 'DOC_TODO'),
           'OrderRef': ('string',
                        'The order reference. Intended for institutional '
                        'customers only, although all customers may use it '
                        'to identify the API client that sent the order '
                        'when multiple API clients are running.'),
           'OrderType': ('string',
                         "The order's type. Available Orders are at "
                         'https://www.interactivebrokers.com/en/software/api/apiguide/tables/supported_order_types.htm.'),
           'Origin': ('int',
                      'The order\'s origin. Same as TWS "Origin" column. '
                      'Identifies the type of customer from which the '
                      'order originated. Valid values are 0 (customer), 1 '
                      '(firm).'),
           'OutsideRth': ('bool',
                          'If set to true, allows orders to also trigger '
                          'or fill outside of regular trading hours.'),
           'OverridePercentageConstraints': ('bool',
                                             'Overrides TWS constraints. '
                                             'Precautionary constraints '
                                             'are defined on the TWS '
                                             'Presets page, and help '
                                             'ensure tha tyour price and '
                                             'size order values are '
                                             'reasonable. Orders sent from '
                                             'the API are also validated '
                                             'against these safety '
                                             'constraints, and may be '
                                             'rejected if any constraint '
                                             'is violated. To override '
                                             'validation, set this '
                                             'parameter’s value to True.'),
           'ParentId': ('int',
                        'The order ID of the parent order, used for '
                        'bracket and auto trailing stop orders.'),
           'PeggedChangeAmount': ('double',
                                  'Pegged-to-benchmark orders: amount by '
                                  "which the order's pegged price should "
                                  'move.'),
           'PercentOffset': ('double',
                             'The percent offset amount for relative '
                             'orders.'),
           'PermId': ('int', 'The Host order identifier.'),
           'RandomizePrice': ('bool', 'DOC_TODO'),
           'RandomizeSize': ('bool', 'DOC_TODO'),
           'ReferenceChangeAmount': ('double',
                                     'Pegged-to-benchmark orders: the '
                                     'amount the reference contract needs '
                                     'to move to adjust the pegged order.'),
           'ReferenceContractId': ('int',
                                   'Pegged-to-benchmark orders: this '
                                   'attribute will contain the conId of '
                                   'the contract against which the order '
                                   'will be pegged.'),
           'ReferenceExchange': ('string',
                                 'Pegged-to-benchmark orders: the exchange '
                                 'against which we want to observe the '
                                 'reference contract.'),
           'ReferencePriceType': ('int',
                                  'Specifies how you want TWS to calculate '
                                  'the limit price for options, and for '
                                  'stock range price monitoring. VOL '
                                  'orders only. Valid values include: \n'
                                  ' 1 - Average of NBBO \n'
                                  ' 2 - NBB or the NBO depending on the '
                                  'action and right. \n'
                                  '.'),
           'Rule80A': ('string',
                       "Individual = 'I'\n"
                       " Agency = 'A'\n"
                       " AgentOtherMember = 'W'\n"
                       " IndividualPTIA = 'J'\n"
                       " AgencyPTIA = 'U'\n"
                       " AgentOtherMemberPTIA = 'M'\n"
                       " IndividualPT = 'K'\n"
                       " AgencyPT = 'Y'\n"
                       " AgentOtherMemberPT = 'N'"),
           'ScaleAutoReset': ('bool', 'DOC_TODO For extended scale orders.'),
           'ScaleInitFillQty': ('int', 'DOC_TODO For extended scale orders.'),
           'ScaleInitLevelSize': ('int',
                                  'Defines the size of the first, or '
                                  'initial, order component. For Scale '
                                  'orders only.'),
           'ScaleInitPosition': ('int',
                                 'DOC_TODO For extended scale orders.'),
           'ScalePriceAdjustInterval': ('int',
                                        'DOC_TODO For extended Scale '
                                        'orders.'),
           'ScalePriceAdjustValue': ('double',
                                     'DOC_TODO For extended Scale orders.'),
           'ScalePriceIncrement': ('double',
                                   'Defines the price increment between '
                                   'scale components. For Scale orders '
                                   'only. This value is compulsory.'),
           'ScaleProfitOffset': ('double',
                                 'DOC_TODO For extended scale orders.'),
           'ScaleRandomPercent': ('bool',
                                  'DOC_TODO For extended scale orders.'),
           'ScaleSubsLevelSize': ('int',
                                  'Defines the order size of the '
                                  'subsequent scale order components. For '
                                  'Scale orders only. Used in conjunction '
                                  'with scaleInitLevelSize().'),
           'ScaleTable': ('string', 'Used for scale orders.'),
           'SettlingFirm': ('string',
                            'DOC_TODO Institutions only. Indicates the '
                            'firm which will settle the trade.'),
           'ShortSaleSlot': ('int',
                             'For institutions only. Valid values are: 1 '
                             '(broker holds shares) or 2 (shares come from '
                             'elsewhere).'),
           'SmartComboRoutingParams': ('List< TagValue >',
                                       'Parameters for combo routing. For '
                                       'more information, refer to '
                                       'https://www.interactivebrokers.com/en/software/api/apiguide/tables/smart_combo_routing.htm.'),
           'Solicited': ('bool', ''),
           'StartingPrice': ('double',
                             "The auction's starting price. For BOX orders "
                             'only.'),
           'StockRangeLower': ('double',
                               'The lower value for the acceptable '
                               'underlying stock price range. For price '
                               'improvement option orders on BOX and VOL '
                               'orders with dynamic management.'),
           'StockRangeUpper': ('double',
                               'The upper value for the acceptable '
                               'underlying stock price range. For price '
                               'improvement option orders on BOX and VOL '
                               'orders with dynamic management.'),
           'StockRefPrice': ('double',
                             "The stock's reference price. The reference "
                             'price is used for VOL orders to compute the '
                             'limit price sent to an exchange (whether or '
                             'not Continuous Update is selected), and for '
                             'price range monitoring.'),
           'SweepToFill': ('bool',
                           'If set to true, specifies that the order is a '
                           'Sweep-to-Fill order.'),
           'Tif': ('string',
                   'The time in force. Valid values are: \n'
                   ' DAY - Valid for the day only.\n'
                   ' GTC - Good until canceled. The order will continue to '
                   'work within the system and in the marketplace until it '
                   'executes or is canceled. GTC orders will be '
                   'automatically be cancelled under the following '
                   'conditions:  If a corporate action on a security '
                   'results in a stock split (forward or reverse), '
                   'exchange for shares, or distribution of shares.  If '
                   'you do not log into your IB account for 90 days.\n'
                   '  At the end of the calendar quarter following the '
                   'current quarter. For example, an order placed during '
                   'the third quarter of 2011 will be canceled at the end '
                   'of the first quarter of 2012. If the last day is a '
                   'non-trading day, the cancellation will occur at the '
                   'close of the final trading day of that quarter. For '
                   'example, if the last day of the quarter is Sunday, the '
                   'orders will be cancelled on the preceding Friday.\n'
                   '  Orders that are modified will be assigned a new '
                   '“Auto Expire” date consistent with the end of the '
                   'calendar quarter following the current quarter.\n'
                   '  Orders submitted to IB that remain in force for more '
                   'than one day will not be reduced for dividends. To '
                   'allow adjustment to your order price on ex-dividend '
                   'date, consider using a Good-Til-Date/Time (GTD) or '
                   'Good-after-Time/Date (GAT) order type, or a '
                   'combination of the two.\n'
                   ' IOC - Immediate or Cancel. Any portion that is not '
                   'filled as soon as it becomes available in the market '
                   'is canceled.\n'
                   ' GTD. - Good until Date. It will remain working within '
                   'the system and in the marketplace until it executes or '
                   'until the close of the market on the date specified\n'
                   ' OPG - Use OPG to send a market-on-open (MOO) or '
                   'limit-on-open (LOO) order.\n'
                   ' FOK - If the entire Fill-or-Kill order does not '
                   'execute as soon as it becomes available, the entire '
                   'order is canceled.\n'
                   ' DTC - Day until Canceled \n'
                   '.'),
           'TotalQuantity': ('double',
                             'The number of positions being bought/sold.'),
           'TrailStopPrice': ('double',
                              'Trail stop price for TRAILIMIT orders.'),
           'TrailingPercent': ('double',
                               'Specifies the trailing amount of a '
                               'trailing stop order as a percentage. '
                               'Observe the following guidelines when '
                               'using the trailingPercent field: .'),
           'Transmit': ('bool',
                        'Specifies whether the order will be transmitted '
                        'by TWS. If set to false, the order will be '
                        'created at TWS but will not be sent.'),
           'TriggerMethod': ('int',
                             'Specifies how Simulated Stop, Stop-Limit and '
                             'Trailing Stop orders are triggered. Valid '
                             'values are:\n'
                             ' 0 - The default value. The "double bid/ask" '
                             'function will be used for orders for OTC '
                             'stocks and US options. All other orders will '
                             'used the "last" function.\n'
                             ' 1 - use "double bid/ask" function, where '
                             'stop orders are triggered based on two '
                             'consecutive bid or ask prices.\n'
                             ' 2 - "last" function, where stop orders are '
                             'triggered based on the last price.\n'
                             ' 3 double last function.\n'
                             ' 4 bid/ask function.\n'
                             ' 7 last or bid/ask function.\n'
                             ' 8 mid-point function.\n'
                             '.'),
           'TriggerPrice': ('double', 'DOC_TODO'),
           'Volatility': ('double',
                          'The option price in volatility, as calculated '
                          "by TWS' Option Analytics. This value is "
                          'expressed as a percent and is used to calculate '
                          'the limit price sent to the exchange.'),
           'VolatilityType': ('int',
                              'Values include:\n'
                              ' 1 - Daily Volatility 2 - Annual Volatility.'),
           'WhatIf': ('bool',
                      'Allows to retrieve the commissions and margin '
                      'information. When placing an order with this '
                      'attribute set to true, the order will not be placed '
                      'as such. Instead it will used to request the '
                      'commissions and margin information that would '
                      'result from this order.')},
 'OrderComboLeg': {'Price': ('double', "The order's leg's price.")},
 'OrderState': {'Commission': ('double', "The order's generated commission."),
                'CommissionCurrency': ('string',
                                       'The generated commission currency.'),
                'EquityWithLoan': ('string',
                                   'Shows the impact the order would have '
                                   "on the account's equity with loan."),
                'InitMargin': ('string',
                               "The order's impact on the account's "
                               'initial margin.'),
                'MaintMargin': ('string',
                                "The order's impact on the account's "
                                'maintenance margin.'),
                'MaxCommission': ('double',
                                  'The executions maximum commission.'),
                'MinCommission': ('double',
                                  "The execution's minimum commission."),
                'Status': ('string', "The order's current status."),
                'WarningText': ('string',
                                'If the order is warranted, a descriptive '
                                'message will be provided.')},
 'ScannerSubscription': {'AbovePrice': ('double',
                                        'Filters out Contracts which price '
                                        'is below this value.'),
                         'AboveVolume': ('int',
                                         'Filters out Contracts which '
                                         'volume is above this value.'),
                         'AverageOptionVolumeAbove': ('int',
                                                      'Filters out '
                                                      'Contracts which '
                                                      'option volume is '
                                                      'above this value.'),
                         'BelowPrice': ('double',
                                        'Filters out contracts which price '
                                        'is above this value.'),
                         'CouponRateAbove': ('double',
                                             'Filter out Contracts with a '
                                             'coupon rate lower than this '
                                             'value.'),
                         'CouponRateBelow': ('double',
                                             'Filter out Contracts with a '
                                             'coupon rate higher than this '
                                             'value.'),
                         'ExcludeConvertible': ('string',
                                                'Filters out Convertible '
                                                'bonds.'),
                         'Instrument': ('string',
                                        "The instrument's type for the "
                                        'scan. I.e. STK, FUT.HK, etc.'),
                         'LocationCode': ('string',
                                          "The request's location (STK.US, "
                                          'STK.US.MAJOR, etc).'),
                         'MarketCapAbove': ('double',
                                            'Filters out Contracts which '
                                            'market cap is above this '
                                            'value.'),
                         'MarketCapBelow': ('double',
                                            'Filters out Contracts which '
                                            'market cap is below this '
                                            'value.'),
                         'MaturityDateAbove': ('string',
                                               'Filter out Contracts with '
                                               'a maturity date earlier '
                                               'than this value.'),
                         'MaturityDateBelow': ('string',
                                               'Filter out Contracts with '
                                               'a maturity date older than '
                                               'this value.'),
                         'MoodyRatingAbove': ('string',
                                              'Filters out Contracts which '
                                              "Moody's rating is below "
                                              'this value.'),
                         'MoodyRatingBelow': ('string',
                                              'Filters out Contracts which '
                                              "Moody's rating is above "
                                              'this value.'),
                         'NumberOfRows': ('int',
                                          'The number of rows to be '
                                          'returned for the query.'),
                         'ScanCode': ('string',
                                      "Same as TWS Market Scanner's "
                                      '"parameters" field, for example: '
                                      'TOP_PERC_GAIN.'),
                         'ScannerSettingPairs': ('string',
                                                 'For example, a pairing '
                                                 '"Annual, true" used on '
                                                 'the "top Option Implied '
                                                 'Vol % Gainers" scan '
                                                 'would return annualized '
                                                 'volatilities.'),
                         'SpRatingAbove': ('string',
                                           'Filters out Contracts with a '
                                           'S&P rating below this value.'),
                         'SpRatingBelow': ('string',
                                           'Filters out Contracts with a '
                                           'S&P rating above this value.'),
                         'StockTypeFilter': ('string',
                                             'CORP = Corporation ADR = '
                                             'American Depositary Receipt '
                                             'ETF = Exchange Traded Fund '
                                             'REIT = Real Estate '
                                             'Investment Trust CEF = '
                                             'Closed End Fund')},
 'UnderComp': {'ConId': ('int',
                         'The unique contract identifier specifying the '
                         'security. Used for Delta-Neutral Combo contracts.'),
               'Delta': ('double',
                         'The underlying stock or future delta. Used for '
                         'Delta-Neutral Combo contracts.'),
               'Price': ('double',
                         'The price of the underlying. Used for '
                         'Delta-Neutral Combo contracts.')}}
