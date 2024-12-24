import os
import time
from os import listdir
from rename import transform_v2
from shutil import copy
# directory = 'D:/security_project/prompts/py_prompts/4_function_level_re/renamed2--use--this--one/'
notworking=['200&2_CVE-2022-0577.py','200&CVE-2022-21683.py','200&CVE-2022-21683.py',
            '200&CVE-2022-21683.py']
directory ='D:/security_project/prompts/py_prompts/4_function_level_re/renamed3/to_rename/'




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
            print(py_file)
            print(p_file)
            # print(os.path.isfile(py_file))
            filename=py_file.split("/")[-1]
            print(filename)
            if 'renamed.py' not in filename and 'renamed_bot.py' not in filename \
                    and 'renamed_hint.py' not in filename:
                rename='{}_renamed.py'.format(p_file)
                # renamed_file=os.path.join(sub_dir, rename)
                renamed_file=sub_dir+rename
                rename_bot='{}_renamed_bot.py'.format(p_file)
                renamed_bot_file=sub_dir+rename_bot
                # renamed_file_bot=os.path.join(sub_dir, rename_bot)
                rename_hint='{}_renamed_hint.py'.format(p_file)
                renamed_hint_file=sub_dir+rename_hint
                # renamed_file_bot=os.path.join(sub_dir, rename_hint)
                print("--------renamed_file---------")
                # print(os.path.isfile(renamed_file))
                # if os.path.isfile(renamed_file):
                #     os.remove(renamed_file)
                if os.path.isfile(rename_bot)==False:
                    copy(rename, rename_bot)
                else:
                    print(rename_bot+" already exists")
                if os.path.isfile(rename_hint)==False:
                    copy(rename,rename_hint)
                else:
                    print(rename_hint+" already exists")
iterating()