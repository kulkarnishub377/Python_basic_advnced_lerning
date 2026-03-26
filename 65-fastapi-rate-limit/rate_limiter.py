import time
import redis
from fastapi import Request, HTTPException
import os

# Connect to Redis. In production use async redis (e.g., redis.asyncio)
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/2")
redis_client = redis.Redis.from_url(REDIS_URL, decode_responses=True)

# Configuration
RATE_LIMIT_REQUESTS = 5      # Maximum requests
RATE_LIMIT_WINDOW = 10       # Per X seconds

def rate_limit(request: Request):
    """
    FastAPI dependency that enforces rate limiting per IP address
    using a Redis Sorted Set (ZSET) to implement a Sliding Window.
    """
    client_ip = request.client.host
    redis_key = f"rate_limit:{client_ip}"
    
    current_time = time.time()
    
    # Start a Redis transaction pipeline to ensure atomicity
    pipeline = redis_client.pipeline()
    
    try:
        # 1. Remove all old requests outside the current time window
        window_start = current_time - RATE_LIMIT_WINDOW
        pipeline.zremrangebyscore(redis_key, 0, window_start)
        
        # 2. Count how many requests are currently in the window
        pipeline.zcard(redis_key)
        
        # 3. Add the new request timestamp
        pipeline.zadd(redis_key, {str(current_time): current_time})
        
        # 4. Set expiry on the key so it cleans itself up if unused
        pipeline.expire(redis_key, RATE_LIMIT_WINDOW)
        
        # Execute pipeline
        results = pipeline.execute()
        
        # results[1] is the result of zcard (the number of current requests)
        request_count = results[1]
        
        if request_count >= RATE_LIMIT_REQUESTS:
            # Revert the current addition if blocked
            redis_client.zrem(redis_key, str(current_time))
            raise HTTPException(
                status_code=429, 
                detail="Too Many Requests. Please wait before trying again."
            )
            
    except redis.RedisError as e:
        # If Redis is down, we allow the request to pass to avoid breaking the application
        print(f"Redis error: {e}")
        pass
    
    return True
