fileopen = open("Data\Audio\Api.txt","r")
api = fileopen.read()
fileopen.close()


import openai
from dotenv import load_dotenv

openai.api_key = api
load_dotenv()
completion = openai.Completion()


def QuestionsAnswer(question, chat_log = None):
    Filelog = open("DataBase\qna_log.txt","r")
    chat_log_template = Filelog.read()
    Filelog.close()

    if chat_log is None:
        chat_log = chat_log_template

    prompt = f'{chat_log}Question: {question}\n Answer: '
    response = completion.create(
        model = "text-davinci-002",
        prompt=prompt,
        temperature = 0,
        max_tokens = 100,
        top_p = 1,
        frequency_penalty = 0.5,
        presence_penalty = 0)    
    answer = response.choices[0].text.strip()
    chat_log_template_update = chat_log_template + f"\nYou : {question} \nEternity 154X : {answer}"
    Filelog = open("DataBase\qna_log.txt","w")
    Filelog.write(chat_log_template_update)
    Filelog.close
    return answer               



