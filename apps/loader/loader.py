import time
import json
import logging
import websocket

from apps.redis import scripts
from docs.config import INTERESTED_PAIRS, UPDATE_TIMEOUT


def on_message(ws, message, data={}):
    for pair in json.loads(message):
        if pair.get('s') in INTERESTED_PAIRS:
            data[pair['s']] = pair.get('c')

    if int(time.time()) % UPDATE_TIMEOUT == 0:
        try:
            scripts.update_rates_from_redis(data)
        except Exception as exc:
            logging.error(f'Unsuccessful attempt to save to redis. Error {str(exc)}')


def on_error(ws, error):
    logging.error(error)

def on_close(ws, close_status_code, close_msg):
    logging.info("### closed ###")

def on_open(ws):
    logging.info("Opened connection")

def get_stream(site_url: str):
    # websocket.enableTrace(True)
    data = {}
    client_websocket = websocket.WebSocketApp(
        site_url,
        on_open=on_open,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close
    )
    client_websocket.run_forever()
