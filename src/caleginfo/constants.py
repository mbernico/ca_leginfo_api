"""Settings and configuration for the API."""

BILL_BASE_URL = "https://leginfo.legislature.ca.gov/faces/"
BILL_QUERY = "?bill_id="
BILL_SEARCH_ALL_QUERY = "?author=All&lawCode=All&house=Both&session_year="

BILL_ANALYSIS_PAGE = "billAnalysisClient.xhtml"
BILL_HISTORY_PAGE = "billHistoryClient.xhtml"
BILL_NAV_PAGE = "billNavClient.xhtml"
BILL_TEXT_PAGE = "billTextClient.xhtml"
BILL_STATUS_PAGE = "billStatusClient.xhtml"
BILL_SEARCH_PAGE = "billSearchClient.xhtml"

BILL_HISTORY_QUERY = BILL_BASE_URL + BILL_HISTORY_PAGE + BILL_QUERY
BILL_TEXT_QUERY= BILL_BASE_URL + BILL_TEXT_PAGE + BILL_QUERY
BILL_ANALYSIS_QUERY = BILL_BASE_URL + BILL_ANALYSIS_PAGE + BILL_QUERY
BILL_NAV_QUERY = BILL_BASE_URL + BILL_NAV_PAGE + BILL_QUERY
BILL_STATUS_QUERY = BILL_BASE_URL + BILL_STATUS_PAGE + BILL_QUERY
BILL_SEARCH_QUERY = BILL_BASE_URL + BILL_SEARCH_PAGE + BILL_SEARCH_ALL_QUERY

HEADERS = {
    'Accept-Language' : 'en-US,en;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'
}