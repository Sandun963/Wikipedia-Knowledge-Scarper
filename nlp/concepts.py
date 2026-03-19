
nlp = spacy.load("en_core_web_sm")


def extract_concepts(text, limit=6):

    doc = nlp(text)

    concepts = []

    for ent in doc.ents:

        if ent.label_ in ["PERSON", "ORG", "GPE", "EVENT", "PRODUCT"]:
            concepts.append(ent.text)

    concepts = list(set(concepts))

    return concepts[:limit]