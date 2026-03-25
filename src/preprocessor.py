#cleans and tokenizes the user text
import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def preprocess(text):
    # Convert to lowercase
    text =text.lower()
    # Remove punctuation
    text=text.translate(str.maketrans('', '', string.punctuation))
    # Split into individual words(tokens)
    tokens=word_tokenize(text)
    #Remove Stopwords (common words like "the", "is", "a")
    stop_words=set(stopwords.words("english"))
    tokens=[word for word in tokens if word not in stop_words]
    return tokens