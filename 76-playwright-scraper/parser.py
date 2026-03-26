from bs4 import BeautifulSoup


def extract_metadata(html: str) -> dict:
    """Parse the rendered HTML and extract structured metadata."""
    soup = BeautifulSoup(html, "html.parser")

    title = soup.title.string.strip() if soup.title and soup.title.string else ""

    meta_desc = ""
    meta_tag = soup.find("meta", attrs={"name": "description"})
    if meta_tag and meta_tag.get("content"):
        meta_desc = meta_tag["content"]

    headings = []
    for tag in ["h1", "h2", "h3"]:
        for h in soup.find_all(tag):
            text = h.get_text(strip=True)
            if text:
                headings.append(text)

    links = soup.find_all("a", href=True)

    body_text = soup.get_text(separator=" ", strip=True)
    word_count = len(body_text.split())

    return {
        "title": title,
        "meta_description": meta_desc,
        "headings": headings[:20],
        "links_count": len(links),
        "word_count": word_count,
    }
