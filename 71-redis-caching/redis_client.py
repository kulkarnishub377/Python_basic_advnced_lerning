import json
import redis
from config import REDIS_URL, CACHE_TTL_SECONDS

try:
    pool = redis.ConnectionPool.from_url(REDIS_URL, decode_responses=True)
    r = redis.Redis(connection_pool=pool)
    r.ping()
    REDIS_AVAILABLE = True
except redis.ConnectionError:
    r = None
    REDIS_AVAILABLE = False


def get_cache(key: str):
    """Retrieve a value from Redis cache. Returns None on miss."""
    if not REDIS_AVAILABLE:
        return None
    raw = r.get(key)
    if raw is None:
        return None
    return json.loads(raw)


def set_cache(key: str, value, ttl: int = CACHE_TTL_SECONDS):
    """Store a value in Redis with a TTL."""
    if not REDIS_AVAILABLE:
        return
    r.setex(key, ttl, json.dumps(value))


def invalidate_cache(pattern: str):
    """Delete all keys matching a given pattern (cache invalidation)."""
    if not REDIS_AVAILABLE:
        return 0
    keys = r.keys(pattern)
    if keys:
        return r.delete(*keys)
    return 0
