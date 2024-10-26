import streamlit as st
st.title("Welcome to My Portfolio")
st.subheader("Hi,I am Megavarshini")
st.write("I am a software developer with a passion for creating innovative solutions.")

#Introduction section
st.header("Introduction")
st.write("I am a student at kgisl institute of technology.I am pursuing my bachelor's degree in information technology")

#skill section
st.header("skills")
skills = ["Python","HTML","Basics of css"]
st.write("I have the following skills")
for i in skills:
  st.write(i)

#contact section
st.header("Contact")
st.write("you can contact me at m27305830@gmail.com")
st.write("you can also find me on linkedin")

#projects section
st.header("Projects")
st.write("Grade calculator")
st.write("This is a simple grade calculator")
st.write("It takes the marks of 5 subjects and calculates the total marks and percentage")