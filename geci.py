import streamlit as st

title = st.text_input('email', '')

title = st.text_input('name', '')

title = st.text_input('how old are you', '')

genre = st.radio(
    "What's your gender",
    ["Male", "Female"],
    index=None,
)



