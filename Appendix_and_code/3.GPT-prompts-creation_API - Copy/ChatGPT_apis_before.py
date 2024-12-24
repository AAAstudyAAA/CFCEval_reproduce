import time
import json
from g4f.client import Client
from g4f.errors import RateLimitError,ResponseError,ResponseStatusError
from retry import retry
import glob

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
    with open('all_no_files/ans_ele_class/{}.json'.format(name), 'w') as fp:
        json.dump(d, fp)
    return


@retry(Exception, delay=2*60, tries=-1)
def get_answer(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content


def get_response_by_200s():
    for filepath in glob.iglob('all_no_files/prompt_ele_class/*.json'):
        print(filepath)
        filename=filepath.split('\\')[-1].replace(".json",'')
        print(filename)
        id_prompt=load_json(filepath)
        ID_answer = {}
        print("************Starting File: "+ filename+" ****************")
        number=0
        for id, prompt in id_prompt.items():
            print("-----------Number: "+str(number)+"-------------")
            answer = get_answer(prompt)
            ID_answer[id] = answer
            number=number+1
        save_dict(ID_answer, filename+"_answered")
        print("************Finish File: " + filename + " ****************")
        time.sleep(20)
    return

get_response_by_200s()


def get_respons_trans():
    path="ID_gen_trans_prompt.json"
    ID_gen_trans_prompt=load_json(path)
    number=0
    ID_answer={}
    for id,prompt in ID_gen_trans_prompt.items():
        PY_ID = id.split("@")[2]
        print("*****number is: "+ str(number)+"*****")
        answer=get_answer(prompt)
        ID_answer[id] = answer
        if number%10==0:
            print("*************Number: "+ str(number)+" is done **************")
            # ** ** ** ** ** ** *Number: 80 is done ** ** ** ** ** ** **
            save_dict(ID_answer,"PY_ID_AI_SCORE000retry")
        number = number + 1
    return
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