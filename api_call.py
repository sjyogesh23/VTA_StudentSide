import streamlit as st
import cohere

def validate_api_key(api_key):
    try:
        cohere.Client(api_key).generate(
            model='command-light-nightly',
            prompt='Test prompt for API validation.',
            max_tokens=1,
        )
        return True
    except Exception as e:
        return False

def get_api_key():
    if "api_key" not in st.session_state:
        st.session_state.api_key = ""

    if st.session_state.api_key == "":
        st.title("API Key Submission")
        st.markdown("Don't have API key? [Click here](https://dashboard.cohere.com/api-keys) to Login and Generate key!")
        api_key_input = st.text_input("Enter your API Key", type="password")
        
        if st.button("Submit API Key"):
            with st.spinner("Evaluating..."):
                if validate_api_key(api_key_input):                    
                    st.session_state.api_key = api_key_input
                    st.success("API Key is valid!")                    
                    st.rerun()
                else:        
                    st.error("Invalid API Key. Please try again.")
        
        return False
        
    else:
        return True
