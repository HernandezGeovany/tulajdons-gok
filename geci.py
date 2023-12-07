
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

f = open("demofile3.txt", "w")
f.write("gender","d","email","name")
f.close()

#open and read the file after the overwriting:
f = open("demofile3.txt", "r")
print(f.read())
