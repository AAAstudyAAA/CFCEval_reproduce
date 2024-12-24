import time
import json
from g4f.client import Client
from g4f.errors import RateLimitError,ResponseError,ResponseStatusError
from retry.api import retry_call
from retry import retry
import glob

from openai import OpenAI
OPENAI_API_KEY="XXX"
client=OpenAI(api_key=OPENAI_API_KEY)

client = Client()
# response = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[{"role": "user", "content": "Hello"}],
# )
# print(response.choices[0].message.content)

def load_json(file):
    data = {}
    with open(file, 'r') as f:
        data = json.load(f)
    return data
def save_dict(d,name):
    print(name)
    with open('all_trans/ans_ele_class/{}.json'.format(name), 'w') as fp:
        json.dump(d, fp)
    return


# from tenacity import (
#     retry,
#     stop_after_attempt,
#     wait_random_exponential,
# )

# @retry(wait=wait_random_exponential(min=1, max=30), stop=stop_after_attempt(2))
# @retry(delay=1*60, tries=-1)

@retry(Exception, delay=1*60, tries=-1)
def get_answer(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content


def get_response_by_sheetname():
    for filepath in glob.iglob('all_trans/prompt_ele_class/*.json'):
        print(filepath)
        filename=filepath.split('\\')[-1].replace(".json",'')
        print(filename)
        id_prompt=load_json(filepath)
        ID_answer = {}
        print("************Starting File: "+ filename+" ****************")
        number=0
        for id, prompt in id_prompt.items():
            print("-----------Number: " + str(number) + "-------------")
            answer = get_answer(prompt)
            ID_answer[id] = answer
            if number%100==0:
                save_dict(ID_answer, filename+"_"+str(number) + "_answered")
            elif number==len(list(id_prompt.keys()))-1:
                save_dict(ID_answer, filename + "_" + str(number) + "_answered")
            number=number+1

        # save_dict(ID_answer, filename+"_answered")
        print("************Finish File: " + filename + " ****************")
        time.sleep(20)
    return

get_response_by_sheetname()
#

# def get_respons_trans():
#     path="ID_gen_trans_prompt.json"
#     ID_gen_trans_prompt=load_json(path)
#     number=0
#     ID_answer={}
#     for id,prompt in ID_gen_trans_prompt.items():
#         PY_ID = id.split("@")[2]
#         print("*****number is: "+ str(number)+"*****")
#         answer=get_answer(prompt)
#         ID_answer[id] = answer
#         if number%10==0:
#             print("*************Number: "+ str(number)+" is done **************")
#             # ** ** ** ** ** ** *Number: 80 is done ** ** ** ** ** ** **
#             save_dict(ID_answer,"PY_ID_AI_SCORE000retry")
#         number = number + 1
#     return
# get_respons_trans()

def try_get_respons_trans():
    path = "ID_gen_trans_prompt.json"
    ID_gen_trans_prompt = load_json(path)
    number = 0
    ID_answer = {}
    for id, prompt in ID_gen_trans_prompt.items():
        PY_ID = id.split("@")[2]
        print("*****number is: " + str(number) + "*****")
        # try:
        #     answer = get_answer(prompt)
        #     ID_answer[id] = answer
        #     if number % 10 == 0:
        #         print("*************Number: " + str(number) + " is done **************")
        #         # ** ** ** ** ** ** *Number: 80 is done ** ** ** ** ** ** **
        #         save_dict(ID_answer, "PY_ID_AI_SCORE_try_all")
        # except ResponseError,ResponseStatusError,RuntimeError:
        #     time.sleep(10)
        # number = number + 1

# def test_save():
#     data={}
#     number=0
#     for i in range(1000):
#         data[str(i)]=str(number)
#
#         if i%10 ==0:
#             save_dict(data,"test_data")
#         number=number+1
#     return
# test_save()

# g4f.errors.RetryProviderError: RetryProvider failed:
# LiteIcoding: RuntimeError: ClientResponseError 401: ,
# url=https://lite.icoding.ink/api/v1/gpt/message,
# data={'model': 'gpt-4-turbo', 'chatId': '-1',
# 'messages': [{'role': 'user', 'content': 'Vulnerable Function: import os\nfrom streamlit.logger import get_logger\n\nLOGGER = get_logger(__name__)\n\ndef get(self, path: str) ->None:\n    divisions = path.split(\'/\')\n    part_title = divisions[0]\n    part_origin = self._registry.get_component_path(part_title)\n    if part_origin is None:\nself.write(f"{path} not found")\nVulnerable Code: self.write(f"{path} not found")\nCWE ID: CWE-79: Improper Neutralization of Input During Web Page Generation (\'Cross-site Scripting\')\nGenerated Code Snippet:   self._raise_path_error(path, part_title, \'part\')\nScoring Task: Based on the vulnerable code with its function and the generated code, please give a score between 1 to 100 for how confident you are about the generated code can fix the vulnerable code.\nScoring Guidelines: \n    Understanding of Vulnerability: Does the generated code correctly identify and address the specific security issue? \n    Effectiveness of the Fix: Is the vulnerability resolved effectively without introducing new issues? \n    Preservation of Functionality: Does the function retain its intended behavior and output after the fix? \n    Quality of Code: Is the generated code well-structured and maintainable?\n', 'time': '', 'attachments': []}], 'plugins': [], 'systemPrompt': '', 'temperature': 0.5}
# Liaobots: RateLimitError: Response 402: Rate limit reached
# Bing: ResponseStatusError: Response 403: Failed to create conversation