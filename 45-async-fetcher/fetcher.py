import asyncio
import aiohttp
import time

async def fetch_data(session, url):
    """
    An asynchronous coroutine that fetches JSON data from a specific API endpoint.
    When network I/O hits `await`, the event loop is instantly yielded back to other tasks.
    """
    start = time.time()
    try:
        # Await pauses this function and lets asyncio run other tasks
        async with session.get(url) as response:
            response.raise_for_status()
            data = await response.json()
            elapsed = time.time() - start
            print(f"[Async] Fetched {len(data)} items from {url} in {elapsed:.3f}s")
            return url, data
    except Exception as e:
        print(f"[Async] Failed fetching {url}: {e}")
        return url, None

async def main():
    endpoints = [
        "https://jsonplaceholder.typicode.com/posts",
        "https://jsonplaceholder.typicode.com/comments",
        "https://jsonplaceholder.typicode.com/albums",
        "https://jsonplaceholder.typicode.com/photos",
        "https://jsonplaceholder.typicode.com/todos",
        "https://jsonplaceholder.typicode.com/users"
    ]
    
    print("Starting asyncio Event Loop...")
    start_time = time.time()
    
    # We use a single ClientSession for connection pooling
    async with aiohttp.ClientSession() as session:
        # Create a list of awaitable tasks
        tasks = []
        for url in endpoints:
            task = asyncio.create_task(fetch_data(session, url))
            tasks.append(task)
            
        # Run them all concurrently
        results = await asyncio.gather(*tasks)
        
    end_time = time.time()
    total_time = end_time - start_time
    
    print(f"\nAsyncio gathering completed in {total_time:.4f} seconds!")
    print(f"Total endpoints processed: {len(results)}")

if __name__ == "__main__":
    # In older Python versions we use asyncio.get_event_loop().run_until_complete()
    # But in modern Python (3.7+), asyncio.run is the standard entry point.
    
    # Windows specific fix for ProactorEventLoop closing error silently:
    import sys
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        
    asyncio.run(main())
