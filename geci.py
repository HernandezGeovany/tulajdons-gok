
import datetime
import streamlit as st

email = st.text_input('email', '')

name = st.text_input('name', '')


d = st.date_input("When's your birthday", value=None)
st.write('Your birthday is:', d
)

gender = st.radio(
    "What's your gender",
    ["Male", "Female"],
    index=None,
)

with open("my_file.txt", "a") as f:
   f.write(email,d,gender,name)
