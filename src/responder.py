#picks and returns the right reply
import json
import random
import os
from dotenv import load_dotenv
import google.genai as genai

# Load .env file if present
if not load_dotenv():
    load_dotenv(".env.example")

# Configure Gemini API
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key) if api_key else None

def has_gemini_key():
    return api_key is not None and api_key != ""


def load_intents(filepath="data/intents.json"):
    with open(filepath, "r") as f:
        data=json.load(f)
    return data["intents"]

def get_response(intent_tag, sentiment, user_input):
    # Use Gemini to generate response
    prompt = f"You are a compassionate mental health support chatbot. The user is feeling {sentiment} and their intent seems to be {intent_tag}. Respond empathetically, helpfully, and appropriately to their message: '{user_input}'. Keep the response supportive and encouraging."
    
    if client is None:
        # No Gemini API key configured; fallback to rule-based response
        intents = load_intents()
        for intent in intents:
            if intent["tag"] == intent_tag:
                responses = intent["responses"]
                if sentiment == "distressed" and len(responses) > 1:
                    return responses[0]
                return random.choice(responses)
        for intent in intents:
            if intent["tag"] == "default":
                return random.choice(intent["responses"])
        return "I'm here for you. Can you tell me more?"

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text.strip()
    except Exception:
        # Fallback to rule-based if API fails
        intents = load_intents()
        for intent in intents:
            if intent["tag"]==intent_tag:
                responses=intent["responses"]
                if sentiment=="distressed" and len(responses)>1:
                    return responses[0]
                return random.choice(responses)
        for intent in intents:
            if intent["tag"]=="default":
                return random.choice(intent["responses"])
        return "I'm here for you. Can you tell me more?"
