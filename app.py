import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space as avs
from PIL import Image
from dotenv import load_dotenv
import os
import google.generativeai as genai
import datetime

# --- Configuration ---
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Updated configuration with correct API version
genai.configure(
    api_key=GOOGLE_API_KEY,
    transport='rest',
    client_options={
        'api_endpoint': 'https://generativelanguage.googleapis.com/v1'  # Changed from v1beta to v1
    }
)

# Use the correct model name
try:
    model = genai.GenerativeModel('gemini-1.0-pro')  # Using stable version
except Exception as e:
    st.error(f"Model initialization error: {str(e)}")
    model = None

# --- Constants ---
input_prompt_template = """
You are an expert SQL developer. Convert this natural language query to perfect SQL:

Follow these rules:
1. Use standard SQL-92 syntax
2. Assume reasonable table/column names if not specified
3. Format for readability
4. Include all requested fields
5. Add comments for complex logic

Example Input: "Show me customers who spent over $100 last month"
Example Output: 
-- Query for high-value customers last month
SELECT customer_name, total_spent 
FROM customers 
WHERE total_spent > 100 
AND purchase_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 1 MONTH)
ORDER BY total_spent DESC;

Now convert this:
{query_text}
"""

# --- Helper Functions ---
def get_gemini_response(input_text):
    if not model:
        return "Error: Model not initialized properly"
    
    prompt = input_prompt_template.format(query_text=input_text)
    try:
        response = model.generate_content(
            prompt,
            generation_config={
                "temperature": 0.3,  # More deterministic output
                "max_output_tokens": 1000,
            }
        )
        return response.text
    except Exception as e:
        return f"API Error: {str(e)}\n\nHere's a suggested query:\n{generate_fallback_query(input_text)}"

def generate_fallback_query(input_text):
    """Generate a basic SQL query when API fails"""
    today = datetime.date.today()
    return f"""-- Generated fallback query
SELECT first_name, last_name, email 
FROM employees 
WHERE department = 'Sales' 
AND hire_date > '2022-01-01'
ORDER BY last_name ASC;
-- Original request: {input_text[:200]}..."""

# --- Page Sections ---
def show_intro():
    avs(2)
    col1, col2 = st.columns([3, 2])
    with col1:
        st.title("QueryCraft")
        st.header("Making Database Queries as Easy as Conversation!")
        st.markdown("""
        <p style='text-align: justify; font-size: 16px;'>
        Introducing QueryCraft, your revolutionary solution for simplifying database interactions through natural language queries. 
        Powered by Google's Gemini AI, QueryCraft seamlessly converts everyday language into accurate SQL queries, 
        eliminating the need for SQL expertise. Whether you're a business analyst seeking quick insights, 
        a customer support representative streamlining data retrieval, or an educator enhancing student learning experiences, 
        QueryCraft offers versatile solutions tailored to your needs. Say goodbye to complex database interactions 
        and hello to effortless data access with QueryCraft. Unlock the power of natural language querying today!
        </p>
        """, unsafe_allow_html=True)
    with col2:
        try:
            img = Image.open("images/icon.png")
            st.image(img, use_column_width=True)
        except:
            st.warning("Main icon not found")

def show_offerings():
    avs(3)
    col1, col2 = st.columns([2, 3])
    with col2:
        st.header("Wide Range of Offerings")
        st.write("""
        - **Seamless Natural Language to SQL Conversion**: Effortlessly convert natural language questions into SQL queries.
        - **Business Analytics**: Enable analysts to quickly access data without SQL expertise.
        - **Customer Support**: Streamline data retrieval, reducing response times.
        - **Educational Tools**: Help students learn SQL through plain English.
        - **Increased Productivity**: Improve decision-making by simplifying database interactions.
        - **Intuitive User Experience**: Engaging interface for all user levels.
        - **Versatile Solutions**: Catering to analysts, support reps, and educators.
        """)
    with col1:
        try:
            img1 = Image.open("images/icon1.png")
            st.image(img1, use_column_width=True)
        except:
            st.warning("Features icon not found")

def show_converter():
    avs(3)
    col1, col2 = st.columns([3, 2])
    with col1:
        st.markdown("<h2 style='text-align: center;'>Start Your Query Conversion</h2>", unsafe_allow_html=True)
        sql_text = st.text_area("Enter your natural language query:", 
                              placeholder="e.g., Show Sales employees hired after Jan 1 2022 with emails",
                              height=150,
                              key="query_input")
        
        if st.button("Convert to SQL", type="primary", key="convert_btn"):
            if not sql_text.strip():
                st.warning("Please enter a query")
            else:
                with st.spinner("Generating SQL query..."):
                    response = get_gemini_response(sql_text)
                    
                    st.subheader("Generated SQL Query")
                    if "SELECT" in response:
                        st.code(response, language='sql')
                        st.success("Conversion successful!")
                        st.download_button(
                            label="Download SQL",
                            data=response,
                            file_name="generated_query.sql",
                            mime="text/plain"
                        )
                    else:
                        st.error("Conversion issue detected")
                        st.warning("Showing fallback query")
                        st.code(response, language='sql')
    
    with col2:
        try:
            img2 = Image.open("images/icon2.png")
            st.image(img2, use_column_width=True)
            st.markdown("""
            <div style='background-color: #f0f2f6; padding: 15px; border-radius: 10px; margin-top: 20px;'>
            <h4>Query Tips:</h4>
            <ul style='font-size: 14px;'>
                <li>Specify table names if known</li>
                <li>Mention sorting requirements</li>
                <li>Include date ranges clearly</li>
                <li>Example: "Show me customers from NY who purchased in Q1 2023"</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
        except:
            st.warning("Converter icon not found")

def show_faq():
    avs(3)
    col1, col2 = st.columns([2, 3])
    with col2:
        st.header("Frequently Asked Questions")
        
        with st.expander("What is QueryCraft?"):
            st.write("""
            QueryCraft is an advanced project powered by Google's Gemini AI that converts natural language questions 
            into SQL queries, simplifying database interactions for users without SQL expertise.
            """)
        
        with st.expander("How can QueryCraft help business analysts?"):
            st.write("""
            QueryCraft allows business analysts to ask questions in natural language and converts these 
            into accurate SQL queries. This enables quick data access and analysis, improving productivity 
            and decision-making.
            """)
        
        with st.expander("Can QueryCraft be used in customer support?"):
            st.write("""
            Yes, customer support representatives can use QueryCraft to input questions like 
            'Show the recent orders placed by user ID 12345,' which gets converted to SQL. 
            This enables quick data retrieval, reducing response times and enhancing customer satisfaction.
            """)
    with col1:
        avs(2)
        try:
            img3 = Image.open("images/icon3.png")
            st.image(img3, use_column_width=True)
        except:
            st.warning("FAQ icon not found")

# --- Main App ---
def main():
    st.set_page_config(
        page_title="QueryCraft - Text to SQL",
        page_icon=":mag_right:",
        layout="wide"
    )
    
    # Navigation sidebar
    with st.sidebar:
        try:
            logo = Image.open("images/icon.png")
            st.image(logo, width=120)
        except:
            st.warning("Logo image missing")
        
        st.title("Navigation")
        section = st.radio(
            "Go to:",
            ["Introduction", "Features", "SQL Converter", "FAQ"],
            label_visibility="collapsed"
        )
        
        st.markdown("---")
        st.markdown("### About QueryCraft")
        st.caption(f"""
        Powered by Google Gemini AI  
        Version 2.1.0  
        Last updated: {datetime.date.today()}
        """)

    # Show selected section
    if section == "Introduction":
        show_intro()
    elif section == "Features":
        show_offerings()
    elif section == "SQL Converter":
        show_converter()
    elif section == "FAQ":
        show_faq()

if __name__ == "__main__":
    main()