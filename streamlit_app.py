import streamlit as st

st.title("~BARUDAWGH~")
st.write(
    "BEJA KA BARUDAWGH ONE KOMANDO"
)
st.image("aleta02150.jpg")
st.balloons() 
st.badge("NO1")
import streamlit as st

audio_value = st.audio_input("Record a voice message")

if audio_value:
    st.audio(audio_value)
import streamlit as st

sentiment_mapping = ["one", "two", "three", "four", "five"]
selected = st.feedback("stars")
if selected is not None:
    st.markdown(f"You selected {sentiment_mapping[selected]} star(s).")
