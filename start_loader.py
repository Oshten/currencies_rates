import logging

from apps.loader.loader import get_stream
from apps.logging.logger import handler
from docs.config import SITE_URLS_WITH_RATES, LEVEL_LOGGING

logging.basicConfig(handlers=[handler], level=LEVEL_LOGGING)

if __name__ == '__main__':
    while True:
        for site_url in SITE_URLS_WITH_RATES:
            logging.info(f'Connect to {site_url}')
            try:
                get_stream(site_url)
            except Exception as exc:
                logging.error(exc)
