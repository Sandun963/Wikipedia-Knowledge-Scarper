import spacy

nlp = spacy.load("en_core_web_sm")


def extract_keywords(text, limit=8):

    doc = nlp(text)

    keywords = []

    for chunk in doc.noun_chunks:

        word = chunk.text.lower().strip()

        if len(word) > 3:
            keywords.append(word)

    keywords = list(set(keywords))

    return keywords[:limit]