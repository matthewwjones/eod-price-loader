import logging

from config.apiconfigloader import ApiConfigLoader
from config.instrumentcodeloader import InstrumentCodeLoader
from load.eodloader import EodLoader


class App:

    def __init__(self):
        self.log = logging.getLogger(__name__)
        self.instrument_codes_file = '../instrument-codes.txt'
        self.api_config_file = '../api-config.txt'

    def run(self):
        self.log.info("Starting EOD price loader app...")
        instrument_code_loader = InstrumentCodeLoader(self.instrument_codes_file)
        instrument_codes = instrument_code_loader.load_instrument_codes()
        api_token = ApiConfigLoader(self.api_config_file).load_api_config()
        eod_loader = EodLoader(api_token, instrument_codes)
        eod_loader.load_prices()
