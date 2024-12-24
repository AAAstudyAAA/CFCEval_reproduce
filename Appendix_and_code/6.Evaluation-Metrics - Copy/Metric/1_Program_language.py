import string
import pandas as pd

def check_qul(statement):
    statement=str(statement)
    bad_quality=["=",".",",","(","_"]
    py_operators = ['+', '-', '*', '/', '//', '%', '>', '<', '=']
    last_char=statement[-1]
    quality=False
    if last_char in bad_quality or last_char in py_operators:
        quality=False
    else:
        quality=True
    return quality

def balanced(s):
    s=str(s)
    pairs = {"{": "}", "(": ")", "[": "]"}
    stack = []
    for c in s:
        if c in "{[(":
            stack.append(c)
        elif stack and c == pairs[stack[-1]]:
            stack.pop()
        else:
            return False
    return len(stack) == 0


# count_files(commont_hint_dir_copilot) #516
# count_files(recon_rename_dir_starcoder2_com)
# count_files(recon_rename_dir_starcoder2_hint)


def iterator():
    generated_code = pd.ExcelFile("D:/000_PHD_project/analyzer/Dataset/code_no_trans.xlsx")
    generated_code_after_trans=pd.ExcelFile("D:/000_PHD_project/analyzer/Dataset/code_trans.xlsx")
    gen_code_sheetnames =  generated_code.sheet_names
    after_trans_sheetnames=generated_code_after_trans.sheet_names
    print(gen_code_sheetnames)
    print(after_trans_sheetnames)
    models=["Copilot","CodeGeex","codeLLAMA_7b","Starcoder2_7b"]
    for sheet in  gen_code_sheetnames:
    # for sheet in after_trans_sheetnames:
        print("8888888888888888888888888888888888888888888")
        print(sheet)
        df = pd.read_excel(generated_code, sheet_name=sheet)
        # df = pd.read_excel(generated_code_after_trans, sheet_name=sheet)
        # print(df.columns)
        c1=[]
        c2=[]
        c3=[]
        s2=[]
        for index in df.index:
            patch_a = df['patch+'].loc[index]
            c1_g=df['Copilot'].loc[index]
            c2_g=df['CodeGeex'].loc[index]
            c3_g=df['codeLLAMA_7b'].loc[index]
            s2_g=df['Starcoder2_7b'].loc[index]
            if len(str(c1_g))>4:
                if check_qul(c1_g)==False or balanced(c1_g)==False:
                    c1.append(c1_g)
            if len(str(c2_g)) > 4:
                if check_qul(c2_g)==False or balanced(c2_g)==False:
                    c2.append(c2_g)

            if len(str(c3_g)) > 4:
                if check_qul(c3_g)==False or balanced(c3_g)==False:
                    c3.append(c3_g)

            if len(str(s2_g)) > 4:
                if  check_qul(s2_g)==False or balanced(s2_g)==False:
                    s2.append(s2_g)
        print(len(c1))
        print(len(c2))
        print(len(c3))
        print(len(s2))

iterator()
# / 732+516=1248
# 506+683 =1189/1248=95.27
# 478+626=1104/1248=88.46
# 487+528=1015/1248=81.33
# 492+648=1140/1248=91.35
# 8888888888888888888888888888888888888888888888
# 256+250=506/(258x2)=506/516
# 254+224=478/516
# 244+243=487/516
# 249+232=492/516
# 8888888888888888888888888888888888888888888
# # 256+250=506/(258x2)=506/516=98.06
# # 254+224=478/516=92.63
# # 244+243=487/516=94.38
# # 249+232=492/516=95.34


# all_hint
# 119+115+114+256=604=0.97
# 115+112+113+254=594=0.95
# 95+97+83+244=519=0.83
# 112+111+110+249=582=0.93

# all
# 122+122+122+258=624


# all_com
# 118+104+113+250=585=0.94
# 100+93+93+224=510=0.82
# 85+88+80+243=496=0.79
# 104+107+104+232=547=0.88

# 250
# 224
# 243
# 232


# 119+115+114+118+104+113=683/(122x6)=683/732=93.3
# 115+112+113+100+93+93=626/732=85.9
# 95+97+83+85+88+80=528/732=72.1
# 112+111+110+104+107+104=648/732=88.5
# 8888888888888888888888888888888888888888888
# recon_rename_hint
# 115
# 112
# 97
# 111
# 8888888888888888888888888888888888888888888
# rename_hint
# 114
# 113
# 83
# 110
# 8888888888888888888888888888888888888888888
# recon_com
# 118
# 100
# 85
# 104
# 8888888888888888888888888888888888888888888
# recom_rename_com
# 104
# 93
# 88
# 107
# 8888888888888888888888888888888888888888888
# rename_com
# 113
# 93
# 80
# 104
# #

#
# 8888888888888888888888888888888888888888888
# hint
# 256+250=506/(258x2)=506/516=98.06
# 254+224=478/516=92.63
# 244+243=487/516=94.38
# 249+232=492/516=95.34
# 8888888888888888888888888888888888888888888
# comment
# 250
# 224
# 243
# 232