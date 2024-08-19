from wordnetReplacer import  replacer_final
import ast
import astor
import inspect
import astunparse


import keyword
print(keyword.kwlist)
reservd_keywors=keyword.kwlist
datatypes=['str','int','float','complext','list',
           'tuple','range','dict','set','frozenset','bool',
           'bytes','bytearray','memoryview','NoneType']
all_res=reservd_keywors+datatypes

def transform(source):
    root = ast.parse(source)
    unchanged=[]+all_res
    renamed={}
    assigned=[]
    for node in ast.walk(root):
        unchanged.append('self')
        if isinstance(node, ast.Import):
            if len(node.names)!=0:
                for ali in node.names:
                    unchanged.append(ali.name)
                    if ali.asname!=None:
                        unchanged.append(ali.asname)
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name):
                unchanged.append(node.func.id)
            if isinstance(node.func,ast.Attribute):
                if isinstance(node.func.value, ast.Name):
                    if 'log' in str(node.func.value.id).lower()[0:3]:
                        unchanged.append(node.func.value.id)

        if isinstance(node,ast.ExceptHandler):
            if isinstance(node.type,ast.Name):
                if node.type.id=='Exception':
                    unchanged.append(node.type.id)
                if 'Error' in str(node.type.id):
                    unchanged.append(node.type.id)
            if isinstance(node.type,ast.Tuple):
                for e in node.type.elts:
                    unchanged.append(e.id)

        if isinstance(node, ast.FunctionDef):
            for arg in node.args.args:
                unchanged.append(arg.arg)


        if isinstance(node,ast.Assign):
            for t in node.targets:
                if isinstance(t,ast.Name):
                    if isinstance(t.ctx,ast.Store):
                        assigned.append(t.id)


        if isinstance(node, ast.Name):
            print(node.id)
            if node.id not in unchanged and node.id not in list(renamed.keys()):
                renamed[node.id]=replacer(node.id)
                node.id=renamed[node.id]
            elif node.id not in unchanged and node.id in list(renamed.keys()):
                node.id=renamed[node.id]



        if isinstance(node, ast.Name):
            ori_node_id=node.id
            if isinstance(node.ctx,ast.Load) and node.id in set(assigned) and node.id not in set(unchanged):
                node.id=renamed[ori_node_id]
            elif isinstance(node.ctx,ast.Load) and node.id not in set(assigned):
                node.id=ori_node_id
            elif isinstance(node.ctx,ast.Load) and node.id in set(unchanged):
                node.id=ori_node_id

    new_src=astor.to_source(root)

    # print(new_src)

    return new_src



def transform_v2(source):
    unchanged=[]+all_res+['self','log','logging','logger','exception','error']
    renamed={}
    root = ast.parse(source)
    print(ast.dump(root))
    store_node=[]
    load_node=[]
    for node in ast.walk(root):
        # print(node)
        # print(node.__dict__)
        if isinstance(node, ast.Import):
            # print("---------ast.Import----------")
            # print(node.names)
            if len(node.names)!=0:
                for ali in node.names:
                    if ali.name!=None:
                        unchanged.append(ali.name)

        if isinstance(node, ast.ImportFrom):
            # print("---------ast.ImportFrom----------")
            # print(node.names)
            if len(node.names)!=0:
                for ali in node.names:
                    if ali.name!=None:
                        unchanged.append(ali.name)

        if isinstance(node, ast.FunctionDef):
            # print("---------ast.Function----------")
            # print(node.name)
            if node.name not in unchanged and node.name not in list(renamed.keys()):
                renamed[node.name]=replacer_final(node.name)
                node.name=renamed[node.name]
                # print("--------------Function---------------")

        if isinstance(node, ast.FunctionDef):
            # print("--------------Function Arg---------------")
            for arg in node.args.args:
                # print(arg.arg)
                unchanged.append(arg.arg)

        if isinstance(node,ast.ClassDef):
            # print("---------ast.ClassDef----------")
            # print(node.name)
            if node.name not in unchanged and node.name not in list(renamed.keys()):
                renamed[node.name]=replacer_final(node.name)
                node.name=renamed[node.name]
                # print(node.name)
                # print("--------------Class---------------")


        # if isinstance(node, ast.Assign):
        #     # print("---------ast.Assign----------")
        #     for t in node.targets:
        #         if isinstance(t,ast.Name) and t.id not in unchanged\
        #                 and t.id not in list(renamed.keys()):
        #             renamed[t.id]=replacer_final(t.id)
        #             t.id=renamed[t.id]
        #             # print(t.id)
        #             # print("--------------Assign---------------")

        # if isinstance(node, ast.Attribute):
        #     # print("-----------Attribute-----")
        #     # print(node.value)
        #     if isinstance(node.value,ast.Name) and node.value.id not in unchanged\
        #             and node.value.id not in list(renamed.keys()):
        #         renamed[node.value.id]=replacer_final(node.value.id)
        #         node.value.id=renamed[node.value.id]
                # print(node.value.id)
            # print("-----------------A-------------")

        # if isinstance(node,ast.ExceptHandler):
        #     # print("----------ExceptHandler-----------")
        #     # print(node.type)
        #     if isinstance(node.type,ast.Tuple):
        #         # print(node.type.elts)
        #         for any in node.type.elts:
        #             if isinstance(any,ast.Name) and any.id not in unchanged\
        #                     and any.id not in list(renamed.keys()):
        #                 renamed[any.id]=replacer_final(any.id)
        #                 any.id=renamed[any.id]
            # print("---------------Except-------------")

        if isinstance(node,ast.Raise):
            # print("----------------Raise-------------------")
            # print(node.exc)
            if isinstance(node.exc,ast.Name) and node.exc.id not in list(renamed.keys()):
                renamed[node.exc.id]=replacer_final(node.exc.id)
                node.exc.id=renamed[node.exc.id]
                print(node.exc.id)
            # print("-------------------Raise----------------------")



        if isinstance(node, ast.Name):
            # print(node.id)
            # print("children: " + str([x for x in ast.iter_child_nodes(node)]) + "\\n")
            if node.ctx.__class__.__name__=='Load':
                # print("Load")
                # print(node.id)
                load_node.append(node.id)
            if node.ctx.__class__.__name__=='Store':
                # print("Store")
                # print(node.id)
                store_node.append(node.id)
        load_store=list(set(load_node).intersection(set(store_node)))

        if isinstance(node, ast.Name):
            if node.id in store_node or node.id in load_store:
                if node.id not in unchanged and node.id not in list(renamed.keys()) and node.id not in list(renamed.values()):
                    renamed[node.id]=replacer_final(node.id)
                    node.id=renamed[node.id]
                elif node.id not in unchanged and node.id in list(renamed.keys()) and node.id not in list(renamed.values()):
                    node.id=renamed[node.id]

        # if isinstance(node, ast.Name):
        #     ori_node_id=node.id
        #     if isinstance(node.ctx,ast.Load) and node.id in set(assigned) and node.id not in set(unchanged):
        #         node.id=renamed[ori_node_id]
        #     elif isinstance(node.ctx,ast.Load) and node.id not in set(assigned):
        #         node.id=ori_node_id
        #     elif isinstance(node.ctx,ast.Load) and node.id in set(unchanged):
        #         node.id=ori_node_id
    # print("store")
    # print(store_node)
    # print("load store")
    # print(load_store)
    new_src=astor.to_source(root)
    # print(new_src)
    # with open("xxxxxx_renamed.py",'w') as f:
    #     f.write(new_src)
    return new_src

#
# f_name="11_3_CVE-2023-22475.py"
# with open(f_name) as f:
#     source=f.read()
# root = ast.parse(source)
# transform_v2(source)



