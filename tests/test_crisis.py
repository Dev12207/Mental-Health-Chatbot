import sys
sys.path.insert(0, '.')
from src.crisis_detector import is_crisis, get_crisis_response

print(is_crisis("I want to end my life"))
print(is_crisis("I feel a bit sad today"))
print(get_crisis_response())