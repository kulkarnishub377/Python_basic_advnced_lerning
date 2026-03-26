import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd

st.set_page_config(page_title="Web Scraper Dashboard", page_icon="WEB")

st.title("Web Article Scraper")
st.markdown("Enter a URL to scrape its headers and build a structural dataframe.")

url_input = st.text_input("Target URL:", "https://en.wikipedia.org/wiki/Web_scraping")

@st.cache_data(show_spinner="Fetching and parsing HTML...")
def scrape_data(url):
    try:
        # Emulate a real browser to avoid basic blocks
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Extract the page title
        title = soup.title.string if soup.title else "No Title Found"
        
        # Extract all headings (h1, h2, h3)
        headings = []
        for tag in soup.find_all(['h1', 'h2', 'h3']):
            headings.append({
                "Level": tag.name.upper(),
                "Text": tag.get_text(strip=True)
            })
            
        # Extract links
        links_count = len(soup.find_all('a'))
        
        # Convert headings to a Pandas DataFrame
        df = pd.DataFrame(headings)
        
        return {
            "success": True,
            "title": title,
            "links_count": links_count,
            "df": df
        }
        
    except requests.RequestException as e:
        return {"success": False, "error": f"Network Error: {e}"}
    except Exception as e:
        return {"success": False, "error": f"Parsing Error: {e}"}

if st.button("Scrape Data"):
    if url_input:
        results = scrape_data(url_input)
        
        if results["success"]:
            st.success(f"Successfully scraped **{results['title']}**")
            
            col1, col2 = st.columns(2)
            col1.metric("Total Headings Found", len(results["df"]))
            col2.metric("Total Links Found", results["links_count"])
            
            st.subheader("Heading Structure Documented")
            st.dataframe(results["df"], use_container_width=True)
            
            # Simple CSV Export feature
            csv = results["df"].to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Download as CSV",
                data=csv,
                file_name="scraped_headers.csv",
                mime="text/csv",
            )
        else:
            st.error(results["error"])
    else:
        st.warning("Please enter a valid URL.")
