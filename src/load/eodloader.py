import json
import logging

import requests


class EodLoader:

    def __init__(self, api_token, instrument_codes):
        self.log = logging.getLogger(__name__)
        self.api_token = api_token
        self.instrument_codes = instrument_codes
        self.log.info("Created EOD price loader.")

    def load_prices(self):
        self.log.info(f"Loading prices for {len(self.instrument_codes)} instrument codes.")
        eod_prices = {}
        for instrument in self.instrument_codes:
            eod_prices[instrument] = self.load_eod_for_instrument(instrument)
        self.log.info(f'Prices: {eod_prices}')

    def load_eod_for_instrument(self, instrument):
        url = 'https://eodhd.com/api/eod/%s?api_token=%s&order=d&fmt=json&from=2023-11-30&to=2023-11-30' % (
            instrument, self.api_token)
        self.log.info(f'Loading EOD price for {instrument} from {url}')
        try:
            response = requests.get(url).json()
            self.log.info(f"Fetched {response}")
            return self.extract_close_from_response(response)
        except Exception as e:
            self.log.exception(f'Error loading price for instrument {instrument} - {e}')

    @staticmethod
    def extract_close_from_response(response):
        return response[0]['close']
