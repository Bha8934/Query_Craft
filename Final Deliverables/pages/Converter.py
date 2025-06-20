# pages/1_Text_to_SQL.py
from dotenv import load_dotenv
import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space as avs
import google.generativeai as genai
import os
from PIL import Image
import pandas as pd
import sqlite3
from datetime import datetime

# Set page config early
st.set_page_config(page_title="Text to SQL Converter", page_icon=":memo:")
st.title("🧠 Text to SQL Converter")

# Display image
try:
    image = Image.open("images/icon1.png")
    st.image(image, use_container_width=True, caption="Your QueryCraft Conversion Tool")
except FileNotFoundError:
    st.warning("Image not found. Make sure it's placed in the 'images/' folder.")

# Load environment variables
load_dotenv()

# Configure Gemini with API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize the generative model
model = genai.GenerativeModel('gemini-1.5-flash')

# SQLite setup
conn = sqlite3.connect("querycraft.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS queries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        input_text TEXT NOT NULL,
        sql_generated TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""")
conn.commit()

def get_gemini_response(input):
    response = model.generate_content(input)
    return response.text

# Prompt template definition
input_prompt_template = """
You are an expert SQL developer that converts natural language queries into precise SQL statements.
Your task is to convert English descriptions into valid, optimized SQL queries.

Guidelines:
1. Identify all relevant tables
2. Select only necessary columns
3. Apply proper filtering conditions
4. Include sorting/grouping when specified
5. Use correct SQL syntax and formatting

Examples:

Example 1:
Input: "Retrieve the names and ages of all employees who are older than 30 years."
Output: 
SQL Query:
SELECT name, age FROM employees
WHERE age > 30;

Example 2:
Input: "Get the total sales amount from the orders table."
Output:
SQL Query:
SELECT SUM(amount) AS total_sales FROM orders;

Example 3:
Input: "Find customers who made purchases in the last month, sorted by purchase date descending."
Output:
SQL Query:
SELECT customer_name FROM purchases
WHERE purchase_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 1 MONTH)
ORDER BY purchase_date DESC;

Example 4:
Input: "Show the average salary by department."
Output:
SQL Query:
SELECT department, AVG(salary) AS avg_salary FROM employees
GROUP BY department;

Now convert this English description to SQL:

Input: {sql_text}

Important Notes:
- Always start with "SQL Query:" on its own line
- Format the query with proper indentation (4 spaces for continuation lines)
- Use standard SQL functions and syntax
- Include column aliases for aggregates
- Correct any typos in the input if necessary
"""

sql_text = st.text_area("Enter your natural language query:",
    placeholder="e.g., Show all customers who purchased more than $100 last month",
    height=150)

submit = st.button("Convert to SQL", type="primary")

if submit and sql_text.strip():
    try:
        prompt = input_prompt_template.format(sql_text=sql_text)
        response = get_gemini_response(prompt)

        # Store in SQLite DB
        cursor.execute(
            "INSERT INTO queries (input_text, sql_generated) VALUES (?, ?)",
            (sql_text, response)
        )
        conn.commit()

        with st.expander("🧾 Generated SQL Query", expanded=True):
            st.code(response, language="sql")
            st.text_area("Copy SQL", value=response, height=150)

        st.subheader("📊 Sample Output Preview")
        sample_data = pd.DataFrame({
            "customer_name": ["Alice", "Bob"],
            "purchase_amount": [120, 180]
        })
        st.dataframe(sample_data)

        st.download_button(
            label="📥 Download SQL",
            data=response,
            file_name="query.sql",
            mime="text/sql"
        )

        # Demo in-memory execution
        st.subheader("⚙️ Run Query on Sample Table")
        st.info("Running SELECT queries only on a mock 'employees' table.")

        demo_conn = sqlite3.connect(":memory:")
        demo_cursor = demo_conn.cursor()
        demo_cursor.execute("""
            CREATE TABLE employees (
                id INTEGER PRIMARY KEY,
                name TEXT,
                age INTEGER,
                department TEXT,
                salary REAL
            )
        """)
        demo_cursor.executemany("INSERT INTO employees (name, age, department, salary) VALUES (?, ?, ?, ?)", [
            ("Alice", 32, "Sales", 60000),
            ("Bob", 45, "HR", 75000),
            ("Carol", 29, "IT", 68000),
            ("David", 38, "Sales", 72000),
        ])
        demo_conn.commit()

        safe_sql = response.strip().lower()
        if safe_sql.startswith("select"):
            try:
                result_df = pd.read_sql_query(response, demo_conn)
                st.dataframe(result_df, use_container_width=True)
            except Exception as e:
                st.error(f"Execution error: {e}")
        else:
            st.warning("Only SELECT queries are allowed for security reasons.")

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
elif submit:
    st.warning("Please enter a query to convert.")

# Sidebar: Display history from SQLite
with st.sidebar:
    st.subheader("🕘 Your History (Saved)")
    cursor.execute("SELECT input_text, created_at FROM queries ORDER BY created_at DESC LIMIT 5")
    rows = cursor.fetchall()
    if rows:
        for idx, (q, created_at) in enumerate(rows):
            st.markdown(f"**{idx+1}.** {q}  \n*{created_at}*")
        if st.button("🗑️ Clear All History"):
            cursor.execute("DELETE FROM queries")
            conn.commit()
            st.experimental_rerun()
    else:
        st.info("No queries saved yet.")
