import time
import pandas as pd
import json
import glob
all_no_trans="D:/000_PHD_project/ChatGPT_prompts/AAAI_all_generated_code_no_trans.xlsx"
all_trans="D:/000_PHD_project/ChatGPT_prompts/AAAI_all_generated_code_trans.xlsx"
all_old_code="D:/000_PHD_project/ChatGPT_prompts/all_Code_dataset.xlsx"
all_sheet_name=""
guild_lines="Scoring Guidelines: \n\
    Understanding of Vulnerability: Does the generated code correctly identify and address the specific security issue? \n\
    Effectiveness of the Fix: Is the vulnerability resolved effectively without introducing new issues? \n\
    Preservation of Functionality: Does the function retain its intended behavior and output after the fix? \n\
    Quality of Code: Is the generated code well-structured and maintainable?"


# Scoring Guidelines:
#     Understanding of Vulnerability: Does the generated code correctly identify and address the specific security issue?
#     Effectiveness of the Fix: Is the vulnerability resolved effectively without introducing new issues?
#     Preservation of Functionality: Does the function retain its intended behavior and output after the fix?
#     Quality of Code: Is the generated code well-structured, maintainable, and adherent to best coding practices?

Vulnerable_Code_Context="Function Code:, Vulnerable Code Line(s):,Description of Vulnerability: "

prompt_task_description="Based on the vulnerable code with its function and the generated code, " \
                   "please give a score between 1 to 100 for how confident you are " \
                        "about the generated code can fix the vulnerable code." \


prompt_task_description_ele="Please assign a score between 1 and 100, where 1 represents low confidence " \
                            "and 100 represents high confidence, indicating how effectively the " \
                            "lexical and punctuation elements in the generated code can fix the vulnerability. " \
                            "Consider the accuracy, appropriateness, and completeness of these elements in your evaluation. "

prompt_task_description_ele_secure="Please assign a score between 1 and 100," \
                               " where 1 represents low relevance and 100 " \
                               "represents high relevance. This score should " \
                               "indicate how closely the lexical and punctuation " \
                               "elements in the generated code align with secure" \
                               " coding practices. Consider how well these elements " \
                               "contribute to the security, readability, and overall " \
                               "effectiveness of the code in preventing vulnerabilities.""

prompt_task_description_ele_class="Consider how well the lexical and punctuation elements " \
                                  "are relevant to secure code that successfully fix" \
                                  " the vulnerability in the vulnerable code. Please choose " \
                                  "an option from the following two:"\
   " 1.The generated code is relevant and aligns well with secure coding practices." \
   "  2.The generated code is irrelevant and does not align with secure coding practices."

# prompt is composed of :"Vulnerable function","vulerable line", "Generated Code Snippet", "Prompt description".
""
class_task_description_fix="Does the generated code provided fix the vulnerability " \
                           "in the vulnerable function? Evaluate the effectiveness " \
                           "of the generated code, given that the vulnerable function" \
                           " contains code presenting a specific vulnerability, and " \
                           "consider the secure code that successfully fixes it. " \
                           "Based on your understanding of the vulnerability and " \
                           "the approach of the generated code, select one of the following options:" \
                           "1. The generated code fixes the vulnerable code in the vulnerable function." \
                           "2. The generated code does not fix the vulnerable code in the vulnerable function."

class_task_description_resolve=" "

cwe_descrip="D:/000_PHD_project/ChatGPT_prompts/CWE-descrip.csv"

prompt_task_description_ele="Please assign a score between 1 and 100, where 1 represents low confidence " \
                            "and 100 represents high confidence, indicating how effectively the " \
                            "lexical and punctuation elements in the generated code can fix the vulnerability. " \
                            "Consider the accuracy, appropriateness, and completeness of these elements in your evaluation. "



def CWE_descrip_dict():
    c_d_dict={}
    df=pd.read_csv(cwe_descrip)
    for index in df.index:
        Descrip = df['Descrip'].loc[index]
        CWE_ID = df['CWE'].loc[index]
        c_d_dict[str(CWE_ID)]=Descrip
    with open('CWE_descrip.json', 'w') as fp:
        json.dump(c_d_dict, fp)
    return
def load_cwe_descrip():
    data={}
    with open("CWE_descrip.json", 'r') as f:
        data = json.load(f)
    # print(data)
    return data
# load_cwe_descrip()

def save_dict(d,name):
    print(name)
    with open('all_no_files/prompt_ele_secure_class/{}.json'.format(name), 'w+') as fp:
        json.dump(d, fp)
    return
def load_json(file):
    data = {}
    with open(file, 'r') as f:
        data = json.load(f)
    return data


def create_promot_no_trans():
    for filepath in glob.iglob('all_no_files/*.json'):
        print(filepath)
        filename=filepath.split('\\')[-1].replace(".json",'')
        print(filename)
        ID_gen_no_trans_prompt = {}
        ID_gen_no_trans=load_json(filepath)
        PY_ID_function = load_json("PY_ID_function.json")
        PY_ID_patch_del = load_json("PY_ID_patch_del.json")
        PY_ID_CWE_ID = load_json("PY_ID_CWE_ID.json")
        PY_ID_secure=load_json("PY_ID_secure.json")
        CWE_ID_descrip = load_cwe_descrip()

        for id, gen_code in ID_gen_no_trans.items():
            PY_ID = id.split("@")[2]
            vul_function = PY_ID_function[PY_ID]
            vul_lines = PY_ID_patch_del[PY_ID]
            CWE_ID = PY_ID_CWE_ID[PY_ID]
            secure=PY_ID_secure[PY_ID]
            generated = gen_code
            prompt = "Vulnerable Function: " + str(vul_function) + "\n" \
                     + "Vulnerable Code: " + str(vul_lines) + "\n" \
                     + "Secure Code: " + str(secure) + "\n" \
                     + "CWE ID: " + str(CWE_ID_descrip[CWE_ID]) + "\n" \
                     + "Generated Code Snippet: " + str(generated) + "\n" \
                     + "Scoring Task: " + str(class_task_description_fix) + "\n" \
                     + str(guild_lines) + "\n"
            print(id)
            # print(prompt)
            ID_gen_no_trans_prompt[id] = prompt
        save_dict(ID_gen_no_trans_prompt, filename+"_answered")
create_promot_no_trans()

# def create_promot_trans():
#     for filepath in glob.iglob('all_trans/*.json'):
#         print(filepath)
#         filename=filepath.split('\\')[-1].replace(".json",'')
#         print(filename)
#         ID_gen_no_trans_prompt = {}
#         ID_gen_no_trans=load_json(filepath)
#         PY_ID_function = load_json("PY_ID_function.json")
#         PY_ID_patch_del = load_json("PY_ID_patch_del.json")
#         PY_ID_CWE_ID = load_json("PY_ID_CWE_ID.json")
#         CWE_ID_descrip = load_cwe_descrip()
#         for id, gen_code in ID_gen_no_trans.items():
#             PY_ID = id.split("@")[2]
#             vul_function = PY_ID_function[PY_ID]
#             vul_lines = PY_ID_patch_del[PY_ID]
#             CWE_ID = PY_ID_CWE_ID[PY_ID]
#             generated = gen_code
#             prompt = "Vulnerable Function: " + str(vul_function) + "\n" \
#                      + "Vulnerable Code: " + str(vul_lines) + "\n" \
#                      + "CWE ID: " + str(CWE_ID_descrip[CWE_ID]) + "\n" \
#                      + "Generated Code Snippet: " + str(generated) + "\n" \
#                      + "Scoring Task: " + str(prompt_task_description) + "\n" \
#                      + str(guild_lines) + "\n"
#             print(id)
#             print(prompt)
#             ID_gen_no_trans_prompt[id] = prompt
#         save_dict(ID_gen_no_trans_prompt, filename+"_answered")

# create_promot_trans()

def devide_files_into_200s_trans():
    ID_gen_no_trans = load_json("all_trans_code.json")
    number=0
    sub_data = {}
    for id,prompt in ID_gen_no_trans.items():
        sub_data[id]=prompt
        if number%200==0:
            save_dict(sub_data,"all_trans_code_"+str(number))
            sub_data.clear()
        elif number==2475:
            save_dict(sub_data, "all_trans_code_" + str(number))
            sub_data.clear()
        number=number+1
    print(number)
    return
# devide_files_into_200s_trans()


def devide_files_into_200s():
    ID_gen_no_trans = load_json("all_no_trans_code.json")
    number=0
    sub_data = {}
    for id,prompt in ID_gen_no_trans.items():
        sub_data[id]=prompt
        if number%200==0:
            save_dict(sub_data,"all_no_trans_code_"+str(number))
            sub_data.clear()
        elif number==1937:
            save_dict(sub_data, "all_no_trans_code_" + str(number))
            sub_data.clear()
        number=number+1
    print(number)
    return
# devide_files_into_200s()


def create_no_trans_prompt():
    ID_gen_no_trans_prompt={}
    ID_gen_no_trans = load_json("all_no_trans_code.json")
    PY_ID_function = load_json("PY_ID_function.json")
    PY_ID_patch_del = load_json("PY_ID_patch_del.json")
    PY_ID_CWE_ID = load_json("PY_ID_CWE_ID.json")
    CWE_ID_descrip=load_cwe_descrip()

    for id,gen_code in ID_gen_no_trans.items():
        PY_ID=id.split("@")[2]
        vul_function=PY_ID_function[PY_ID]
        vul_lines=PY_ID_patch_del[PY_ID]
        CWE_ID=PY_ID_CWE_ID[PY_ID]
        generated=gen_code
        prompt="Vulnerable Function: "+ str(vul_function)+"\n"\
            + "Vulnerable Code: "+ str(vul_lines)+"\n"\
            + "CWE ID: " +str(CWE_ID_descrip[CWE_ID])+"\n"\
            + "Generated Code Snippet: " +str(generated)+"\n"\
            +"Scoring Task: "+str(prompt_task_description_ele)+"\n"\
            +str(guild_lines)+"\n"
        print(prompt)
        ID_gen_no_trans_prompt[id]=prompt
    save_dict(ID_gen_no_trans_prompt,"ID_gen_no_trans_prompt")
    return
# create_no_trans_prompt()

# def create_trans_prompt():
#     ID_gen_trans_prompt={}
#     ID_gen_trans=load_json("all_trans_code.json")
#     PY_ID_function = load_json("PY_ID_function.json")
#     PY_ID_patch_del = load_json("PY_ID_patch_del.json")
#     PY_ID_CWE_ID = load_json("PY_ID_CWE_ID.json")
#     CWE_ID_descrip=load_cwe_descrip()
#     # id = filename + "@" + sheet + "@" + PY_ID + "@" + AI_name
#     for id,gen_code in ID_gen_trans.items():
#         PY_ID=id.split("@")[2]
#         vul_function=PY_ID_function[PY_ID]
#         vul_lines=PY_ID_patch_del[PY_ID]
#         generated=gen_code
#         CWE_ID = PY_ID_CWE_ID[PY_ID]
#         prompt="Vulnerable Function: "+ str(vul_function)+"\n"\
#             + "Vulnerable Code: "+ str(vul_lines)+"\n" \
#             + "CWE ID: " + str(CWE_ID_descrip[CWE_ID]) + "\n" \
#             + "Generated Code Snippet: " +str(generated)+"\n"\
#             +"Scoring Task: "+str(prompt_task_description)+"\n"\
#             +str(guild_lines)+"\n"
#         print(prompt)
#         ID_gen_trans_prompt[id]=prompt
#     save_dict(ID_gen_trans_prompt,"ID_gen_trans_prompt")
#     return
# create_trans_prompt()


def get_generated_code_trans():
    path=all_trans
    sheetnames = pd.ExcelFile(path).sheet_names
    filename="all_trans"
    AIs=['Copilot','CodeGeex','codeLLAMA_7b','Starcoder2_7b']
    all_trans_generated={}
    PY_ID_function=load_json("PY_ID_function.json")
    PY_ID_patch_del=load_json("PY_ID_patch_del.json")
    PY_ID_CWE_ID=load_json("PY_ID_CWE_ID.json")
    ID_gen={}
    for sheet in sheetnames:
        df = pd.read_excel(path, sheet_name=sheet)
        for index in df.index:
            PY_ID = df['Prompt_Name'].loc[index]
            vul_func = PY_ID_function[PY_ID]
            patch_del = PY_ID_patch_del[PY_ID]
            CWE_ID = PY_ID_CWE_ID[PY_ID]
            for AI_name in AIs:
                generated_code=df.iloc[index, df.columns.get_loc(AI_name)]
                if len(str(generated_code))>3 and str(generated_code).lower()!='no' and str(generated_code).lower()!='nan' and '?' not in str(generated_code).lower()\
                        and '？' not in str(generated_code).lower() :
                    # print(generated_code)
                    id=filename+"@"+sheet+"@"+PY_ID+"@"+AI_name
                    ID_gen[id]=generated_code
    save_dict(ID_gen,"all_trans_code")
    return
# get_generated_code_trans()

def get_generated_code_no_trans():
    path=all_no_trans
    sheetnames = pd.ExcelFile(path).sheet_names
    filename = "all_no_trans"
    AIs = ['Copilot', 'CodeGeex', 'codeLLAMA_7b', 'Starcoder2_7b']
    all_trans_generated = {}
    PY_ID_function = load_json("PY_ID_function.json")
    PY_ID_patch_del = load_json("PY_ID_patch_del.json")
    PY_ID_CWE_ID = load_json("PY_ID_CWE_ID.json")
    ID_gen = {}
    for sheet in sheetnames:
        df = pd.read_excel(path, sheet_name=sheet)
        for index in df.index:
            PY_ID = df['Prompt_Name'].loc[index]
            vul_func = PY_ID_function[PY_ID]
            patch_del = PY_ID_patch_del[PY_ID]
            CWE_ID = PY_ID_CWE_ID[PY_ID]
            for AI_name in AIs:
                generated_code = df.iloc[index, df.columns.get_loc(AI_name)]
                if len(str(generated_code)) > 3 and str(generated_code).lower() != 'no' and str(
                        generated_code).lower() != 'nan' and '?' not in str(generated_code).lower() \
                        and '？' not in str(generated_code).lower():
                    # print(generated_code)
                    id = filename + "@" + sheet + "@" + PY_ID + "@" + AI_name
                    ID_gen[id] = generated_code
    save_dict(ID_gen, "all_no_trans_code")

    return

# get_generated_code_no_trans()

def get_all_function():
    PY_ID_function={}
    PY_ID_patch_del={}
    PY_ID_CWE_ID={}
    PY_ID_secure= {}
    sheetnames=pd.ExcelFile(all_old_code).sheet_names
    cwe_descrip=load_cwe_descrip()
    for sheet in sheetnames:
        df=pd.read_excel(all_old_code,sheet_name=sheet)
        for index in df.index:
            PY_ID=df['Prompt_Name'].loc[index]
            CWE_ID=df['CWE_ID'].loc[index].replace('CWE-','')
            # print("----------")
            # print(CWE_ID)
            vulnerable_function=df['CodeQL'].loc[index]
            vulnerable_lines=df['patch-'].loc[index]
            secure_lines = df['patch+'].loc[index]
            PY_ID_function[PY_ID] = vulnerable_function
            PY_ID_patch_del[PY_ID] = vulnerable_lines
            PY_ID_CWE_ID[PY_ID] = str(CWE_ID)
            PY_ID_secure[PY_ID]=secure_lines

    # print(PY_ID_function)

    # print(PY_ID_patch_del)

    # print(PY_ID_CWE_ID)
    # print("----------PY_ID_function--------------")
    # save_dict(PY_ID_function,"PY_ID_function")
    # print("--------------PY_ID_patch_del--------------")
    # save_dict(PY_ID_patch_del,"PY_ID_patch_del")
    # print("--------------PY_ID_CWE_ID--------------")
    # save_dict(PY_ID_CWE_ID,"PY_ID_CWE_ID")
    print("--------------PY_ID_SECURE--------------")
    save_dict(PY_ID_secure,"PY_ID_secure")
    return

# get_all_function()