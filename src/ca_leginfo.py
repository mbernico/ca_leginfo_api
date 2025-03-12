"""CA Leginfo API."""

import requests
from bs4 import BeautifulSoup
import logging

import constants

logging.basicConfig(level=logging.DEBUG)

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
