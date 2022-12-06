import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

# test prompt to make sure it's working
prompt_test = "who is president?"

response = openai.Completion.create(
  model="text-davinci-002",
  prompt=prompt_test,
  temperature=0.7,
  )

print("response is " + response.choices[0].text)

