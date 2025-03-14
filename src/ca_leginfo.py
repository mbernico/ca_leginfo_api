"""CA Leginfo API."""

import dataclasses
import requests
from bs4 import BeautifulSoup
import logging

import constants

logging.basicConfig(level=logging.DEBUG)

@dataclasses.dataclass
class BillStatus:
   lead_author: str = None
   topic: str = None
   house_location: str = None
   last_amended: str = None
   committee_location: str = None
   history: list = dataclasses.field(default_factory=list)

def _get_bill_identifier(session_id: str, bill_id: str ) -> str:
  """Formats the session id and bill id so that it can be queried."""
  return  session_id + "0" + bill_id

class CALegInfoClient:
  """Client for interacting with CA Leginfo."""

  def __init__(self, session_id: str):
    """Initializes CALegInfoClient.
    
    Args:
    session_id: A string that identifies the legislative session to
        interact with (e.g. 20252026 for the 2025-2026 Legislative session).
    """
    self._session_id = session_id

  def get_bill_title(self, bill_id: str):
    """
    Scrapes the title of a bill from a given bill ID and session ID.

    Args:
        bill_id: The bill ID.

    Returns:
        The bill title as a string, or None if not found.
    """
    bill_text_url = constants.BILL_TEXT_QUERY + _get_bill_identifier(self._session_id, bill_id)
    logging.debug(bill_text_url)

    try:
        response = requests.get(bill_text_url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        soup = BeautifulSoup(response.content, "html.parser")
        title_element = soup.select_one("#bill_header h1") # more robust selector.
        logging.debug(f"Title element parsed: {title_element}")

        if title_element:
            return title_element.text.strip()
        else:
            return None

    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching URL: {e}")
        return None
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return None
    
  def get_bill_status(self, bill_id:str) -> BillStatus:
    """Returns author info, topic, last amended date, and history."""
    bill_status_url = constants.BILL_STATUS_QUERY + _get_bill_identifier(self._session_id, bill_id)
    logging.debug(bill_status_url)

    status = BillStatus()

    try:
      response = requests.get(bill_status_url)
      response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
      # Inspect https://leginfo.legislature.ca.gov/faces/billStatusClient.xhtml?bill_id=202320240AB2071
      # For details if this breaks.
      soup = BeautifulSoup(response.content, "html.parser")
      lead_author = soup.find(id="leadAuthors")
      topic = soup.select_one(".statusCellData #subject")
      house_location = soup.find(id="houseLoc")
      last_amended = soup.select_one(".statusCellData #lastAction")
      committee_location = soup.select_one(".statusCellData #latest_commitee_location")
      bill_history = soup.find(id="billhistory")

      if lead_author:
         status.lead_author = lead_author.text.strip()
      if topic:
         status.topic = topic.text.strip()
      if house_location:
         status.house_location = house_location.text.strip()
      if last_amended:
         status.last_amended = last_amended.text.strip()
      if committee_location:
         status.committee_location = committee_location.text.strip()
      if bill_history:
         tbody = bill_history.find('tbody')
         history_rows = tbody.find_all('tr')
         for row in history_rows:
            cells = row.find_all('td')
            row_dict = {'date': cells[0].text.strip(), 'action': cells[1].text.strip()}
            status.history.append(row_dict)
    
      return status

    except requests.exceptions.RequestException as e:
      logging.error(f"Error fetching URL: {e}")
      return None
    except Exception as e:
      logging.error(f"An unexpected error occurred: {e}")
      return None

