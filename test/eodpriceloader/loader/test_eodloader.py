from unittest import TestCase

from loader.eodloader import EodLoader


class TestEodLoader(TestCase):
    json = '[{"date":"2023-10-31","open":169.35,"high":170.9,"low":167.9,"close":170.77,"adjusted_close":170.77,' \
           '"volume":44846000}] '

    def test_extract_close_from_response_returns_expected_value(self):
        loader = EodLoader([])
        close_price = loader.extract_close_from_response(self.json)
        self.assertEqual(close_price, 170.77)
