import streamlit as st
import os
import openai
openai.api_key = "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"


def translate_code(code, source_language, target_language):
    prompt = f"Translate this code from {source_language} to {target_language}:\n\n{code}"
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        temperature=0.3,
        top_p=1.0,
        n=1,
        stop=None,
        log_level="info"
    )
    
    translated_code = response.choices[0].text.strip()
    
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