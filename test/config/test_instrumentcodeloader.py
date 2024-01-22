from unittest import TestCase

from src.config.instrumentcodeloader import InstrumentCodeLoader


class TestInstrumentCodeLoader(TestCase):
    test_instrument_codes_file = '../test/config/test-data/test-instrument-codes.txt'
    empty_instrument_codes_file = '../test/config/test-data/empty-instrument-codes-file.txt'

    def test_load_instrument_codes_returns_expected_list(self):
        loader = InstrumentCodeLoader(self.test_instrument_codes_file)
        self.assertEqual(loader.load_instrument_codes(), ['HSBA.LSE', 'OCDO.LSE', 'VOD.LSE'])

    def test_load_instrument_codes_empty_file(self):
        loader = InstrumentCodeLoader(self.empty_instrument_codes_file)
        self.assertEqual(loader.load_instrument_codes(), [])

    def test_load_instrument_codes_raises_exception_for_invalid_path(self):
        with self.assertRaises(Exception) as context:
            InstrumentCodeLoader('invalid-path').load_instrument_codes()
        self.assertIn('File invalid-path does not exist.', str(context.exception))
