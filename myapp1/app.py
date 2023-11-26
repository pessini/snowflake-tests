import streamlit as st
import os

st.write(f"Current folder: {os.path.dirname(__file__)}")

filename = "data/file.txt"
try:
    with open(filename, "r") as file:
        st.write(f"{filename} content: {file.read()}")
except:
    st.error(f"Cannot open {filename}")

filename = f"{os.path.dirname(__file__)}/data/file.txt"
try:
    with open(filename, "r") as file:
        st.write(f"{filename} content: {file.read()}")
except:
    st.error(f"Cannot open {filename}")

filename = "../myapp2/data/file.txt"
try:
    with open(filename, "r") as file:
        st.write(f"{filename} content: {file.read()}")
except:
    st.error(f"Cannot open {filename}")

filename = "/mount/src/snowflake-tests/myapp1/data/file.txt"
try:
    with open(filename, "r") as file:
        st.write(f"{filename} content: {file.read()}")
except:
    st.error(f"Cannot open {filename}")
