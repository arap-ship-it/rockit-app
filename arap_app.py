import streamlit as st

st.page_link("arap_app.py", label="Home", icon="🏠")
st.page_link("page_1.py", label="Page 1", icon="1️⃣")
st.page_link("page_2.py", label="Page 2", icon="2️⃣", disabled=True)
st.page_link("http://www.google.com", label="Google", icon="🌎")
