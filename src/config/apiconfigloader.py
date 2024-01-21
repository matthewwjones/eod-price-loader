import logging


class ApiConfigLoader:

    def __init__(self, api_config_file):
        self.log = logging.getLogger(__name__)
        self.api_config_file = api_config_file

    def load_api_config(self):
        self.log.info(f"Loading API config from {self.api_config_file}...")
        try:
            with open(self.api_config_file) as file:
                for line in file:
                    if line.startswith('api_token='):
                        return line.rstrip('api_token=')
        except FileNotFoundError as e:
            raise Exception(f"API config file {self.api_config_file} does not exist.", e)
