#Detects if user is happy, sad, or neutral
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer=SentimentIntensityAnalyzer()
def analyze_sentiment(text):
    scores=analyzer.polarity_scores(text)
    compound=scores['compound']
    if compound<=-0.5:
        return "distressed"
    elif compound<0:
        return "sad"
    elif compound==0:
        return "neutral"
    else:
        return "positive"