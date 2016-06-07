EWRAPPER_DATA = """\
virtual void tickPrice( TickerId tickerId, TickType field, double price, int canAutoExecute) = 0;
virtual void tickSize( TickerId tickerId, TickType field, int size) = 0;
virtual void tickOptionComputation( TickerId tickerId, TickType tickType, double impliedVol, double delta,
   double optPrice, double pvDividend, double gamma, double vega, double theta, double undPrice) = 0;
virtual void tickGeneric(TickerId tickerId, TickType tickType, double value) = 0;
virtual void tickString(TickerId tickerId, TickType tickType, const IBString& value) = 0;
virtual void tickEFP(TickerId tickerId, TickType tickType, double basisPoints, const IBString& formattedBasisPoints,
   double totalDividends, int holdDays, const IBString& futureExpiry, double dividendImpact, double dividendsToExpiry) = 0;
virtual void orderStatus( OrderId orderId, const IBString &status, int filled,
   int remaining, double avgFillPrice, int permId, int parentId,
   double lastFillPrice, int clientId, const IBString& whyHeld) = 0;
virtual void openOrder( OrderId orderId, const Contract&, const Order&, const OrderState&) = 0;
virtual void openOrderEnd() = 0;
virtual void winError( const IBString &str, int lastError) = 0;
virtual void connectionClosed() = 0;
virtual void updateAccountValue(const IBString& key, const IBString& val,
const IBString& currency, const IBString& accountName) = 0;
virtual void updatePortfolio( const Contract& contract, int position,
  double marketPrice, double marketValue, double averageCost,
  double unrealizedPNL, double realizedPNL, const IBString& accountName) = 0;
virtual void updateAccountTime(const IBString& timeStamp) = 0;
virtual void accountDownloadEnd(const IBString& accountName) = 0;
virtual void nextValidId( OrderId orderId) = 0;
virtual void contractDetails( int reqId, const ContractDetails& contractDetails) = 0;
virtual void bondContractDetails( int reqId, const ContractDetails& contractDetails) = 0;
virtual void contractDetailsEnd( int reqId) = 0;
virtual void execDetails( int reqId, const Contract& contract, const Execution& execution) =0;
virtual void execDetailsEnd( int reqId) =0;
virtual void error(const int id, const int errorCode, const IBString errorMsg) = 0;
virtual void updateMktDepth(TickerId id, int position, int operation, int side,
  double price, int size) = 0;
virtual void updateMktDepthL2(TickerId id, int position, IBString marketMaker, int operation,
  int side, double price, int size) = 0;
virtual void updateNewsBulletin(int msgId, int msgType, const IBString& newsMessage, const IBString& originExch) = 0;
virtual void managedAccounts( const IBString& accountsList) = 0;
virtual void receiveFA(faDataType pFaDataType, const IBString& cxml) = 0;
virtual void historicalData(TickerId reqId, const IBString& date, double open, double high, 
   double low, double close, int volume, int barCount, double WAP, int hasGaps) = 0;
virtual void scannerParameters(const IBString &xml) = 0;
virtual void scannerData(int reqId, int rank, const ContractDetails &contractDetails,
   const IBString &distance, const IBString &benchmark, const IBString &projection,
   const IBString &legsStr) = 0;
virtual void scannerDataEnd(int reqId) = 0;
virtual void realtimeBar(TickerId reqId, long time, double open, double high, double low, double close,
   long volume, double wap, int count) = 0;
virtual void currentTime(long time) = 0;
virtual void fundamentalData(TickerId reqId, const IBString& data) = 0;
virtual void deltaNeutralValidation(int reqId, const UnderComp& underComp) = 0;
virtual void tickSnapshotEnd( int reqId) = 0;
virtual void marketDataType( TickerId reqId, int marketDataType) = 0;
virtual void commissionReport( const CommissionReport &commissionReport) = 0;
virtual void position( const IBString& account, const Contract& contract, int position, double avgCost) = 0;
virtual void positionEnd() = 0;
virtual void accountSummary( int reqId, const IBString& account, const IBString& tag, const IBString& value, const IBString& curency) = 0;
virtual void accountSummaryEnd( int reqId) = 0;
virtual void verifyMessageAPI( const IBString& apiData) = 0;
virtual void verifyCompleted( bool isSuccessful, const IBString& errorText) = 0;
virtual void displayGroupList( int reqId, const IBString& groups) = 0;
virtual void displayGroupUpdated( int reqId, const IBString& contractInfo) = 0;"""
