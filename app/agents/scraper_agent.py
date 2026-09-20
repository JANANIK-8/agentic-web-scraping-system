
import requests
from bs4 import BeautifulSoup


def scrape_website(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(
        url,
        headers=headers,
        timeout=10
    )

    response.raise_for_status()

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    title = soup.title.get_text(strip=True) if soup.title else ""

    links = []

    for link in soup.find_all("a", href=True):
        links.append({
            "text": link.get_text(strip=True),
            "url": link["href"]
        })

    return {
        "title": title,
        "links": links
    }


if __name__ == "__main__":
    url = "https://example.com"

    result = scrape_website(url)

    print("Website Title:", result["title"])
    print("Links Found:", len(result["links"]))

    for link in result["links"]:
        print(link)
