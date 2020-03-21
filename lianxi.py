"""
查询括号是否正确
"""


class FuhaoError(Exception):
    pass


from lsqueue import *

exp = list(input())
# for item in exp:
#     print(item)
ls1 = LSqueue()
list01 = []
for item in exp:
    ls1.enqueue(item)
while not ls1.is_empty():
    temp = ls1.dequeue()
    if temp not in ["(", "[", "}", ")", "]", "}"]:
        print(temp, end="")
    else:
        a = ord(temp)
        list01.append(a)
        if len(list01) % 2 == 1 and (a == 41 or a == 93 or a == 125):
            # 首次出现的符号为右边符号则错误
            raise FuhaoError("错误发生")
        elif len(list01) % 2 == 0:
            # 检查是否配对
            v1 = list01[-1]
            v2 = list01[-2]
            if (v1 - v2 == 1) or (v1 - v2 == 2):
                print(temp, end="")
            else:
                raise FuhaoError("错误发生")

        else:
            print(temp, end="")
# 检查所有符号是否配对
if len(list01)%2==1:
    raise FuhaoError("错误发生")
"""
from lstack import *
exp = list(input())
ls1 = LStack()
ls2 = LStack()
list01=[]
for item in exp:
    ls1.push(item)
    # print(ls1.top())
while not ls1.is_empty():
    a=ls1.pop()
    ls2.push(a)
    # print(ls2.top())
while not ls2.is_empty():
    # print(ls2.pop())
    val=ls2.pop()
    if val not in ["(", "[", "}", ")", "]", "}"] and len(list01)==0:
        print(val,end="")
    elif len(list01)==1:
        list02.append()
    elif val in ["(", "[", "}", ")", "]", "}"]:
        a=ord(val)
        list01.append(a)
    else:
        a = ord(val)
        list01.append(a)
        if len(list01) % 2 == 1 and (a == 41 or a == 93 or a == 125):
            raise FuhaoError("错误发生")
        elif len(list01) % 2 == 0:
            v1 = list01[-1]
            v2 = list01[-2]
            if (v1 - v2 == 1) or (v1 - v2 == 2):
                print(val, end="")
            else:
                raise FuhaoError("错误发生")

        else:
            print(val, end="")

"""
"""
老师方法
"""
# text = "[hdvj]hvjkhkjcxhvkjxjcnkd[chjdcjsdvjxkvjkd]chjdhvjdshjsdhd(sdvsvhjdghdj)jbvsvjsdhvj{jhdjccjdc}dg"
# # 将验证条件提前定义好
# parens = "()[]{}"  # 特殊处理的字符集
# left_parens = "([{"  # 入栈字符集
# # 验证匹配关系
# opposite = {'}': '{', ']': '[', ')': '('}
# from lstack import *
#
# ls = LStack()  # 存储括号的栈
#
#
# # 编写生成器，遍历字符串，不断提供括号及其位置
# def parent(text):
#     # i为索引位置
#     i, text_len = 0, len(text)
#     # for i in range(text_len):
#     #     if text[i] in parens:
#     #         yield text[i]
#     # 遍历
#     while True:
#         while i < text_len and text[i] not in parens:
#             i += 1
#         # 到字符串结尾
#         if i >= text_len:
#             return
#         else:
#             yield text[i], i
#             i += 1
#
#
# # 判断提供的括号是否匹配
# def ver():
#     for pr, i in parent(text):
#         if pr in left_parens:
#             ls.push((pr, i))  # 左括号入栈
#         elif ls.is_empty() or ls.pop()[0] != opposite[pr]:  # 初始为右括号或者两个括号不对应则报错
#             print("Unmatching is found at %d for %s" % (i, pr))
#             break
#     else:
#         if ls.is_empty():
#             print("All parentheses are matched")
#         else:
#             # 左括号多了
#             d = ls.pop()
#             print("Unmatching is found at %d for %s" % (d[1], d[0]))
# ver()
#
