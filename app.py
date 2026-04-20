import streamlit as st
import os
import pyodbc

server = os.getenv("SQL_SERVER")
database = os.getenv("SQL_DATABASE")
username = os.getenv("SQL_USERNAME")
password = os.getenv("SQL_PASSWORD")

try:
    conn = pyodbc.connect(
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={server};DATABASE={database};UID={username};PWD={password}"
    )

    st.success("Database connected successfully")

    cursor = conn.cursor()
    cursor.execute("SELECT GETDATE()")
    row = cursor.fetchone()

    st.write("Current DB Time:", row[0])

except Exception as e:
    st.error(f"Database connection failed: {e}")