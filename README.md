# gsheet_openai_py
Python application to process questions with openAI

## Environment Variables
This project relies on API keys in order to access Google sheets as well as openAI (https://chat.openai.com/), in order to reference these variables, create a file called .env in the root level of this repo (where this README.md is located) for openAI's API key (instructions here https://beta.openai.com/docs/quickstart/build-your-application)

The .env file should look like

```
FLASK_APP=app
FLASK_ENV=development
OPENAI_API_KEY=
```

and you should input your API key after OPENAI_API_KEY= like
OPENAI_API_KEY=abcdmyapikeyhere

For the google sheets API you'll need your credentials in a file called credentials.json at the root level of this repo (again, the same directory as this README), for instructions on how to generate this credentials.json file see https://developers.google.com/sheets/api/quickstart/python
