#This is the main file for the application. It will run and process all the logic
import streamlit as st
from src.preprocessor import preprocess
from src.sentiment_analyzer import analyze_sentiment
from src.crisis_detector import is_crisis, get_crisis_response
from src.intent_classifier import classify_intent
from src.responder import get_response, has_gemini_key

#Page Config
st.set_page_config(
    page_title="Mental Health Support Bot",
    page_icon="🧠",
)
#Title
st.title("Mental Health Support Bot")
st.caption("A safe space to talk. I'm here to listen. ")

if not has_gemini_key():
    st.warning("Gemini API key is not configured. The bot will use rule-based responses until GEMINI_API_KEY is set in .env.")

#Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages=[]
    st.session_state.messages.append({
        "role": "assistant",
        "content": "Hi there! I'm here to listen and support you. How are you feeling today?"
    })
#Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
#User input box at the bottom
user_input=st.chat_input("Type how you're feeling...")
if user_input:
    #show user message
    st.session_state.messages.append({
        "role":"user",
        "content":user_input
    })
    with st.chat_message("user"):
        st.markdown(user_input)
    #Generate bot response
    with st.chat_message("assistant"):
        #Step 1: Check for crisis first
        if is_crisis(user_input):
            response=get_crisis_response()
        
        else:
            #Step 2: Analyze sentiment
            sentiment=analyze_sentiment(user_input)
            #Step 3: Classify intent
            intent=classify_intent(user_input)
            #step 4: Get response
            response=get_response(intent, sentiment, user_input)
        st.markdown(response)
    #Save bot response to chat history
    st.session_state.messages.append({
        "role":"assitant",
        "content":response
    })        
