import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

# download required resources
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('wordnet')
nltk.download('stopwords')

def lemmatize_text(text: str) -> str:
    # split text to sentences
    sentences = sent_tokenize(text)

    # initialize lemmatizer
    lemmatizer = WordNetLemmatizer()

    # process each sentence
    lemmatized_sentences = []

    for sentence in sentences:
        words = word_tokenize(sentence)  # split sentence to words
        lemmatized_words = [lemmatizer.lemmatize(word, pos='v') for word in words if word.lower() not in stopwords.words('english')]
        lemmatized_sentences.append(" ".join(lemmatized_words))

    result = " ".join(lemmatized_sentences)

    return result
