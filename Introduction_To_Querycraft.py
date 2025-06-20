# Introduction To QueryCraft (Welcome Page)
import streamlit as st
from PIL import Image

st.set_page_config(page_title="Introduction To QueryCraft", page_icon=":sparkles:", layout="wide")

st.title("Welcome to QueryCraft! 🧠")

col1, col2 = st.columns([3, 2])

with col1:
    st.markdown("""
        QueryCraft is your intelligent assistant that converts natural language
        into SQL with ease.

        👉 Use the sidebar to:
        - Convert English queries to SQL
        - Explore FAQs

        Whether you're a data analyst, a student, or just curious about data,
        QueryCraft is here to make SQL simple.
        

        Introducing QueryCraft, your revolutionary solution for simplifying database interactions through natural language queries.
        Powered by a cutting-edge Large Language Model (LLM), QueryCraft seamlessly converts everyday language into accurate SQL queries,
        eliminating the need for SQL expertise. Whether you're a business analyst seeking quick insights, a customer support representative
        streamlining data retrieval, or an educator enhancing student learning experiences, QueryCraft offers versatile solutions tailored
        to your needs. Say goodbye to complex database interactions and hello to effortless data access with QueryCraft. Unlock the power of natural language querying today!

    """)

with col2:
    try:
        img = Image.open("images/icon.png")
        st.image(img, use_container_width=True)
    except FileNotFoundError:
        st.image("https://via.placeholder.com/300x300?text=QueryCraft+Welcome", use_container_width=True)

st.markdown("---")
st.success("Use the sidebar to get started.")
