"""Unit tests for ca_leginfo.py."""

import ca_leginfo

import unittest

class CALegInfoClientTests(unittest.TestCase):
    """TODO: These are currently live tests against the prod API and should be Mocked Out someday."""

    def setUp(self):
        self._client = ca_leginfo.CALegInfoClient(session_id="20232024")

    def test_get_bill_title(self):
        """Tests that get bill author can correctly return an author."""
        got = self._client.get_bill_title(bill_id='AB1939')
        print(got)
        want = "AB-1939 Pupil attendance"
        self.assertIn(want, got)

if __name__ == '__main__':
    unittest.main()