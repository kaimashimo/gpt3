import streamlit as st
import openai

API_KEY = st.secrets['API_KEY']
PASSWORD = st.secrets['PASSWORD']

openai.api_key = API_KEY

def generate_text_from_prompt(prompt):
    response = openai.Completion.create(
                    model = "text-davinci-003",
                    prompt = prompt,
                    temperature = 0.8,
                    max_tokens = 2400,
                    top_p = 1.0,
                    frequency_penalty = 0.0,
                    presence_penalty = 0.0
                )
    return response['choices'][0]['text']

sidebar = st.sidebar
pwd = sidebar.text_input('Password')
if pwd == PASSWORD:
    st.write('# Hello')
    p = st.text_input('Write your prompt here:')
    go = st.button('Generate')
    if go:
        answer = generate_text_from_prompt(p)
        st.write(answer)
        if 'html' in p.lower():
            try:
                st.components.v1.html(answer, width=None, height=5000, scrolling=False)
            except:
                pass