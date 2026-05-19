import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from langdetect import detect
from googletrans import Translator

# -----------------------------
# Load dataset
# -----------------------------
@st.cache_data
def load_data():
    data = pd.read_csv("Dataset.csv")
    return data

data = load_data()
questions = data["question"].astype(str)
answers = data["answer"].astype(str)

# -----------------------------
# Vectorizer Training
# -----------------------------
@st.cache_resource
def train_vectorizer(questions):
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(questions)
    return vectorizer, X

vectorizer, X = train_vectorizer(questions)

# -----------------------------
# Detect & Translate Input
# -----------------------------
translator = Translator()

def convert_to_english(text):
    try:
        lang = detect(text)
        if lang != "en":
            translated = translator.translate(text, dest="en").text
            return translated
        return text
    except:
        return text
    
def detect_and_translate_next_message(text_lang, next_message):
    try:
        detected_lang = detect(text_lang)
        #translator = Translator()
        translated_message = translator.translate(next_message, dest=detected_lang).text
        return translated_message
    except:
        return next_message

# -----------------------------
# Get Best Response
# -----------------------------
def get_best_response(user_input):
    user_vec = vectorizer.transform([user_input])
    similarity = cosine_similarity(user_vec, X)
    index = similarity.argmax()
    return answers.iloc[index]

# -----------------------------
# STREAMLIT UI
# -----------------------------
st.title("💬 FAQ Chatbot")
st.write("Ask a question (any language allowed)")

user_input = st.text_input("Your question:")

if user_input:
    eng_text = convert_to_english(user_input)
    response = get_best_response(eng_text)
    translated_output = detect_and_translate_next_message(user_input, response)
    st.subheader("📝 Answer:")
    st.write(translated_output)
