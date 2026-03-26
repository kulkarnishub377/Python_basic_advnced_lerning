import time
from playwright.async_api import async_playwright
from config import HEADLESS, TIMEOUT_MS, USER_AGENT
from parser import extract_metadata


async def scrape_url(url: str) -> dict:
    """
    Launch a headless Chromium browser, navigate to the URL,
    wait for JavaScript to render, then extract the full DOM.
    """
    start = time.perf_counter()

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=HEADLESS)
        context = await browser.new_context(user_agent=USER_AGENT)
        page = await context.new_page()

        try:
            await page.goto(url, timeout=TIMEOUT_MS, wait_until="networkidle")
        except Exception as e:
            await browser.close()
            return {"error": f"Failed to load page: {str(e)}"}

        # Get the fully rendered HTML (after JS execution)
        html = await page.content()
        await browser.close()

    elapsed = round((time.perf_counter() - start) * 1000, 1)

    metadata = extract_metadata(html)
    metadata["url"] = url
    metadata["load_time_ms"] = elapsed

    return metadata
