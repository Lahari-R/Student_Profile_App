import streamlit as st
from groq import Groq
st.set_page_config(page_title='STUDENT PROFILE', page_icon='😊' layout='centered')
st.title('🎓Student Profile App')
st.caption('Developed by Lahari R')
st.caption('ℹ️Fill in your detailes and click View my profile')
try:
  client=Groq(api_key=st.secrets['GROQ_API_KEY'])
except(KeyError,FileNotFoundError):
  st.error("API key is missing. Add it on advanced settings")
  st.stop
name=st.text_input('Student Name','Enter your name')
usn=st.text_input('USN/ ROLL NUMBER','Enter your USN')
dept=st.selectbox('Department', ['CSE', 'ISE', 'ECE', 'EEE','CIVIL','MECHANICAL'])
year=st.radio('Current Year',['1st year','2nd year','3rd year','4th year'])
if st.button('View my profile'):
  if name and usn:
    st.caption('Profile submitted successfully')
    st.text('Name:'+name)
    st.text('Roll:'+usn)
    st.text('Dept:'+dept)
    st.text('Year:'+year)
