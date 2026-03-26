import sys
sys.path.insert(0, '.')
from src.intent_classifier import classify_intent

print(classify_intent("hello there"))
print(classify_intent("I feel really sad today"))
print(classify_intent("I am so anxious and worried"))
print(classify_intent("thank you so much"))
print(classify_intent("xyzabc gibberish"))