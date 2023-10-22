import spacy
from textblob import TextBlob

nlp = spacy.load('en_core_web_sm')

def get_sentiment(text):
    """This function receives a text and returns its sentiment polarity and subjectivity."""
    doc = nlp(text)
    sentiment = TextBlob(text).sentiment
    return sentiment