import streamlit as st

title = st.text_input('email', '')

title = st.text_input('name', '')

genre = st.radio(
    "What's your gender",
    ["mail", "Female"],
    index=None,
)



