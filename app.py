
import streamlit as st
from groq import Groq

# Page configuration
st.set_page_config(
    page_title="STUDENT PROFILE",
    page_icon="😊",
    layout="centered"
)

# Application title
st.title("🎓 Student Profile Application")
st.caption("Developed by Lahari R")
st.caption("ℹ️ Fill in your details and click View My Profile")

# Groq API configuration
try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except (KeyError, FileNotFoundError):
    st.error("API key is missing. Add it in Streamlit Secrets.")
    st.stop()

# Student details
name = st.text_input("Student Name", placeholder="Enter your name")
usn = st.text_input("USN / ROLL NUMBER", placeholder="Enter your USN")

dept = st.selectbox(
    "Department",
    ["CSE", "ISE", "ECE", "EEE", "CIVIL", "MECHANICAL"]
)

year = st.radio(
    "Current Year",
    ["1st year", "2nd year", "3rd year", "4th year"]
)

# View profile button
if st.button("View My Profile"):
    if name.strip() and usn.strip():
        st.success("Profile submitted successfully! 🎉")

        st.subheader("📋 Student Profile")

        st.text("Name: " + name)
        st.text("Roll Number: " + usn)
        st.text("Department: " + dept)
        st.text("Year: " + year)

    else:
        st.warning("Please enter both your name and USN.")
