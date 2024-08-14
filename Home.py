from openai import OpenAI
import streamlit as st

st.logo("msi-logo.png")

st.title("MSI-GPT ")

st.warning("This Proof of Concept is a non-production demonstration version of OctoStack, provided exclusively for evaluation and testing purposes. It is not intended for use in a production environment and should not be relied upon for any operational deployment.")

st.markdown("---")
st.info("""
        Sentiment: This agent is designed to analyze and summarize social media posts by identifying key 
            themes, determining sentiment, and providing a sentiment score along with 
            suggestions for improvement. 
""")
# Create buttons that link to specific pages
if st.button("Comment Sentiment", type="primary", key='sentiment'):
    st.switch_page("pages/1_Sentiment.py")