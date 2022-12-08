# gsheet_openai_py
Python application to process questions with openAI

## Requirements
This project runs off of python 3.11.0, you can download Python here https://www.python.org/downloads/

## Running the app

After downloading python 3.11 you can check it exists by typing python --version (you should get back the python version 3.11.0)

To run the app simply run

$python3 app.py

And this will cause the app to begin to run (forever) until you stop the app by inputting any key followed by a return (ENTER)

## Environment Variables
This project relies on API keys in order to access Google sheets as well as openAI (https://chat.openai.com/), in order to reference these variables, create a file called .env in the root level of this repo (where this README.md is located) for openAI's API key (instructions here https://beta.openai.com/docs/quickstart/build-your-application)

The .env file should look like

```
OPENAI_API_KEY=yourOpenAIKeyHere
SPREADSHEET_ID=yourSpreadsheetIDHere
```

and you should input your API key after OPENAI_API_KEY= like
OPENAI_API_KEY=abcdmyapikeyhere (no spaces)

also in this repo is an example_env.txt that you can copy and then rename to .env and just replace the values that are there (the final file will just be .env)

## Google Sheets
For the google sheets API you'll need your credentials in a file called credentials.json at the root level of this repo (again, the same directory as this README), for instructions on how to generate this credentials.json file see my website post here (https://mljar.com/blog/authenticate-python-google-sheets-service-account-json-credentials/)


