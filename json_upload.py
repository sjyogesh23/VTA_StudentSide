import streamlit as st
import json
import base64

def decode_base64_data(encoded_data):
    try:
        return base64.b64decode(encoded_data)
    except Exception as e:
        st.error(f"Error decoding base64 data: {e}")
        return None

def upload_file():
    st.title("Upload VTA file from Creator side")
    uploaded_file = st.file_uploader("Don't have the file? [Click here](https://sjy-video-tutor-assist-creator-side.streamlit.app/) and create the content!", type=["json"])
    if uploaded_file is not None:
        try:
            content = uploaded_file.read()
            decoded_content = content.decode('utf-8')
            data = json.loads(decoded_content)
            st.session_state.data_json = data
            st.success("File uploaded!")
            return True
        except UnicodeDecodeError as e:
            st.error(f"Error decoding the uploaded file: {e}")
            return False
        except json.JSONDecodeError as e:
            st.error(f"Error parsing JSON: {e}")
            return False
    return False
