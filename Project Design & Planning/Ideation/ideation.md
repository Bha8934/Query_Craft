
# QueryCraft: Natural Language to SQL Converter

## 🧠 Project Ideation

### ❓ Problem It Solves
Writing SQL queries can be difficult for non-technical users. QueryCraft allows users to describe what they need in natural language, and the system converts it into an SQL query using Google's Gemini Pro AI.

### ✅ Solution
- Accepts plain English input.
- Converts to SQL using Gemini Pro API.
- Supports multiple databases: PostgreSQL, MySQL, SQLite, SQL Server.

---

## 🧱 System Architecture

### Components:

1. **User**
   - Inputs a natural language query through the UI.
   - Receives SQL output from the web app.

2. **Web App (Streamlit + Python)**
   - Provides UI for user input.
   - Prepares prompt for the Gemini Pro API.
   - Displays generated SQL query.

3. **Gemini Pro API (Google Cloud)**
   - Receives prompt with natural language query.
   - Processes and returns a valid SQL query.

---

## 📊 Data Flow

```text
[ User ] 
   ⇅  Natural Language Query
[ Web App (Streamlit) ]
   ⇅  API Call with Prompt
[ Gemini Pro API ]
   ⇅  SQL Query
[ Web App ]
   ⇅  SQL Output
[ User ]
```

---

## 🔐 Security Highlights

- API key stored in `.env` file.
- `.gitignore` used to prevent key exposure.
- HTTPS, rate limiting, session timeout supported.

---

## 📁 Project Structure

```
QueryCraft/
├── app.py
├── .env
├── requirements.txt
├── images/
└── README.md
```
