from unittest import TestCase

from config.instrumentcodeloader import InstrumentCodeLoader


class TestInstrumentCodeLoader(TestCase):
    test_instrument_codes_file = 'test/config/test-data/test-instrument-codes.txt'

    def test_load_instrument_codes_returns_expected_list(self):
        loader = InstrumentCodeLoader(self.test_instrument_codes_file)
        self.assertEqual(loader.load_instrument_codes(), ['HSBA.LSE', 'OCDO.LSE', 'VOD.LSE'])
