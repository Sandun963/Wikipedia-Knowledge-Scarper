from scraper.wiki_scraper import fetch_wikipedia_page, parse_article
from nlp.key_facts import extract_key_facts
from nlp.concepts import extract_concepts
from nlp.keywords import extract_keywords


def main():

    topic = input("Enter Wikipedia topic: ")

    html = fetch_wikipedia_page(topic)

    article = parse_article(html)

    text = article["text"]

    print("\nTITLE:")
    print(article["title"])

    print("\nSUMMARY:")
    print(article["summary"])

    # -------- KEY FACTS --------
    facts = extract_key_facts(text)

    print("\nKEY FACTS:")
    for f in facts:
        print("•", f)

    # -------- IMPORTANT CONCEPTS --------
    concepts = extract_concepts(text)

    print("\nIMPORTANT CONCEPTS:")
    for c in concepts:
        print("•", c)

    # -------- KEYWORDS --------
    keywords = extract_keywords(text)

    print("\nKEYWORDS:")
    for k in keywords:
        print("-", k)


if __name__ == "__main__":
    main()