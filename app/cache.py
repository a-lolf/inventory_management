import os
import redis

# redis = aioredis.from_url("redis://localhost")

REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
REDIS_PORT = os.getenv('REDIS_PORT', '6379')

redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)


async def get_cached_item(item_id: int):
    item = await redis_client.get(f"item:{item_id}")
    if item:
        return item.decode("utf-8")
    return None


async def cache_item(item_id: int, item: str):
    await redis_client.set(f"item:{item_id}", item, ex=3600)
