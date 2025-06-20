# 🌟 Gemini Prompt Design

# 🖋️ Designing Prompts for Accurate SQL Generation

**Objective:**\
Ensure that prompts sent to Gemini are structured to produce syntactically correct and context-aware SQL queries.

**Prompt Structure Example:**

```python
prompt_template = f"""
You are an expert SQL assistant. Convert the following natural language question to an SQL query.
Use the following database schema:
{schema}

User Question: {user_question}

SQL Query:
"""
```

**🔹 Key Tips:**

- ✅ Always include the database schema.
- ✅ Use clear instructions like "Convert to SQL" or "Generate query".
- ✅ Enclose all variables (e.g., table names) with context to avoid ambiguity.
- ✅ Add examples in the prompt to improve accuracy if needed.

**🖊️ Sample Prompt:**

```python
schema = """
Table: employees
Columns: id, name, age, department, salary
"""

user_question = "List all employees older than 30."
```

---

# 🔒 Security Features

# 🔐 Security Features in QueryCraft

## 1. 📁 API Key Management

Use the `.env` file to store the Gemini API key securely.

```bash
# .env
GEMINI_API_KEY=your_api_key_here
```

**🧰 Access in Python:**

```python
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('GEMINI_API_KEY')
```

## 2. ⏰ Rate Limiting (Basic Implementation)

Prevent abuse by limiting requests.

```python
from flask_limiter import Limiter
from flask import Flask

app = Flask(__name__)
limiter = Limiter(app, default_limits=["100 per hour"])
```

## 3. 🌐 CORS & Headers (Optional)

Add CORS and secure headers to avoid external misuse.

```python
from flask_cors import CORS
CORS(app)
```

---

# 📂 Database Support

# 📊 Supported Databases and Connection Setup

QueryCraft supports:

- ✅ MySQL
- ✅ PostgreSQL
- ✅ SQLite

## 1. 💾 SQLite Setup (Local)

```python
import sqlite3
conn = sqlite3.connect('example.db')
cursor = conn.cursor()
```

## 2. 💼 MySQL Setup

```python
import mysql.connector

conn = mysql.connector.connect(
  host="localhost",
  user="youruser",
  password="yourpass",
  database="yourdb"
)
cursor = conn.cursor()
```

## 3. 📁 PostgreSQL Setup

```python
import psycopg2

conn = psycopg2.connect(
    dbname="yourdb",
    user="youruser",
    password="yourpass",
    host="localhost"
)
cursor = conn.cursor()
```

**🔹 Tip:** Use ORM like SQLAlchemy for unified code across all databases.

---

# 📄 Code Snippets

# 📝 Core Function Snippets in QueryCraft

## 1. 🎨 Get Gemini Response

```python
def get_gemini_response(prompt, model):
    response = model.generate_content(prompt)
    return response.text
```

## 2. ✏️ Convert Text to SQL

```python
def convert_question_to_sql(user_question, schema, model):
    prompt = f"""
    Use the schema below and convert the question into SQL:
    Schema: {schema}
    Question: {user_question}
    SQL:
    """
    return get_gemini_response(prompt, model)
```

## 3. ▶️ Execute SQL

```python
def run_sql_query(sql_query, conn):
    cursor = conn.cursor()
    cursor.execute(sql_query)
    return cursor.fetchall()
```

## 4. 🚪 Flask Route (Example)

```python
@app.route('/query', methods=['POST'])
def handle_query():
    data = request.json
    sql_query = convert_question_to_sql(data["question"], data["schema"], model)
    result = run_sql_query(sql_query, db_conn)
    return jsonify(result)
```

