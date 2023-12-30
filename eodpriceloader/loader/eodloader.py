import logging


class EodLoader:

    def __init__(self, instrument_codes):
        self.log = logging.getLogger(__name__)
        self.instrument_codes = instrument_codes
        self.log.info("Created EOD price loader.")

    def load_prices(self):
        self.log.info(f"Loading prices for {len(self.instrument_codes)} instrument codes.")
