"""Settings and configuration for the API."""

BILL_BASE_URL = "https://leginfo.legislature.ca.gov/faces/"
BILL_QUERY = "?bill_id="

BILL_ANALYSIS_PAGE = "billAnalysisClient.xhtml"
BILL_HISTORY_PAGE = "billHistoryClient.xhtml"
BILL_NAV_PAGE = "billNavClient.xhtml"
BILL_TEXT_PAGE = "billTextClient.xhtml"


BILL_HISTORY_QUERY = BILL_BASE_URL + BILL_HISTORY_PAGE + BILL_QUERY
BILL_TEXT_QUERY= BILL_BASE_URL + BILL_TEXT_PAGE + BILL_QUERY
BILL_ANALYSIS_QUERY = BILL_BASE_URL + BILL_ANALYSIS_PAGE + BILL_QUERY
BILL_NAV_QUERY = BILL_BASE_URL + BILL_NAV_PAGE + BILL_QUERY
