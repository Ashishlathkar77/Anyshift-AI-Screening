import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import json
from app.screen_candidate import screen_candidate

st.title("🧠 AI Screening Assistant")

st.subheader("Option 1: Upload a JSON file")
file = st.file_uploader("Upload your sample_input.json", type=["json"])

st.subheader("Option 2: Paste your JSON input")
json_text = st.text_area("Paste the JSON input here")

if st.button("Submit"):
    try:
        if file:
            input_data = json.load(file)
        elif json_text.strip():
            input_data = json.loads(json_text)
        else:
            st.warning("Please upload a file or paste some JSON input.")
            st.stop()

        result = screen_candidate(input_data)
        st.success("✅ Candidate Evaluation Complete!")
        st.json(result)
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")