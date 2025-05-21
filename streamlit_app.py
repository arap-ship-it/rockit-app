import streamlit as st
st.title("~BARUDAWGH~")
st.write(
    "BEJA KA BARUDAWGH ONE KOMANDO"
)
st.image("aleta02150.jpg")
st.balloons() 
st.badge("NO1")
import streamlit as st
st.text("Kelakuan Anak Kucai") 

sentiment_mapping = ["one", "two", "three", "four", "five"]
selected = st.feedback("stars")
if selected is not None:
    st.markdown(f"You selected {sentiment_mapping[selected]} star(s).")
    import streamlit as st

st.page_link("streamlit_app.py", label="Home", icon="🏠")
st.page_link("page_1.py", label="Page 1", icon="1️⃣")
st.page_link("page_2.py", label="Page 2", icon="2️⃣", disabled=True)
st.page_link("http://www.google.com", label="Google", icon="🌎")
