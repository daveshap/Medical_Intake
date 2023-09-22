import re
import openai
from time import time, sleep
from halo import Halo
import textwrap
import yaml


###     file operations


def save_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as outfile:
        outfile.write(content)



def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as infile:
        return infile.read()


###     API functions


def chatbot(conversation, model="gpt-4-0613", temperature=0, max_tokens=2000):
    max_retry = 7
    retry = 0
    while True:
        try:
            spinner = Halo(text='Thinking...', spinner='dots')
            spinner.start()
            
            response = openai.ChatCompletion.create(model=model, messages=conversation, temperature=temperature, max_tokens=max_tokens)
            text = response['choices'][0]['message']['content']

            spinner.stop()
            
            return text, response['usage']['total_tokens']
        except Exception as oops:
            print(f'\n\nError communicating with OpenAI: "{oops}"')
            exit(5)


def chat_print(text):
    formatted_lines = [textwrap.fill(line, width=120, initial_indent='    ', subsequent_indent='    ') for line in text.split('\n')]
    formatted_text = '\n'.join(formatted_lines)
    print('\n\n\nCHATBOT:\n\n%s' % formatted_text)


if __name__ == '__main__':
    openai.api_key = open_file('key_openai.txt').strip()
    
    conversation = list()
    conversation.append({'role': 'system', 'content': open_file('system_01_intake.txt')})
    user_messages = list()
    all_messages = list()
    print('Describe your symptoms to the intake bot. Type DONE when done.')
    
    ## INTAKE PORTION
    
    while True:
        # get user input
        text = input('\n\nUSER: ').strip()
        if text == 'DONE':
            break
        user_messages.append(text)
        all_messages.append('PATIENT: %s' % text)
        conversation.append({'role': 'user', 'content': text})
        response = chatbot(conversation)
        conversation.append({'role': 'assistant', 'content': response})
        all_messages.append('INTAKE: %s' % response)
    
    ## CHARTING NOTES
    
    print('\n\nGenerating notes...')
    conversation = list()
    conversation.append({'role': 'system', 'content': open_file('system_02_prepare_notes.txt')})
    text_block = '\n\n'.join(all_messages)
    chat_log = '<<BEGIN PATIENT INTAKE CHAT>>\n\n%s\n\n<<END PATIENT INTAKE CHAT>>' % text_block
    conversation.append({'role': 'user', 'content': chat_log})
    notes = chatbot(conversation)
    print('\n\nNotes version of conversation:\n\n%s' % notes)
    
    ## GENERATING REPORT

    print('\n\nGenerating report...')
    conversation = list()
    conversation.append({'role': 'system', 'content': open_file('system_03_diagnosis.txt')})
    conversation.append({'role': 'user', 'content': notes})
    report = chatbot(conversation)
    print('\n\nPhysician Report:\n\n%s' % report)
