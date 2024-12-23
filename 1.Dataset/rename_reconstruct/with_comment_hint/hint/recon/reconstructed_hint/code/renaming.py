# import nltk
# from nltk.corpus import wordnet as wn
# import ast
# import astor
# # import inspect
# # import astunparse
# from wordnetReplacer import replacer
#
#
# with open("2_1_CVE-2023-28836_aft.py") as f:
#     source=f.read()
# # class Visitor(ast.NodeVisitor):
# #     def visit(self,node:ast.AST):
# #         print(node)
# #         self.generic_visit(node)
# #
# # node=ast.parse(source)
# # print(node)
# # print(node._fields)
# # print(node.body)
# # Visitor().visit(node)
#
# def hack(source):
#     root = ast.parse(source)
#     print(ast.dump(root,indent=5))
#     unchanged=[]
#     for node in ast.walk(root):
#         unchanged.append('self')
#         print("------------")
#         print(node)
#         if isinstance(node, ast.ClassDef):
#             print("ast.ClassDef")
#             print(node._fields)
#         # if isinstance(node,ast.)
#         if isinstance(node, ast.Call):
#             print("call")
#             # print(node)
#             print(node.func)
#             if isinstance(node.func, ast.Name):
#                 print("node.func.id")
#                 print(node.func.id)
#                 unchanged.append(node.func.id)
#         if isinstance(node, ast.FunctionDef):
#             print("ast.FunctionDef--node.name")
#             print(node._fields)
#         if isinstance(node, ast.Name):
#             if node.id not in unchanged:
#                 print("ast.Name")
#                 print(node._fields)
#                 print(replacer(node.id))
#         # if isinstance(node,ast.Assign):
#         #     print("node")
#         #     # yield node.id
#         # elif isinstance(node, ast.Attribute):
#         #     print("Attribute")
#         #     print(node.attr)
#         #     # yield node.attr
#         # if isinstance(node, ast.FunctionDef):
#         #     # print(node.name)
#         #     # print(node.body)
#         #     yield node.name
# #         #     yield  node.body
# #
# hack(source)
# print(list(hack(source)))
#
# # import ast
# #
# # class toLower(ast.NodeTransformer):
# #     def visit_arg(self, node):
# #         return ast.arg(**{**node.__dict__, 'arg':node.arg.lower()})
# #
# #     def visit_Name(self, node):
# #         return ast.Name(**{**node.__dict__, 'id':node.id.lower()})
# #
# # code = """
# # def myFunc(Variable):
# #     Tmp = sin(Variable)
# #     return Tmp * 2
# # """
# # new_code = ast.unparse(toLower().visit(ast.parse(code)))
# # print(new_code)
# #
# # import ast
# #
# # class RewriteName(ast.NodeTransformer):
# #
# #     def visit_Name(self, node):
# #         return ast.copy_location(ast.Num(n=3.5, ctx=node.ctx), node)
# #
# # tree = ast.parse('a + b', 'eval')
# # tree = RewriteName().visit(tree)
# # ast.fix_missing_locations(tree)
# # o = compile(tree, '<string>', 'eval')
# # print(eval(o))
# #
# # import ast
# # import astor
# #
# # class MyRenamer(ast.NodeTransformer):
# #
# #     def __init__(self):
# #         self._arg_count = 0
# #
# #     def visit_FunctionDef(self, node):
# #         node.name = "method_name"
# #         self.generic_visit(node)
# #         return node
# #
# #     def visit_arg(self, node):
# #         node.arg = "arg_{}".format(self._arg_count)
# #         self._arg_count += 1
# #         self.generic_visit(node)
# #         return node
# #
# # code = """
# # def foo(my_input):
# #   return my_input + 42
# # """
# #
# # node = ast.parse(code)
# # renamer = MyRenamer()
# # node2 = renamer.visit(node)
# # print(astor.to_source(node2))
# #
# # def collect_variables(a):
# #     if type(a) is ast.Module:
# #         return [v for s in a.body for v in collect_variables(s)]
# #
# #     elif type(a) is ast.FunctionDef:
# #         vs = [v for s in a.body for v in collect_variables(s)]
# #         return [a.name] + vselif type(a) is ast.Assign:
# #         vs = [v for s in a.targets for v in collect_variables(s)]
# #         return vs + collect_variables(a.value)
# #
# #     elif type(a) is ast.Return:
# #         return collect_variables(a.value)elif type(a) is ast.Name:
# #         return [a.id]elif type(a) is ast.BinOp:
# #         return \
# #             collect_variables(a.left) + collect_variables(a.right)
# #
# #     else:
# #         print(type(a)) # Display trees not captured by cases above.
# #     return []