#checks for danger signals in the messaage
import os

def load_crisis_keywords(filepath="data/crisis_keywords.txt"):
    if not os.path.exists(filepath):
        return[]
    with open(filepath, "r") as f:
        keywords=[line.strip().lower() for line in f.readlines()]
        return keywords
    
def is_crisis(text):
    keywords=load_crisis_keywords()
    text=text.lower()
    for keyword in keywords:
        if keyword in text:
            return True
    return False

def get_crisis_response():
    return ("I'm really concerned about what you just shared. "
            "please know you are not alone. "
            "Reach out to iCall right now - they are here to help you: "
            "📞 iCall: 9152987821 (Mon–Sat, 8am–10pm). "
            "You matter and help is available. "
    )

