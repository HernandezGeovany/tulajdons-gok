
import datetime
import streamlit as st

title = st.text_input('email', '')

title = st.text_input('name', '')


today = datetime.datetime.now()
next_year = today.year + 1
jan_1 = datetime.date(next_year, 1, 1)
dec_31 = datetime.date(next_year, 12, 31)

d = st.date_input(
    "Select your vacation for next year",
    (jan_1, datetime.date(next_year, 1, 7)),
    jan_1,
    dec_31,
    format="MM.DD.YYYY",
)

genre = st.radio(
    "What's your gender",
    ["Male", "Female"],
    index=None,
)



