# backend/humor_models.py
import re
import random
from textblob import TextBlob
import spacy
import google.generativeai as genai

# Initialize spaCy
nlp = spacy.load("en_core_web_sm")

# Rule-based Humor Detection
def rule_based_humor_detection(text):
    if re.search(r"Why did.*?do.*?because", text):
        return True
    return False

# Rule-based Joke Generation
def rule_based_joke_generation(theme):
    templates = [
        f"Why did {theme} cross the road? To get to the other side!",
        f"Why don't {theme}s tell secrets? Because they are too loud!"
    ]
    return random.choice(templates)

# NLP Humor Detection
def nlp_humor_detection(text):
    sentiment = TextBlob(text).sentiment.polarity
    doc = nlp(text)
    pos_tags = [token.pos_ for token in doc]
    if "VERB" in pos_tags and sentiment < 0:
        return True
    return False

# Transformer Model - Humor Detection (using Gemini API or GPT)
genai.configure(api_key="YOUR_API_KEY")

def transformer_humor_detection(text):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(f"Is this text funny? '{text}' Answer with Yes or No.")
    if "yes" in response.text.lower():
        return True
    return False

# Rule-based, NLP, Transformer Combination for Humor Detection
def detect_humor(text):
    if rule_based_humor_detection(text):
        return True
    elif nlp_humor_detection(text):
        return True
    elif transformer_humor_detection(text):
        return True
    return False

# Rule-based Joke Generation
def generate_joke(theme):
    joke = rule_based_joke_generation(theme)
    if not joke:
        joke = "No joke available!"
    return joke
