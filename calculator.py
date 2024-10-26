import streamlit as st

st.title("Basic calculator")
st.write("""
1.addition
2.subtraction
3.multiplication
4.Division""")
choice = st.number_input("Enter your choice", value=0)
num_1 = st.number_input("Enter your first number", value=0.0)
num_2 = st.number_input("Enter your second number", value=0.0)
st.button("cff")
if st.button("Enter"):
  if choice == 1:
    result = (num_1 + num_2)
  elif choice == 2:
    result = num_1 - num_2
  elif choice == 3:
    result = num_1 * num_2
  else:
    result = num_1 / num_2
  st.write("The result is", result)