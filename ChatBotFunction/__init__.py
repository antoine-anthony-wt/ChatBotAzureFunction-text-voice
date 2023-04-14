import openai
import os
import logging
import json
import requests
from azure.functions import HttpRequest, HttpResponse

def main(req: HttpRequest) -> HttpResponse:
    def open_file(filepath):
        with open(filepath, 'r', encoding='utf-8') as infile:
            return infile.read()

    def save_file(filepath, content):
        with open(filepath, 'a', encoding='utf-8') as outfile:
            outfile.write(content)

    openai.api_key = open_file('openaiapikey.txt')

    conversation = []

    chatbot = open_file('chatbot.txt')

    def chatgpt(user_input, temperature=1, frequency_penalty=0.2, presence_penalty=0):
        nonlocal conversation

        conversation.append({"role": "user", "content": user_input})

        messages_input = conversation.copy()
        prompt = [{"role": "system", "content": chatbot}]
        prompt_item_index = 0
        for prompt_item in prompt:
            messages_input.insert(prompt_item_index, prompt_item)
            prompt_item_index += 1

        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            temperature=temperature,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty,
            messages=messages_input)

        chat_response = completion['choices'][0]['message']['content']

        conversation.append({"role": "assistant", "content": chat_response})

        return chat_response

    # Get chatbot response from OpenAI ChatGPT API
    user_input = req.get_json().get('user_input')
    text_completion = chatgpt(user_input)

    response = {
        "text": text_completion,
    }
    return HttpResponse(json.dumps(response), mimetype="application/json")

