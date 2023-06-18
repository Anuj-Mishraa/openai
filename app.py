# import os
# import openai
# from flask import Flask, render_template, request, jsonify

# app = Flask(__name__)


# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/translate', methods=['POST'])
# def translate():
#     source_language = request.form.get('source_language')
#     target_language = request.form.get('target_language')
#     code = request.form.get('code')

#     prompt = f"##### Translate this function from {source_language} into {target_language}\n### {source_language}\n\n{code}\n### {target_language}"

#     response = openai.Completion.create(
#         model="text-davinci-003",
#         prompt=prompt,
#         temperature=0,
#         max_tokens=150,
#         top_p=1,
#         frequency_penalty=0,
#         presence_penalty=0,
#         stop=["###"]
#     )

#     translated_code = response.choices[0].text.strip()

#     return render_template('translation.html', code=translated_code)

# if __name__ == '__main__':
#     app.run()

import streamlit as st
import openai
import os
openai.api_key = "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"
def translate_code(source_code, source_language, target_language):
    prompt = f"##### Translate this code from {source_language} into {target_language}\n{source_code}\n### {target_language}"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["###"]
    )
    translated_code = response.choices[0].text.strip()
    return translated_code
def main():
    st.title("Programming Language Translator")
    st.subheader("Translate code snippets between different programming languages")

    # Source Language selection
    source_language = st.selectbox("Source Language:", ["Python", "Java", "C"])

    # Target Language selection
    target_language = st.selectbox("Target Language:", ["Haskell", "JavaScript", "C++"])

    # Code input
    code = st.text_area("Code:")

    # Translate button
    if st.button("Translate"):
        translated_code = translate_code(code, source_language, target_language)
        st.code(translated_code, language=target_language)

if __name__ == "__main__":
    main()
