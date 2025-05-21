import streamlit as st

st.page_link("streamlit_app.py", label="Home", icon="🏠")
st.page_link("page1.py", label="Page1", icon="1️⃣")
st.page_link("page2.py", label="Page2", icon="2️⃣", disabled=True)
st.page_link("http://www.google.com", label="Google", icon="🌎")
