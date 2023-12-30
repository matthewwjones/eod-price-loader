import logging

from app import App

if __name__ == "__main__":
    try:
        App().run()
    except Exception as e:
        logging.info("Error running eod-price-loader.", e)
