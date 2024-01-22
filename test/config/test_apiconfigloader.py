from unittest import TestCase

from src.config.apiconfigloader import ApiConfigLoader


class TestApiConfigLoader(TestCase):
    test_api_config_file = 'test/config/test-data/test-api-config.txt'

    def test_load_api_config_returns_expected_key(self):
        loader = ApiConfigLoader(self.test_api_config_file)
        self.assertEqual('api-key', loader.load_api_config())
