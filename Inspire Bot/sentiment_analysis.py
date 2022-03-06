from textblob import TextBlob


def run_sentiment(text: str)-> float:
    blob = TextBlob(text)
    return blob.sentiment.polarity
