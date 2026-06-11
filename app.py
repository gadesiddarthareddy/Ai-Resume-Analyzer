import streamlit as st

st.title("AI Resume Analyzer")

name = st.text_input("Enter your name")

resume = st.file_uploader("Upload Resume", type=["pdf"])

if st.button("Analyze"):

    if resume:
        st.success("Resume uploaded successfully!")

        st.write("Name:", name)
        st.write("Resume Name:", resume.name)
        st.write("Resume Size:", round(resume.size/1024, 2), "KB")

        st.subheader("Resume Score")
        st.progress(75)
        st.write("Your resume score: 75/100")

    else:
        st.warning("Please upload a resume.")
