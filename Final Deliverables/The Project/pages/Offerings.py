# pages/2_Offerings.py

import streamlit as st
from PIL import Image

st.set_page_config(page_title="Offerings", page_icon="📊", layout="wide")

# Page Title
st.title("📊 Wide Range of Offerings")

# Layout with image and text
col1, col2 = st.columns([1.5, 2])

with col1:
    try:
        img = Image.open("images/offerings.png")  # Make sure the file path and name are correct
        st.image(img, use_container_width=True)
    except FileNotFoundError:
        st.image("https://via.placeholder.com/500x400?text=Offerings+Illustration", use_container_width=True)

with col2:
    st.markdown("### Wide Range of Offerings")
    st.markdown("""
    - **Seamless Natural Language to SQL Conversion**: Effortlessly convert natural language questions into SQL queries.
    - **Business Analytics**: Enable business analysts to quickly access and analyze data without needing SQL expertise.
    - **Customer Support**: Streamline data retrieval for customer service representatives, reducing response times and enhancing satisfaction.
    - **Educational Tools**: Assist students in learning SQL by allowing them to input queries in plain English.
    - **Increased Productivity**: Improve decision-making and productivity by simplifying database interactions.
    - **Intuitive User Experience**: Provide an intuitive and engaging experience for users across various scenarios.
    - **Versatile Solutions**: Cater to the needs of business analysts, support representatives, and educators.
    """)

