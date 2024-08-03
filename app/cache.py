import json
import os

import redis

REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
REDIS_PORT = os.getenv('REDIS_PORT', 6379)

redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)


async def get_cached_item(item_id: int):
    item = redis_client.get(f"item:{item_id}")
    if item:
        return json.loads(item.decode("utf-8"))
    return None


async def cache_item(item_id: int, item: str):
    redis_client.set(f"item:{item_id}", json.dumps(item, default=str), ex=3600)
