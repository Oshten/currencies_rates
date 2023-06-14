import redis
import logging

from docs.config import REDIS_HOST, REDIS_PORT, REDIS_PASSWORD

class RedisConnect:

    def __init__(self):
        self.connect = redis.StrictRedis(
            host=REDIS_HOST,
            port=REDIS_PORT,
            password=REDIS_PASSWORD,
            charset="utf-8",
            decode_responses=True
        )

    def __enter__(self):
        return self.connect

    def __exit__(self, type, value, traceback):
        return self.connect.close

    