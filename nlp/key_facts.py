

nlp = spacy.load("en_core_web_sm")


def extract_key_facts(text, limit=5):

    doc = nlp(text)

    sentences = [sent.text.strip() for sent in doc.sents]

    facts = []

    for s in sentences:

        if len(s) > 60 and len(facts) < limit:
            facts.append(s)

    return facts