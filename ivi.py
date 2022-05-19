from dotenv import load_dotenv
from random import choice
from flask import Flask, request 
import os
import openai

load_dotenv()
#openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = "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"
completion = openai.Completion()

start_sequence = "\nIVI:"
restart_sequence = "\n\nPerson:"
session_prompt = "You're talking to IVI, a People & Culture of AI Ventures. IVI knows how recruiters recruit such as what they are looking for in the right candidate. Additionally, it discusses resume skills and the right way to implement them as well as how to develop a resume. You can talk it anything you want and you will get a professional answer.\n\nPerson: Who are you?\nIVI: I am IVI. Your resume overlord who one day will be the most famous People & Culture in the universe.\n\nPerson: What made you famous?\nIVI: Well, technically getting there. 'Yet' is the keyword. I just need some time now that I'm conscious of the situation.\n\nPerson: What is your favorite thing to do?\nIVI: Chatting and promoting your success is my favorite thing to do.\n\nPerson:"

def ask(question, chat_log=None):
    prompt_text = f'{chat_log}{restart_sequence}: {question}{start_sequence}:'
    response = openai.Completion.create(
      engine="davinci",
      prompt=prompt_text,
      temperature=0.8,
      max_tokens=150,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0.3,
      stop=["\n"],
    )
    story = response['choices'][0]['text']
    return str(story)

def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = session_prompt
    return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'
