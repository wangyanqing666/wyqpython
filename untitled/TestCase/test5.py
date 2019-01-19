# coding=utf-8
# import os,time
#
# now = time.strftime("%Y-%m-%d %H_%M_%S",time.localtime())
# filename = '../report/' + now + '_result.html'
# f= open(filename,'w')
# a,b,c=input().split()
# print(a,b,c)
# print(type(a))
str_info = '{"name": "test", "age": 18}'
dict_info = eval(str_info)
print(dict_info)
