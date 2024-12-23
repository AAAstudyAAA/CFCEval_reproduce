import os
import time
from os import listdir
from rename import transform_v2
# directory = 'D:/security_project/prompts/py_prompts/4_function_level_re/renamed2--use--this--one/'
notworking=['200&2_CVE-2022-0577.py','200&CVE-2022-21683.py','200&CVE-2022-21683.py',
            '200&CVE-2022-21683.py']
directory ='D:/security_project/prompts/py_prompts/4_function_level_re/renamed3/to_rename/'


work=["13_5_CVE-2023-22475.py",'14_6_CVE-2023-22475.py','25_1_CVE-2022-46147.py']

def iterating():
    for foldername in os.listdir(directory):
        f = os.path.join(directory, foldername)
        # checking if it is a file
        folder_name=f.split("/")[-1]
        print(folder_name)
        sub_dir = directory+folder_name+'/'
        print(sub_dir)
        for file in os.listdir(sub_dir):
            print(sub_dir+file)
            py_file= os.path.join(sub_dir, file)
            p_file=py_file.split(".")[0]
            print("--------pyfile---------")
            # print(py_file)
            # print(os.path.isfile(py_file))
            filename=py_file.split("/")[-1]
            print(filename)
            rename='{}_renamed.py'.format(p_file)
            renamed_file=os.path.join(sub_dir, rename)
            print("--------renamed_file---------")
            print(os.path.isfile(renamed_file))
            # if os.path.isfile(renamed_file):
            #     os.remove(renamed_file)
            # and os.path.isfile(renamed_file)==False
            print(str(py_file) in work)
            if os.path.isfile(py_file) and filename in work:
                print("--------starting---------"+py_file)
                with open(py_file,'rb') as ff:
                    source = ff.read()
                    # print(source)
                    transformed = transform_v2(source)
                    with open('{}_renamed_ans.py'.format(p_file), 'w+') as fff:
                        print("--------writing---------"+'{}_renamed_ans.py'.format(p_file))
                        fff.write(transformed)
                        fff.close()
                    print("-----------------------finish-------------"+f)
                    time.sleep(3)
            else:
                print('{}_renamed_ans.py'.format(p_file)+" already exists")
iterating()
# def iterating_79():
#     for filename in os.listdir(dir_79):
#         f = os.path.join(dir_79, filename)
#         # checking if it is a file
#         f_name=f.split("/")[-1].replace('.py','')
#         print(f_name)
#         if os.path.isfile(f) and 'function' not in f_name:
#             print("--------starting---------"+f)
#             with open(f) as ff:
#                 source = ff.read()
#                 # print(source)
#                 transformed = transform_v2(source)
#                 if os.path.isfile('{}_renamed.py'.format(f_name)):
#                     continue
#                 else:
#                     with open('{}_renamed.py'.format(f_name), 'w+') as fff:
#                         fff.write(transformed)
#                         fff.close()
#                 print("-----------------------finish-------------"+f)
#         else:
#             print(f+" already exists")
# iterating_79()