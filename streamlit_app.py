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
