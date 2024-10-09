import streamlit as st

st.title("hello world")

name = st.text_input ("your name", key = "name")

if st.button("click me"):
    st.write(f"hello,{name}!")