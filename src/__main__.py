import logging

from app import App

logging.basicConfig(level='INFO', format='%(asctime)s [%(levelname)s] %(name)s -- %(message)s',
                    handlers=[logging.StreamHandler()])

if __name__ == "__main__":
    try:
        App().run()
    except Exception as e:
        logging.error(f"Error occurred whilst running app. {e}",)
