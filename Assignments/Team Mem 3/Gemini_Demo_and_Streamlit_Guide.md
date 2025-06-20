
# 🧪 Gemini Demo + 🛠 Streamlit: Detailed Research & Implementation Guide

---

## 📘 Part 1: Gemini Demo – Hands-on with Google’s Generative AI

### 🔍 Introduction

Gemini is a suite of advanced multimodal AI models developed by Google DeepMind. To help developers quickly prototype applications using Gemini, Google provides a **Gemini Colab Demo Notebook**. This notebook showcases how to interact with the Gemini models—particularly **Gemini Pro** (for text) and **Gemini Pro Vision** (for image + text).

The Gemini Python SDK (`google-generativeai`) allows seamless integration of these capabilities into local scripts or apps.

---

### 🧪 Local Setup of Gemini via Python

#### Step 1: Install the SDK

```bash
pip install -U google-generativeai
```

#### Step 2: Configure API Key

```bash
touch .env
echo "GOOGLE_API_KEY=your_actual_api_key" >> .env
```

```python
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
```

#### Step 3: Initialize Gemini Client and Generate Output

```python
import google.generativeai as genai

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-pro")

response = model.generate_content("Explain how photosynthesis works.")
print(response.text)
```

---

### 💬 Example Output

**Prompt:** `"What is the capital of France?"`  
**Response:** `"The capital of France is Paris."`

**Prompt:** `"Write a Python function for factorial"`  
**Response:**

```python
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)
```

---

### 🧠 Vision Example (Image + Text)

```python
from PIL import Image

image = Image.open("invoice.jpg")
response = model.generate_content(["What is the total amount?", image])
print(response.text)
```

---

## 🔗 Reference Notebook

[Gemini Python Demo on Colab](https://colab.research.google.com/github/google/generative-ai-docs/blob/main/site/en/gemini-api/docs/get-started/python.ipynb)

---

## 🖥️ Part 2: Streamlit – Building Web Apps for AI Projects

### 🧭 Introduction

**Streamlit** is a lightweight Python framework used to convert data science and AI scripts into interactive web applications. It’s widely favored for its:

* Simplicity (no frontend skills required)
* Real-time interactivity
* Instant browser previews

---

### ⚙️ Step-by-Step Setup

#### Step 1: Install Streamlit

```bash
pip install streamlit
```

#### Step 2: Create a Python Script

```bash
touch app.py
```

#### Step 3: Write Your First App

```python
import streamlit as st

st.title("Hello Streamlit!")
name = st.text_input("What's your name?")
if st.button("Greet"):
    st.success(f"Hi {name}, welcome to Streamlit!")
```

#### Step 4: Run the App

```bash
streamlit run app.py
```

---

## 🧪 Example: QueryCraft with Streamlit + Gemini

```python
import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

st.title("QueryCraft: Natural Language → SQL")

query = st.text_input("Describe your database query:")
if st.button("Generate SQL"):
    model = genai.GenerativeModel("gemini-pro")
    prompt = f"Convert this into SQL: "{query}""
    response = model.generate_content(prompt)
    st.code(response.text, language="sql")
```

### 🧠 Sample Inputs and Outputs

**Input:**  
"List all customers who made purchases above $500 last month"

**Output:**

```sql
SELECT * FROM customers
WHERE purchase_amount > 500 AND purchase_date >= DATE_SUB(CURDATE(), INTERVAL 1 MONTH);
```

---

## 🔧 Streamlit Widgets Cheat Sheet

| Widget               | Function                  |
| -------------------- | ------------------------- |
| `st.text_input()`    | Get user text input       |
| `st.button()`        | Create a clickable button |
| `st.slider()`        | Select a numeric range    |
| `st.file_uploader()` | Upload a file             |
| `st.code()`          | Display formatted code    |
| `st.text_area()`     | Multi-line text input     |

---

## ☁️ Streamlit Deployment Tips

You can deploy Streamlit apps on:

* **Streamlit Cloud**: Free tier available, integrates with GitHub
* **Heroku** / **AWS EC2** / **GCP App Engine**

To deploy on Streamlit Cloud:

1. Push your code to GitHub
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud)
3. Link your repo and deploy in minutes

---

## 📎 Final References

* 🔗 [Gemini API Docs](https://ai.google.dev/gemini-api/docs)
* 🔗 [Gemini Demo Notebook](https://colab.research.google.com/github/google/generative-ai-docs/blob/main/site/en/gemini-api/docs/get-started/python.ipynb)
* 🔗 [Streamlit Documentation](https://docs.streamlit.io/)
* 🔗 [Streamlit Beginner Guide (GFG)](https://www.geeksforgeeks.org/a-beginners-guide-to-streamlit/)
