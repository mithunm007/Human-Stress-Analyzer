from agent import tips
import streamlit as st

def stress_level(level):
    
    try:
        st.divider()
        st.subheader("here are some tips ✨")
        with st.spinner('Loading...'):
            response = tips(level)
            st.info(response)
    except:
        st.info("sorry tips cannot be generated now!")