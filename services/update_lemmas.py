from spacy.language import Language

custom_lemmas = {
    "ru": {
        "вордпресс": "wordpress",
        "вордпрессе": "wordpress",
        "вордпрессу": "wordpress",
        "вордпрессом": "wordpress",
        "вордпресса": "wordpress",
    }
}


def add_custom_lemmatizers(nlp_models: dict[str, Language]):
    nlp_models["ru"].add_pipe("ru_custom_lemmatizer", after="lemmatizer")


@Language.component(name="ru_custom_lemmatizer")
def _ru_custom_lemmatizer_function(doc):
    return _custom_lemmatizer_function(doc, custom_lemmas["ru"])


def _custom_lemmatizer_function(doc, rels: dict[str, str]):
    for token in doc:
        if token.norm_ in rels:
            token.lemma_ = rels[token.norm_]

    return doc
