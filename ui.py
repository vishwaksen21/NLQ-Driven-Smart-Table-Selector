import streamlit as st
import requests

# Set up Streamlit UI
st.title("AI-Powered Table Selector")
st.write("Enter a natural language query, and the system will return the most relevant tables.")

# User input
query = st.text_input("Enter your query:", placeholder="E.g., Show me all orders placed last month.")

# Send query to FastAPI when user enters text
if query:
    response = requests.get(f"http://127.0.0.1:8000/select_tables/?query={query}")
    
    if response.status_code == 200:
        st.subheader("Relevant Tables:")
        st.json(response.json())  # Display API response as JSON
    else:
        st.error("Error fetching results. Make sure the FastAPI server is running.")
