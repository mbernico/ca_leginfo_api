"""Unit tests for ca_leginfo.py."""

import ca_leginfo

import unittest

class CALegInfoClientTests(unittest.TestCase):
    """Integration tests for CALegInfoClient.
    
    These are "live" integration tests.  
    
    By design they use the live API and will fail if the upstream website
      gets changed.
    """

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