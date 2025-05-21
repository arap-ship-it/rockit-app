import streamlit as st
st.title("~BARUDAWGH~")
st.write(
    "BEJA KA BARUDAWGH ONE KOMANDO"
)
st.page("streamlit_app.py", label="Home", icon="🏠")
st.page_link("page1.py", label="Page1.py", icon="1️⃣")
st.page_link("page2.py", label="Page2.py", icon="2️⃣", disabled=True)
st.page_link("http://www.google.com", label="Google", icon="🌎")

st.image("aleta02150.jpg")
st.balloons() 
st.badge("NO1")
import streamlit as st
st.text("Kelakuan Anak Kucai") 

sentiment_mapping = ["one", "two", "three", "four", "five"]
selected = st.feedback("stars")
if selected is not None:
    st.markdown(f"You selected {sentiment_mapping[selected]} star(s).")
