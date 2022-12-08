from __future__ import print_function
import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account

# environment imports
import os
from dotenv import load_dotenv
load_dotenv()

spreadsheet_id = os.getenv("SPREADSHEET_ID")
creds = service_account.Credentials.from_service_account_file("credentials.json")

# openai imports 
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

from datetime import datetime

# for threads
from threading import Thread
import time

thread_running = True

# functions
def get_values(spreadsheet_id, range_name):
    try:
        service = build('sheets', 'v4', credentials=creds)

        result = service.spreadsheets().values().get(
            spreadsheetId=spreadsheet_id, range=range_name).execute()
        rows = result.get('values', [])
        print(f"{len(rows)} rows retrieved")

        new_list = []
        if len(rows) > 0:
          for row in rows:
            print(row)
            new_list.append(row[0].strip())
        else:
          # single prompt
          print("no questions detected")

        return new_list
        # return result
    except HttpError as error:
        print(f"An error occurred: {error}")
        return error


def openai_response(input_prompt):
  response = openai.Completion.create(
    model="text-davinci-002",
    prompt=input_prompt,
    temperature=0.7,
    )
  return response.choices[0].text

def my_forever_while():
    global thread_running

    start_time = time.time()

    # run this while there is no input
    while thread_running:
        time.sleep(0.1)

        if time.time() - start_time >= 5:
            start_time = time.time()
            print('Another 5 seconds has passed') 
            
            current_time = datetime.now()
            
            # so first need to get all of the values/questions
            questions_list = get_values(spreadsheet_id, "A2:A100")

            print("length of questions list is ")
            print(str(len(questions_list)))

            # read the number of questions asked and stop
            # if no new questions
            fileread = open("questions_asked.txt", "r")
            questions_asked_already = fileread.read()
            fileread.close()

            print("questions asked already is " + questions_asked_already)
            #questions_asked_total = int(questions_asked_already) + len(questions_list)

            if len(questions_list) <= int(questions_asked_already):
              print("already asked all questions")
              print("the current time is ", current_time)

            else:
                # write the number of questions asked
                filewrite = open('questions_asked.txt', 'w')
                filewrite.write(str(len(questions_list)))
                filewrite.close()



                for question in questions_list:
                  print(question)


                start_range = "B2"
                end_range = ""

                end_range = len(questions_list) + 1

                update_range = "{}:B{}".format(start_range, end_range)

                answer_list = []

                # call openAI API for each question
                for question in questions_list:
                  ai_response = openai_response(question)
                  ai_response_no_newline = ai_response.replace("\n", "")
                  answer_list.append([[ai_response_no_newline.strip()]])
                

                print(answer_list)

                # use the credentials.json file
                service = build('sheets', 'v4', credentials=creds)

                # update the google sheet
                # first get the proper format of data
                data_list = []
                count = 2
                for answer in answer_list:
                  temp_dict = {}
                  temp_dict['range'] = 'Sheet1!B{}'.format(str(count))
                  temp_dict['values'] = answer
                  count = count + 1

                  data_list.append(temp_dict)

                # update sheet API call
                batch_update_values_request_body = {
                    "valueInputOption": "RAW",
                    "data": data_list
                }
                service.spreadsheets().values().batchUpdate(
                spreadsheetId=spreadsheet_id, 
                body=batch_update_values_request_body
                ).execute()
            
def take_input():
    user_input = input('Press a key to stop the script: ')
    # doing something with the input
    print('Press a key to stop the script: ', user_input)


if __name__ == '__main__':
    t1 = Thread(target=my_forever_while)
    t2 = Thread(target=take_input)

    t1.start()
    t2.start()

    t2.join()  # interpreter will wait until your process get completed or terminated
    thread_running = False
    print('The end')

