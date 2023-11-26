import streamlit as st
import os

st.write(f"Current folder: {os.path.dirname(__file__)}")

with open("data/file.txt", "r") as file:
    st.write(f"File.txt content: {file.read()}")

with open("../myapp1/data/file.txt", "r") as file:
    st.write(f"Myapp1 File.txt content: {file.read()}")