Chatbot App with Azure Functions
================================

This project is a Chatbot App using Azure Functions, OpenAI, and Eleven Labs APIs to handle both text and voice chat interactions.

Requirements
------------

-   Python 3.6 or higher
-   [Azure Functions Core Tools](https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=windows%2Ccsharp%2Cbash#install-the-azure-functions-core-tools) (version 3.x)

Project Structure
-----------------

javascriptCopy code

`.
├── ChatBotFunction
│   ├── __init__.py
│   └── function.json
├── ChatVoiceFunction
│   ├── __init__.py
│   └── function.json
├── getting_started_with_azure_functions.md
├── requirements.txt
├── openaiapikey.txt
├── elevenlabsapikey.txt
└── chatbot.txt`

### Function Folders

-   `ChatBotFunction`: Azure Function for handling text chat interactions with the chatbot.
-   `ChatVoiceFunction`: Azure Function for handling voice chat interactions with the chatbot.

### Files

-   `getting_started_with_azure_functions.md`: Instructions on setting up Azure Functions.
-   `requirements.txt`: Required Python packages for the project.
-   `openaiapikey.txt`: Place your OpenAI API key here.
-   `elevenlabsapikey.txt`: Place your Eleven Labs API key here.
-   `chatbot.txt`: Instructions for the chatbot behavior.

Setup
-----

1.  Install the required Python packages by running:

shCopy code

`pip install -r requirements.txt`

1.  Add your OpenAI API key to the `openaiapikey.txt` file.
2.  Add your Eleven Labs API key to the `elevenlabsapikey.txt` file.

Running the Functions Locally
-----------------------------

1.  Start the Azure Functions Core Tools by running:

shCopy code

`func start`

1.  Test the `ChatBotFunction` by sending a POST request to `http://localhost:7071/api/ChatBotFunction` with a JSON payload containing the `user_input` key. For example:

jsonCopy code

`{
  "user_input": "Tell me a joke."
}`

1.  Test the `ChatVoiceFunction` by sending a POST request to `http://localhost:7071/api/ChatVoiceFunction` with a JSON payload containing the `text_completion` key. For example:

jsonCopy code

`{
  "text_completion": "This is a test text for the chatbot."
}`

Deploying to Azure
------------------

Follow the instructions in `getting_started_with_azure_functions.md` to deploy your functions to Azure.

Usage
-----

-   `ChatBotFunction`: Send a POST request with a JSON payload containing the `user_input` key to interact with the text chatbot.
-   `ChatVoiceFunction`: Send a POST request with a JSON payload containing the `text_completion` key to get the voice response for the given text.

Contributing
------------

If you'd like to contribute, please submit a pull request with your changes or bug fixes.