import streamlit as st

st.page("page2.py", label="Page 1", icon="1️⃣")
st.page("page3.py", label="Page 2", icon="2️⃣", disabled=True)
st.page("http://www.google.com", label="Google", icon="🌎")
