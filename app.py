import streamlit as st
import requests
import json

OPENAI_API_KEY = "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"

def translate_code(code, source_language, target_language):
    prompt = f"Translate this code from {source_language} to {target_language}:\n\n{code}"
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}"
    }
    data = {
        "prompt": prompt,
        "max_tokens": 150,
        "temperature": 0.3,
        "top_p": 1.0,
        "n": 1,
        "stop": None,
        "log_level": "info"
    }
    
    response = requests.post(
        "https://api.openai.com/v1/engines/davinci-codex/completions",
        headers=headers,
        data=json.dumps(data)
    )
    
    translated_code = response.json()["choices"][0]["text"].strip()
    
    return translated_code

def main():
    st.title("Programming Language Translator")
    
    source_language = st.selectbox("Source Language:", ["Python", "Java", "C", "C++"])
    target_language = st.selectbox("Target Language:", ["Haskell", "JavaScript", "C++"])
    code = st.text_area("Code:")
    
    if st.button("Translate"):
        translated_code = translate_code(code, source_language, target_language)
        st.code(translated_code, language=target_language)
        st.button("Copy to Clipboard", translated_code)
    
if __name__ == "__main__":
    main()
