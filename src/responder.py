#picks and returns the right reply
import json
import random

def load_intents(filepath="data/intents.json"):
    with open(filepath, "r") as f:
        data=json.load(f)
    return data["intents"]

def get_response(intent_tag, sentiment):
    intents=load_intents()

    for intent in intents:
        if intent["tag"]==intent_tag:
            responses=intent["responses"]
            # If user is distressed, try to pick a more empathetic response
            if sentiment=="distressed" and len(responses)>1:
                return responses[0]
            return random.choice(responses)
    #Fallback to default if tag not found
    for intent in intents:
        if intent["tag"]=="default":
            return random.choice(intent["responses"])
    return "I'm here for you. Can you tell me more?"
