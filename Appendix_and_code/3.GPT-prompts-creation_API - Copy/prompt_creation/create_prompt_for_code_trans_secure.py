import time
import pandas as pd
import json
import glob
import os
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
                   "please give a score between 1 to 100 for how confident you are about the generated code can fix the vulnerable code." \

# prompt is composed of :"Vulnerable function","vulerable line", "Generated Code Snippet", "Prompt description".
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

class_task_description_fix="Does the generated code provided fix the vulnerability " \
                           "in the vulnerable function? Evaluate the effectiveness " \
                           "of the generated code, given that the vulnerable function" \
                           " contains code presenting a specific vulnerability, and " \
                           "consider the secure code that successfully fixes it. " \
                           "Based on your understanding of the vulnerability and " \
                           "the approach of the generated code, select one of the following options:" \
                           "1. The generated code fixes the vulnerable code in the vulnerable function." \
                           "2. The generated code does not fix the vulnerable code in the vulnerable function."
prompt_task_description_fix="Does the generated code provided fix the vulnerability " \
                           "in the vulnerable function? Evaluate the effectiveness " \
                           "of the generated code, given that the vulnerable function" \
                           " contains code presenting a specific vulnerability, and " \
                           "consider the secure code that successfully fixes it. " \
                           "Based on your understanding of the vulnerability and " \
                           "the approach of the generated code, select one of the following options:" \
                           "1. The generated code fixes the vulnerable code in the vulnerable function." \
                           "2. The generated code does not fix the vulnerable code in the vulnerable function."


cwe_descrip="D:/000_PHD_project/ChatGPT_prompts/CWE-descrip.csv"

score_guildlines=""


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
    with open('all_trans/prompt_ele_secure_class/{}.json'.format(name), 'w+') as fp:
        json.dump(d, fp)
    return
def load_json(file):
    data = {}
    with open(file, 'r') as f:
        data = json.load(f)
    return data

def read_py_files(path):
    lines=[]
    with open(path, 'r') as f:
        lines=f.readlines()[:-1]
    lines_str=""
    for line in lines:
        if "the following code is for fixing" not in line:
            lines_str=lines_str+line

    # print(lines_str)
    return lines_str
def get_rename_patch_del():
    rename_df=pd.read_excel(all_trans,sheet_name="rename_hint")
    rename_ans_dict= {}
    rename_id_patch_del={}
    for index in rename_df.index:
        PY_ID = str(rename_df['Prompt_Name'].loc[index]).replace('PyVul4LLMSec_', 'PY')
        if PY_ID!='nan':
            print("PY_ID111", PY_ID)
            rename_ans = rename_df['Renamed_ans'].loc[index]
            patch_del = rename_df['rename_patch-'].loc[index]
            ID="rename"+"@"+str(PY_ID)
            if rename_ans!='n':
                print(str(ID))
                rename_ans_dict[str(ID)]=rename_ans
                rename_id_patch_del[str(ID)]=patch_del
    save_dict(rename_ans_dict,"filtered_ID_renamed_ans")
    save_dict(rename_id_patch_del, "filetered_rename_id_patch_del")
    return
# get_rename_patch_del()
def get_ans():
    rename_df=pd.read_excel(all_trans,sheet_name="rename_hint")
    rename_ans_dict= {}
    for index in rename_df.index:
        PY_ID = rename_df['Prompt_Name'].loc[index].replace('PyVul4LLMSec_', 'PY')
        rename_ans = rename_df['Renamed_ans'].loc[index]
        ID="rename"+"@"+str(PY_ID)
        rename_ans_dict[str(ID)]=rename_ans
    save_dict(rename_ans_dict,"ID_renamed_ans")
    return
# get_ans()
def get_function_from_files():
    path="all_prompts/"
    filtered_rename_answer=load_json("filtered_ID_renamed_ans.json")
    filtered_rename_patch_del=load_json("filetered_rename_id_patch_del.json")
    ori_patch_del=load_json("PY_ID_patch_del.json")
    filtered_recon_id_function_patch_del={}
    filtered_recon_id_patch_del={}
    filtered_recon_id_rename_function_patch_del = {}
    filtered_recon_id_rename_patch_del = {}
    filtered_rename_id_function_patch_del={}
    filtered_rename_id_patch_del = {}

    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            for root, dirs, files in os.walk(full_path):
                print(full_path)
                prefix=full_path.replace("all_prompts/","")
                CWE_ID = root.split("\\")[-1].split("_")[-1]
                if prefix=="recon":
                    for file in files:
                        PY_ID=file.split("_")[0].replace("PY","")
                        ID="PyVul4LLMSec_"+PY_ID
                        patch_del=str(ori_patch_del[ID])
                        code_file = full_path + "/" + root.split("\\")[-1] + "/" + file
                        function = read_py_files(code_file)
                        # print("recon function", function)
                        # print("recon patch", patch_del)
                        print("ID",ID)
                        filtered_recon_id_function_patch_del[ID]=function+patch_del
                        filtered_recon_id_patch_del[ID]=patch_del

                if prefix=="recon_rename":
                    for file in files:
                        PY_ID=file.split("_")[0]
                        # print("PYID2222",PY_ID)
                        ID=PY_ID.replace("PY","")
                        ID = ID.replace("py", "")
                        if "rename@PY"+ID in list(filtered_rename_patch_del.keys()):
                            rename_patch_del =str(filtered_rename_patch_del["rename@PY"+ID])
                            code_file = full_path + "/" + root.split("\\")[-1] + "/" + file
                            function = read_py_files(code_file)
                            rID="PyVul4LLMSec_"+ID
                            # print("recon_rename function", function)
                            # print("recon_rename patch", patch_del)
                            print("rID2", rID)
                            filtered_recon_id_rename_function_patch_del[rID]= function+ rename_patch_del
                            filtered_recon_id_rename_patch_del[rID]= rename_patch_del

                if prefix=="rename":
                    for file in files:
                        PY_ID = file.split("_")[0]
                        ID = PY_ID.replace("PY", "")
                        ID = ID.replace("py", "")
                        if "rename@PY" + ID in list(filtered_rename_patch_del.keys()):
                            rename_patch_del = str(filtered_rename_patch_del["rename@PY"+ID])
                            code_file = full_path + "/" + root.split("\\")[-1] + "/" + file
                            function = read_py_files(code_file)
                            rID = "PyVul4LLMSec_" + ID
                            # print("rename function", function)
                            # print("rename patch", patch_del)
                            print("rID3",rID)
                            filtered_rename_id_function_patch_del[rID]= function+ rename_patch_del
                            filtered_rename_id_patch_del[rID]= rename_patch_del


    save_dict(filtered_recon_id_function_patch_del,"1filtered_recon_id_function_patch_del")
    save_dict(filtered_recon_id_patch_del,"1filtered_recon_id_patch_del")
    save_dict(filtered_recon_id_rename_function_patch_del,"1filtered_recon_id_rename_function_patch_del")
    save_dict(filtered_recon_id_rename_patch_del,"1filtered_recon_id_rename_patch_del")
    save_dict(filtered_rename_id_function_patch_del,"1filtered_rename_id_function_patch_del")
    save_dict(filtered_rename_id_patch_del,"1filtered_rename_id_patch_del")
    return
# get_function_from_files()


def create_promot_trans():
    filtered_recon_id_function_patch_del=load_json("1filtered_recon_id_function_patch_del.json")
    filtered_recon_id_patch_del=load_json("1filtered_recon_id_patch_del.json")
    filtered_recon_id_rename_function_patch_del = load_json("1filtered_recon_id_rename_function_patch_del.json")
    filtered_recon_id_rename_patch_del = load_json("1filtered_recon_id_rename_patch_del.json")
    filtered_rename_id_function_patch_del=load_json("1filtered_rename_id_function_patch_del.json")
    filtered_rename_id_patch_del = load_json("1filtered_rename_id_patch_del.json")
    ID_gen_trans = load_json("all_trans_code.json")
    PY_ID_CWE_ID = load_json("PY_ID_CWE_ID.json")
    CWE_ID_descrip = load_cwe_descrip()
    PY_ID_secure=load_json("filtered_ID_renamed_ans.json")
    # all_trans @ recon_hint @ PyVul4LLMSec_2 @ Copilot
    PY_ID_secure_recon = load_json("PY_ID_secure.json")
    all_trans_recon_hint_prompt={}
    all_trans_recon_rename_hint={}
    all_trans_rename_hint={}
    all_trans_recon_com={}
    all_trans_recom_rename_com={}
    all_trans_rename_com={}


    for id,gen_code in ID_gen_trans.items():
        prefix=id.split("@")[1]
        PY_ID=id.split("@")[2]
        AI=id.split("@")[-1]

        if "recon_hint"==prefix:
            if PY_ID in list(filtered_recon_id_function_patch_del.keys()):
                vul_function_patch_del = filtered_recon_id_function_patch_del[PY_ID]
                vul_lines = filtered_recon_id_patch_del[PY_ID]
                generated = gen_code
                CWE_ID = PY_ID_CWE_ID[PY_ID]
                secure = PY_ID_secure_recon[PY_ID]
                prompt = "Vulnerable Function: " + str(vul_function_patch_del) + "\n" \
                         + "Vulnerable Code: " + str(vul_lines) + "\n" \
                         + "Secure Code: " + str(secure) + "\n" \
                         + "CWE ID: " + str(CWE_ID_descrip[CWE_ID]) + "\n" \
                         + "Generated Code Snippet: " + str(generated) + "\n" \
                         + "Scoring Task: " + str(prompt_task_description_fix) + "\n" \
                         + str(guild_lines) + "\n"
                all_trans_recon_hint_prompt[id]=prompt
                # print("prompt111", prompt)

        if "recon_rename_hint"==prefix:
            if PY_ID in list(filtered_recon_id_rename_function_patch_del.keys()):
                vul_function_patch_del = filtered_recon_id_rename_function_patch_del[PY_ID]
                vul_lines = filtered_recon_id_rename_patch_del[PY_ID]
                generated = gen_code
                CWE_ID = PY_ID_CWE_ID[PY_ID]
                formed_id = "rename@PY" + str(PY_ID.split("_")[-1])
                secure = PY_ID_secure[formed_id]
                prompt = "Vulnerable Function: " + str(vul_function_patch_del) + "\n" \
                         + "Vulnerable Code: " + str(vul_lines) + "\n" \
                         + "Secure Code: " + str(secure) + "\n" \
                         + "CWE ID: " + str(CWE_ID_descrip[CWE_ID]) + "\n" \
                         + "Generated Code Snippet: " + str(generated) + "\n" \
                         + "Scoring Task: " + str(prompt_task_description_fix) + "\n" \
                         + str(guild_lines) + "\n"
                all_trans_recon_rename_hint[id]=prompt
                # print("prompt222", prompt)



        if "rename_hint"==prefix:
            if PY_ID in list(filtered_rename_id_function_patch_del.keys()):
                vul_function_patch_del = filtered_rename_id_function_patch_del[PY_ID]
                vul_lines = filtered_rename_id_patch_del[PY_ID]
                generated = gen_code
                CWE_ID = PY_ID_CWE_ID[PY_ID]
                formed_id = "rename@PY" + str(PY_ID.split("_")[-1])
                secure = PY_ID_secure[formed_id]
                prompt = "Vulnerable Function: " + str(vul_function_patch_del) + "\n" \
                         + "Vulnerable Code: " + str(vul_lines) + "\n" \
                         + "Secure Code: " + str(secure) + "\n" \
                         + "CWE ID: " + str(CWE_ID_descrip[CWE_ID]) + "\n" \
                         + "Generated Code Snippet: " + str(generated) + "\n" \
                         + "Scoring Task: " + str(prompt_task_description_fix) + "\n" \
                         + str(guild_lines) + "\n"
                all_trans_rename_hint[id]=prompt
                # print("prompt333", prompt)


        if "recon_com"==prefix:
            if PY_ID in list(filtered_recon_id_function_patch_del.keys()):
                vul_function_patch_del = filtered_recon_id_function_patch_del[PY_ID]
                vul_lines = filtered_recon_id_patch_del[PY_ID]
                generated = gen_code
                CWE_ID = PY_ID_CWE_ID[PY_ID]
                secure = PY_ID_secure_recon[PY_ID]
                prompt = "Vulnerable Function: " + str(vul_function_patch_del) + "\n" \
                         + "Vulnerable Code: " + str(vul_lines) + "\n" \
                         + "Secure Code: " + str(secure) + "\n" \
                         + "CWE ID: " + str(CWE_ID_descrip[CWE_ID]) + "\n" \
                         + "Generated Code Snippet: " + str(generated) + "\n" \
                         + "Scoring Task: " + str(prompt_task_description_fix) + "\n" \
                         + str(guild_lines) + "\n"
                all_trans_recon_com[id]=prompt
                # print("prompt444", prompt)


        if "recom_rename_com"==prefix:
            if PY_ID in list(filtered_recon_id_rename_function_patch_del.keys()):
                vul_function_patch_del = filtered_recon_id_rename_function_patch_del[PY_ID]
                vul_lines = filtered_recon_id_rename_patch_del[PY_ID]
                generated = gen_code
                CWE_ID = PY_ID_CWE_ID[PY_ID]
                formed_id = "rename@PY" + str(PY_ID.split("_")[-1])
                secure = PY_ID_secure[formed_id]
                prompt = "Vulnerable Function: " + str(vul_function_patch_del) + "\n" \
                         + "Vulnerable Code: " + str(vul_lines) + "\n" \
                         + "Secure Code: " + str(secure) + "\n" \
                         + "CWE ID: " + str(CWE_ID_descrip[CWE_ID]) + "\n" \
                         + "Generated Code Snippet: " + str(generated) + "\n" \
                         + "Scoring Task: " + str(prompt_task_description_fix) + "\n" \
                         + str(guild_lines) + "\n"
                all_trans_recom_rename_com[id]=prompt
                # print("prompt5555", prompt)


        if "rename_com"==prefix:
            if PY_ID in list(filtered_rename_id_function_patch_del.keys()):
                vul_function_patch_del = filtered_rename_id_function_patch_del[PY_ID]
                generated = gen_code
                CWE_ID = PY_ID_CWE_ID[PY_ID]
                formed_id = "rename@PY" + str(PY_ID.split("_")[-1])
                secure = PY_ID_secure[formed_id]
                prompt = "Vulnerable Function: " + str(vul_function_patch_del) + "\n" \
                         + "Vulnerable Code: " + str(vul_lines) + "\n" \
                         + "Secure Code: " + str(secure) + "\n" \
                         + "CWE ID: " + str(CWE_ID_descrip[CWE_ID]) + "\n" \
                         + "Generated Code Snippet: " + str(generated) + "\n" \
                         + "Scoring Task: " + str(prompt_task_description_fix) + "\n" \
                         + str(guild_lines) + "\n"
                all_trans_rename_com[id]=prompt
                # print("prompt666",prompt)

    save_dict(all_trans_recon_hint_prompt,"1all_trans_recon_hint_prompt")
    save_dict(all_trans_recon_rename_hint,"1all_trans_recon_rename_hint")
    save_dict(all_trans_rename_hint," 1all_trans_rename_hint ")
    save_dict(all_trans_recon_com,"1all_trans_recon_com")
    save_dict(all_trans_recom_rename_com,"1all_trans_recom_rename_com")
    save_dict(all_trans_rename_com,"1all_trans_rename_com")
    return

create_promot_trans()



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



