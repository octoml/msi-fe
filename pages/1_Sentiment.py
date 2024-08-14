import streamlit as st
from openai import OpenAI
import toml


examples = toml.load(".streamlit/examples.toml")

MODEL_NAME = examples["inference_params"]["model_name"]
API_KEY = examples["inference_params"]["key"]
BASE_URL = examples["inference_params"]["base_url"]

def render_main_content():
    st.title("MSI-GPT: Comment Sentiment")
    st.warning("""This Proof of Concept is a non-production demonstration version of OctoStack, provided exclusively for evaluation and testing purposes. 
               It is not intended for use in a production environment and should not be relied upon for any operational deployment.
                """)
    st.warning("""
               For trust and safety purposes, please be advised that all prompts and responses are logged and securely 
               stored in a privately-owned database hosted and operated by MSI.
                """)
    st.markdown("---")
    
def initialize_session_state():
    if "messages" not in st.session_state:
        st.session_state["messages"] = [
            {"role": "assistant", "content": "Feel free to copy in content, type or use the example to start."}
        ]
    if "response" not in st.session_state:
        st.session_state["response"] = None

def display_chat_messages():
    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])
        
def handle_user_input(client, system_message):
    # Regular user input
    if prompt := st.chat_input("Message"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)

        # Include entire chat history
        messages_for_api = [system_message] + st.session_state.messages
        
        with st.chat_message("assistant"):
            response = client.chat.completions.create(
                model=MODEL_NAME, 
                messages=messages_for_api, 
                max_tokens=4096,
                stream=False,
                temperature=0.0
            )
            st.write(response.choices[0].message.content)
        
        st.session_state.messages.append({"role": "assistant", "content": response.choices[0].message.content})
        st.session_state["response"] = response.choices[0].message.content
        
def reset_session_state_button():
    if st.button("Reset chat history", type='secondary', key="reset_chat_sentiment"):
        st.session_state["messages"] = [
            {"role": "assistant", "content": "Feel free to copy in content, type or use the example to start."}
        ]
        st.session_state["response"] = None
        st.rerun()  # Rerun the app to refresh the chat display
        
def main():
    st.logo("msi-logo.png")
    render_main_content()
    initialize_session_state()
    display_chat_messages()

    client = OpenAI(api_key=API_KEY, base_url=BASE_URL)
    system_message = {
        "role": "system",
        "content": examples['sentiment']['system_prompt_sentiment']
    }
    handle_user_input(client, system_message)
    reset_session_state_button();
    
if __name__ == "__main__":
    main()