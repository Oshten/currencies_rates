from apps.redis.connect import RedisConnect

def update_rates_from_redis(data: dict):
    with RedisConnect() as r:
        r.mset(data)

def get_rates_from_redis(pair=None):
    with RedisConnect() as r:
        if pair:
            value = r.get(pair)
            return {pair: value}
        all_keys = r.keys()
        all_values = r.mget(all_keys)
        return {k: v for k, v in zip(all_keys, all_values)}