import streamlit as st  # for UI
import os
from dotenv import load_dotenv  # to get env variables loaded into the application
import google.generativeai as genai  # import generative AI library

# Load environment variables
load_dotenv()

# Configure API key for genai
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize the model
model = genai.GenerativeModel('gemini-pro')

# Define a function to generate a response from the LLM
def get_gemini_response(ques):
    try:
        resp = model.generate_content(ques)
        return resp.text
    except Exception as e:
        return f"Error: {e}"

# Set up Streamlit app
st.set_page_config(
    page_title="Gemini pro Q/A project",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Set up header
st.header("Gemini Q/A app")

# Input
question = st.text_input("Ask a question:")

# Submit button
if st.button("Submit"):
    if question:  # Check if the question is not empty
        response = get_gemini_response(question)
        st.write("User:", question)
        st.write("Bot:", response)
    else:
        st.write("Please ask a question.")