
import datetime
import streamlit as st

title = st.text_input('email', '')

title = st.text_input('name', '')


d = st.date_input("When's your birthday", value=None)
st.write('Your birthday is:', d
)

genre = st.radio(
    "What's your gender",
    ["Male", "Female"],
    index=None,
)



