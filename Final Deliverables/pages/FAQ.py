# pages/2_FAQ.py
import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space as avs
from PIL import Image

st.set_page_config(page_title="FAQs", page_icon="❓")
st.title("❓ Frequently Asked Questions")

col1, col2 = st.columns([2, 3])

with col2:
    st.markdown("**Question:** What is QueryCraft?")
    st.markdown("""
    **Answer:** QueryCraft is a natural language interface for SQL. Powered by Gemini,
    it allows users to generate SQL queries from plain English inputs.
    """)
    avs(2)

    st.markdown("**Question:** Who can use QueryCraft?")
    st.markdown("""
    **Answer:** It's ideal for:
    - Business analysts
    - Students
    - Developers
    - Customer support teams
    """)
    avs(2)

    st.markdown("**Question:** How does it work?")
    st.markdown("""
    **Answer:** You enter a natural language query, and QueryCraft uses a LLM model to
    generate the corresponding SQL.
    """)
    avs(2)

    st.markdown("**Question:** What models are used?")
    st.markdown("""
    **Answer:** Currently it uses Google's Gemini 1.5 Flash model for lightweight and fast performance.
    """)

with col1:
    try:
        img = Image.open("images/faq_icon.png")
        st.image(img, use_container_width=True, caption="QueryCraft FAQ")
    except FileNotFoundError:
        st.image("https://via.placeholder.com/400x500?text=QueryCraft+FAQ", use_container_width=True)
