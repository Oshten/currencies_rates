import os
import sys
import logging

from starlette.config import Config

# -- Project information -----------------------------------------------------

project = "Exchange rates"
author = "Oshten"

# -- Configuration settings -----------------------------------------------------

ROOT_DIR_NAME = os.path.abspath('..')
sys.path.insert(0, ROOT_DIR_NAME)
config = Config(f'{ROOT_DIR_NAME}/.env')

LEVEL_LOGGING = logging.DEBUG
LOGS_FILE = f'currencies_rates.log'


#Configuration redis
REDIS_HOST = 'redis'
REDIS_PORT = 6379
REDIS_PASSWORD = config('REDIS_PASSWORD', cast=str, default='12345')


SITE_URLS_WITH_RATES = [

    'wss://stream.binance.com:9443/ws/!ticker@arr',
]

UPDATE_TIMEOUT = 5 # Timeout for update rates for database
INTERESTED_PAIRS = [
    'BTCKZT',
    'BTCGEL',
    'BTCEUR',
    'BTCBRL',
    'ETHBTC',
    'ETHRUB',
    'ETHUSDT',
    'USDTTRCEUR',
    'USDTTRCKZT',
    'USDTTRCGEL]',
    'USDTERCRUB',
    'USDTERCUSD',
    'USDTBRL'
]



