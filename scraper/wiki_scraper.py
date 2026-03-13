import requests
from bs4 import BeautifulSoup


def fetch_wikipedia_page(topic):

    # Wikipedia search API
    search_url = "https://en.wikipedia.org/w/api.php"

    params = {
        "action": "query",
        "list": "search",
        "srsearch": topic,
        "format": "json"
    }

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(search_url, params=params, headers=headers)

    data = response.json()

    if not data["query"]["search"]:
        raise Exception("No Wikipedia article found")

    # Get the best matching title
    title = data["query"]["search"][0]["title"]

    page_url = f"https://en.wikipedia.org/wiki/{title.replace(' ', '_')}"

    page_response = requests.get(page_url, headers=headers)

    if page_response.status_code != 200:
        raise Exception(f"Failed to fetch Wikipedia page (status {page_response.status_code})")

    return page_response.text


def parse_article(html):

    from bs4 import BeautifulSoup

    soup = BeautifulSoup(html, "html.parser")

    title_tag = soup.find("h1")
    title = title_tag.text if title_tag else "No title found"

    paragraphs = soup.select("p")

    text = ""
    summary = ""

    for p in paragraphs:

        paragraph_text = p.get_text().strip()

        if paragraph_text:

            text += paragraph_text + " "

            # first valid paragraph becomes summary
            if summary == "":
                summary = paragraph_text

    return {
        "title": title,
        "summary": summary,
        "text": text
    }