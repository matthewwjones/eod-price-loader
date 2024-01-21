import logging

from config.instrumentcodeloader import InstrumentCodeLoader
from load.eodloader import EodLoader


class App:

    def __init__(self):
        self.log = logging.getLogger(__name__)
        self.instrument_codes_file = 'instrument-codes.txt'

    def run(self):
        self.log.info("Starting EOD price loader app...")
        instrument_code_loader = InstrumentCodeLoader(self.instrument_codes_file)
        instrument_codes = instrument_code_loader.load_instrument_codes()
        eod_loader = EodLoader(instrument_codes)
        eod_loader.load_prices()
