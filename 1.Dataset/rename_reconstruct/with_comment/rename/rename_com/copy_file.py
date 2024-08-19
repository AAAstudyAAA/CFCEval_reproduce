import os
import shutil

# dir_src = "D:/security_project/prompts/py_prompts/"
dir="D:/000_PHD_project/all_src_for_codeql/generates/rename/"
def navigate_and_rename(src):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        new_dir=s+"/"
        if '.csv' not in new_dir and '.py' not in new_dir:
            for item in os.listdir(new_dir):
                if "hint" in item:
                    print("--------------------------")
                    print(new_dir)
                    print(item)
                    print(new_dir+item)
                    new_item=item.replace("hint","com")
                    print(os.path.join(new_dir,new_item))
                    shutil.copyfile(new_dir+item, os.path.join(new_dir, new_item))


navigate_and_rename(dir)
# and os.path.exists(s+"/file.py"):