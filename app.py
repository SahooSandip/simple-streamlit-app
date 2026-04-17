import os
import streamlit as st

st.set_page_config(page_title="Simple Azure App", layout="centered")

st.title("Simple Azure Streamlit App")
st.write("Azure setup is complete.")

st.subheader("Environment Check")

st.write("SQL_SERVER:", os.getenv("SQL_SERVER", "Not found"))
st.write("SQL_DATABASE:", os.getenv("SQL_DATABASE", "Not found"))
st.write("SQL_USERNAME:", os.getenv("SQL_USERNAME", "Not found"))

if os.getenv("SQL_PASSWORD"):
    st.write("SQL_PASSWORD: Loaded")
else:
    st.write("SQL_PASSWORD: Not found")