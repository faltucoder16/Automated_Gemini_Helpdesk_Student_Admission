# app.py

import streamlit as st
from chatbot_backend import get_ai_response

st.set_page_config(page_title="Student Admission Helpdesk", layout="centered")

st.title("🎓 Student Admission Helpdesk")
st.markdown("Ask any question related to admissions!")

user_query = st.text_input("Enter your query here:")

if st.button("Get Response"):
    if user_query:
        with st.spinner("Thinking..."):
            response = get_ai_response(user_query)
        st.success("Response:")
        st.write(response)
    else:
        st.warning("Please enter a question.")
