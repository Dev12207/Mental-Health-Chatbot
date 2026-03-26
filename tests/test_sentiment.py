import sys
sys.path.insert(0,'.')
from src.sentiment_analyzer import analyze_sentiment

print(analyze_sentiment("I am so happy today!"))
print(analyze_sentiment("I am okay I guess"))
print(analyze_sentiment("I feel hopeless and empty"))
print(analyze_sentiment("I want to end everything"))
