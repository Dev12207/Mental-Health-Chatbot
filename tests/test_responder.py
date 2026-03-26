import sys
sys.path.insert(0, '.')
from src.responder import get_response

print(get_response("greet", "positive"))
print(get_response("feeling_sad", "sad"))
print(get_response("feeling_anxious", "distressed"))
print(get_response("default", "neutral"))