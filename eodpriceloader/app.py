import logging

from eodpriceloader.loader.eodloader import EodLoader


class App:

    def __init__(self):
        self.current_number = 0
        self.log = logging.getLogger(__name__)

    def run(self):
        self.log.info("Starting EOD price loader app...")
        instrument_codes = []
        eod_loader = EodLoader(instrument_codes)
        eod_loader.load_prices()
