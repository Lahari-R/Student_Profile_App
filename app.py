import streamlit as st

st.set_page_config(
    page_title="Student Profile Application",
    page_icon="🎓"
)

st.title("🎓 Student Profile Application")
st.subheader("Developed by Student Name")

st.info("Fill in your details and click View My Profile.")

with st.form("student_form"):

    name = st.text_input("Student Name", placeholder="Enter your name")

    usn = st.text_input("USN / Roll Number", placeholder="Enter roll number")

    department = st.selectbox(
        "Department",
        ["CSE", "ISE", "ECE", "EEE", "Mechanical", "Civil"]
    )

    year = st.radio(
        "Current Year",
        ["1st Year", "2nd Year", "3rd Year", "4th Year"]
    )

    submit = st.form_submit_button("View My Profile")

if submit:
    if name.strip() and usn.strip():

        st.success("Profile Created Successfully!")

        st.subheader("My Student Profile")
        st.write("Student Name:", name)
        st.write("USN / Roll Number:", usn)
        st.write("Department:", department)
        st.write("Current Year:", year)

    else:
        st.warning("Please enter your name and USN.")
