"""lemmatization service module"""

import spacy
from langdetect import detect

nlp_models = {
    "en": spacy.load("en_core_web_sm"),
    "ru": spacy.load("ru_core_news_sm"),
    "pl": spacy.load("pl_core_news_sm"),
    "uk": spacy.load("uk_core_news_sm"),
}


def lemmatize_text(text: str) -> list:
    """
    lemmatize text using spaCy NLP models.

    :param text: text to lemmatize
    :return: list of the lemmatized words
    """
    # detect a text language
    try:
        language = detect(text)
    except Exception as exc:
        raise ValueError("Text language detection failed.") from exc

    if language not in nlp_models:
        raise ValueError(
            f"'{language}' language is not supported yet. "
            + f"Supported languages: {", ".join(nlp_models.keys())}"
        )

    # get target spacy model
    nlp = nlp_models[language]

    # process text using spacy pipeline
    doc = nlp(text)

    # get lemmatized words of the text
    lemmatized_words = [
        token.lemma_ for token in doc if not token.is_punct and not token.is_space
    ]

    return lemmatized_words
