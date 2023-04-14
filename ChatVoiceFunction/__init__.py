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
 
    elapikey = open_file('elevenlabsapikey.txt')

    def get_voice(text):
        url = 'replace with your Eleven Labs Voice URL'
        headers = {
            'accept': 'audio/mpeg',
            'xi-api-key': elapikey,
            'Content-Type': 'application/json'
        }
        data = {
            'text': text,
            'voice_settings': {
                'stability': 0.6,
                'similarity_boost': 0.85
            }
        }
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            return response.content
        else:
            return None

    # Get voice as MP3 bytes from ElevenLabs API
    text_completion = req.get_json().get('text_completion')
    voice_mp3 = get_voice(text_completion)

    if voice_mp3 is not None:
        # Return the text completion and voice as a JSON object
        response = {
            "voice": voice_mp3.decode('ISO-8859-1')
        }
        return HttpResponse(json.dumps(response), mimetype="application/json")
    else:
        response = {
            "voice": None
        }
        return HttpResponse(json.dumps({"response": response}), mimetype="application/json")

