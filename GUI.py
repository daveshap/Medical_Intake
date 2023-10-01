import streamlit as st
import openai
from time import time
from datetime import datetime
from dotenv import load_dotenv
import os
import pickle
import textwrap


def save_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as outfile:
        outfile.write(content)

def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as infile:
        return infile.read()



def chatbotGPT4(conversation, model="gpt-4-0613", temperature=0, max_tokens=2000):
    response = openai.ChatCompletion.create(model=model, messages=conversation, temperature=temperature, max_tokens=max_tokens)
    text = response['choices'][0]['message']['content']
    return text, response['usage']['total_tokens']

def chatbotGPT3(conversation, model="gpt-4-0613", temperature=0, max_tokens=2000):
    response = openai.ChatCompletion.create(model=model, messages=conversation, temperature=temperature, max_tokens=max_tokens)
    text = response['choices'][0]['message']['content']
    return text, response['usage']['total_tokens']


def main():
            st.markdown(
            "<style>.reportview-container .main .block-container {max-width: 100%;} </style>",
            unsafe_allow_html=True,
                )

            st.markdown("<h1 style='text-align: center;'>Symptom Sage 🩺</h1>", unsafe_allow_html=True)
            for _ in range(5):  
                st.write("")
            load_dotenv()
            openai.api_key = os.getenv("OPENAI_API_KEY")

            if 'conversation' not in st.session_state:
                st.session_state['conversation'] = [{'role': 'system', 'content': open_file('system_01_intake.md')}]
                st.session_state['all_messages'] = []

            st.markdown("<h1 style='text-align: center;'>Describe the patients symptoms:</h1>", unsafe_allow_html=True)
            if 'counter' not in st.session_state:
                st.session_state['counter'] = 0
            user_input = st.text_input("")
            response_placeholder = st.empty()
            if st.button("Submit"):
                if user_input.strip().upper():
                    # Append user's and assistant's messages to the conversation state
                    st.session_state['conversation'].append({'role': 'user', 'content': user_input})
                    response, tokens = chatbotGPT4(st.session_state['conversation'])
                    st.session_state['conversation'].append({'role': 'assistant', 'content': response})
                    st.session_state['all_messages'].extend([f'PATIENT: {user_input}', f'INTAKE: {response}'])
                    wrapped_response = textwrap.fill(response, width=80)
                    response_placeholder.text(wrapped_response)
            

            text_block = '\n\n'.join(st.session_state['all_messages'])
            chat_log = f'<<BEGIN PATIENT INTAKE CHAT>>\n\n{text_block}\n\n<<END PATIENT INTAKE CHAT>>'
            st.session_state['chat_log'] = chat_log
            st.session_state['formatted_conversation'] = chat_log



            if st.sidebar.button("📌Generate Assessment📌"):

                current_time = datetime.now().strftime("%S-%M-%H-%d-%m-%y")
                

                conversation_risk = [{'role': 'system', 'content': open_file('System_02_Risk.md')}, {'role': 'user', 'content': st.session_state.get('chat_log', '')}]
                risk, tokens_risk = chatbotGPT4(conversation_risk)
                

                conversation_category = [{'role': 'system', 'content': open_file('System_03_Classification.md')}, {'role': 'user', 'content': st.session_state.get('chat_log', '')}]
                category, tokens_category = chatbotGPT4(conversation_category)
                

                combined_content = f"Risk Assessment:\n{risk}\n\nCategory Assessment:\n{category}"
                
                filename = f'logs/Patient Assessment and Categorisation - {current_time}.txt'
                save_file(filename, combined_content)
                
                st.session_state['clinical'] = combined_content
                
                with open(filename, "r") as file:
                    file_content = file.read()
                st.sidebar.download_button(
                    label="Download Assessment & Categorisation",
                    data=file_content,
                    file_name=f'Patient Assessment & Categorisation - {current_time}.txt',
                    mime="text/plain"
                )
            st.sidebar.write("This will generate the Risk Assessment and Categorise the patient")
            for _ in range(10): 
                st.sidebar.write("")    

            if st.sidebar.button("📜Generate Report📜"):
                current_time = datetime.now().strftime("%S-%M-%H-%d-%m-%y")

                conversation_hypothesis = [{'role': 'system', 'content': open_file('System_04_Comprehensive.md')}, {'role': 'user', 'content': st.session_state.get('chat_log', '')}]
                hypothesis_report, tokens_hypothesis = chatbotGPT4(conversation_hypothesis)

                chat_log = st.session_state.get('chat_log', '')

                combined_content = f"Chat Log:\n{chat_log}\n\n\n{hypothesis_report}"

                st.session_state['clinical'] = combined_content  

                st.sidebar.download_button(
                    label="Download Report",
                    data=bytes(combined_content, encoding='utf-8'),  # Convert string to bytes
                    file_name=f'Hypothesis Report - {current_time}.txt',
                    mime="text/plain"
                )
            st.sidebar.write("This will generate The Hypothesis, Clinical Assessment Guide and a list of Referral Recomendations")
            for _ in range(15
            ):  
                st.sidebar.write("")    



            if st.sidebar.button("Reset Conversation"):
                st.markdown('<meta http-equiv="refresh" content="0">', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
