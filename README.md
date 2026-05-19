# Multilingual-Chatbot

A simple and intelligent **FAQ Chatbot** built using **Python** and **Streamlit** that can answer user questions in multiple languages.
The chatbot uses **TF-IDF Vectorization** and **Cosine Similarity** to find the most relevant answer from a dataset.

---

## 🚀 Features

* 🌍 Supports multiple languages
* 🔄 Automatic language detection
* 🌐 Translates user questions to English
* 🤖 Finds best matching answer using NLP
* 📝 Translates response back to user language
* ⚡ Fast and lightweight Streamlit UI
* 📊 Uses Machine Learning concepts for text similarity

---

## 🛠️ Technologies Used

* Python
* Streamlit
* Pandas
* Scikit-learn
* TF-IDF Vectorizer
* Cosine Similarity
* Google Translate API
* LangDetect

---

## 📊 How It Works

### Step 1: Load Dataset

The chatbot loads questions and answers from `Dataset.csv`.

### Step 2: Train TF-IDF Vectorizer

Questions are converted into numerical vectors using TF-IDF.

### Step 3: Detect Language

The chatbot detects the language of the user input.

### Step 4: Translate to English

If the question is not in English, it gets translated.

### Step 5: Find Best Match

Cosine similarity compares user question with dataset questions.

### Step 6: Generate Response

Best matching answer is selected.

### Step 7: Translate Response

Answer is translated back to the user's language.

---

## 📌 Example

### User Input

```text
What is Artificial Intelligence?
```

### Chatbot Response

```text
Artificial Intelligence is the simulation of human intelligence by machines.
```

---

## 📦 Requirements

Example `requirements.txt`

```txt
streamlit
pandas
scikit-learn
langdetect
googletrans==4.0.0-rc1
