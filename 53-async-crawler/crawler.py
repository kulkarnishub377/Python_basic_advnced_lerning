import asyncio
import aiohttp
from bs4 import BeautifulSoup
import time
from urllib.parse import urljoin, urlparse

class AsyncCrawler:
    def __init__(self, base_url, max_concurrent=5, max_depth=2):
        self.base_url = base_url
        self.max_depth = max_depth
        self.visited = set()
        # Semaphore limits how many requests we execute concurrently
        self.semaphore = asyncio.Semaphore(max_concurrent)
        
    def is_valid_url(self, url):
        """Only crawl URLs belonging to the original domain"""
        parsed = urlparse(url)
        base_parsed = urlparse(self.base_url)
        return bool(parsed.netloc) and parsed.netloc == base_parsed.netloc
        
    async def fetch(self, session, url):
        """Downloads the raw HTML utilizing the semaphore limit."""
        async with self.semaphore:
            try:
                # Add tiny delay to be polite
                await asyncio.sleep(0.1)
                async with session.get(url, timeout=10) as response:
                    return await response.text()
            except Exception as e:
                print(f"[Error fetching {url}]: {e}")
                return None

    def extract_links(self, html, current_url):
        """Uses BeautifulSoup to synchronously parse links from the DOM."""
        if not html:
            return []
            
        soup = BeautifulSoup(html, 'html.parser')
        links = set()
        
        for anchor in soup.find_all('a', href=True):
            href = anchor['href']
            # Convert relative URLs to absolute URLs
            absolute_url = urljoin(current_url, href)
            # Remove URL fragments (e.g. index.html#section1)
            absolute_url = absolute_url.split('#')[0]
            
            if self.is_valid_url(absolute_url) and absolute_url not in self.visited:
                links.add(absolute_url)
                
        return list(links)

    async def crawl(self, session, url, depth):
        """Recursive asynchronous crawl function."""
        if depth > self.max_depth or url in self.visited:
            return
            
        self.visited.add(url)
        print(f"Crawling (Depth {depth}): {url}")
        
        html = await self.fetch(session, url)
        links = self.extract_links(html, url)
        
        # Base case
        if not links or depth == self.max_depth:
            return
            
        # Recursive step: fire off concurrently
        tasks = []
        for link in links:
            if link not in self.visited:
                tasks.append(self.crawl(session, link, depth + 1))
                
        await asyncio.gather(*tasks)

async def main():
    target_site = "https://quotes.toscrape.com/"
    print(f"Starting Async Crawler on {target_site}")
    print("-" * 40)
    
    start_time = time.time()
    crawler = AsyncCrawler(target_site, max_concurrent=10, max_depth=2)
    
    # We maintain a single resilient HTTP connection pool Session
    async with aiohttp.ClientSession() as session:
        await crawler.crawl(session, crawler.base_url, 0)
        
    end_time = time.time()
    
    print("-" * 40)
    print(f"Summary:")
    print(f"Unique URLs crawled: {len(crawler.visited)}")
    print(f"Total time elapsed: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    import sys
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
