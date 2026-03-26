#detects what the user wants to say
import json
from src.preprocessor import preprocess

def load_intents(filepath="data/intents.json"):
    with open(filepath, "r") as f:
        data=json.load(f)
    return data["intents"]

def classify_intent(text):
    intents=load_intents()
    tokens=preprocess(text)
    best_match=None
    best_score=0
    for intent in intents:
        if intent["tag"]=="default":
            continue
        for pattern in intent["patterns"]:
            pattern_tokens=preprocess(pattern)

            #Count how many tokens match
            matches=len(set(tokens) & set(pattern_tokens))
            if matches>best_score:
                best_score=matches
                best_match=intent["tag"]
    #If nothing matched, return default
    if best_match is None or best_score==0:
        return "default"
    return best_match