import streamlit as st
from agent import tips

import streamlit as st
from agent import tips

def ai():
    st.title("Stress Bot")
    st.subheader("Hello! how can i help you...")

  # Initialize session state for conversation history
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    prompt = st.chat_input("Say something")

    if prompt:
      # Update conversation history
        with st.spinner('Loading...'):
            st.session_state.chat_history.append({"user": prompt, "response": tips(prompt + ".give a small answer of about 3 or 5 lines, answer the questions only if they are related to stress.")})
      
      # Create a container with scroll functionality
        chat_container = st.container()
        with chat_container:
            for message in st.session_state.chat_history:
                st.write(f"**You:** {message['user']}")
                st.info(f"**AI:** {message['response']}")
                st.write("---")

          # Clear the chat input field
        st.empty()

    

    