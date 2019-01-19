# -*- coding: utf-8 -*-
# dic={'zhangsan':100, 'lisi':65, 'tianlaoshi':65, 'liulaoshi':99}
#
# print(list(dic))
# # # print(dic.values())
# # for k,v in  dic.items():
# #    # print(k,v)
# #    #print(dic.values())
# #    cou=list(dic.values()).count(v)
# #    print(cou)
# #    # if  list(dic.values()).count(v)>1:
# #    #     del(k)
# # print(dic)
#
# data = {
# 				     'JiaNaiLiang': 60,
# 				     'LiXiaoLu': 75,
# 				     'TianLaoShi': 99,
# 				     'MaSu': 88,
# 				     'KongLingHui': 35,
# 				     'LiuLaoShi': 100
# 				}
# print(sorted(list(data.items()),
#              key=lambda
#                  item:item[1])
#       [-1])
# print()
# # aa=list(data.values())
# # print(aa)
# # print(sum(aa))
# # print(max(aa))
'''
def avg(list):
    return sum(list)/len(list)
list1=[]
shuxue=[]
yingyu=[]
yuwen=[]
data = {
		            '小明':{'语文':60, '数学':68, '英语':45},
		            '小璐':{'语文':10, '数学':28, '英语':5},
		            '小辉':{'语文':44, '数学':86, '英语':73},
		            '小亮':{'语文':99, '数学':95, '英语':95},
		            '田老师':{'语文':98, '数学':65, '英语':100},
		            '刘老师':{'语文':77, '数学':97, '英语':65},
		       	}
for k,v in data.items():
    #print(v.values())
    #print((v.get('语文','0')))
    vv=list(v.values())
    print(vv)
    #print(v)
    #print(v.get('语文','0'))
    yuwen.append(v.get('语文','0'))
    yingyu.append(v.get('英语', '0'))
    shuxue.append (v.get('数学', '0'))
    if avg(vv)<60:
        print(k)
print('语文最高分：%d ,英语最高分：%d，数学最高分%d'%(max(yuwen),max(shuxue),max(yingyu)))
print('语文平均分：%d ,英语平均分：%d，数学平均分%d'%(avg(yuwen),avg(shuxue),avg(yingyu)))

'''
def avg(list):
    return sum(list)/len(list)
list1=[]
shuxue={}
yingyu={}
yuwen={}
data = {
		            '小明':{'语文':60, '数学':68, '英语':45},
		            '小璐':{'语文':10, '数学':28, '英语':5},
		            '小辉':{'语文':44, '数学':86, '英语':73},
		            '小亮':{'语文':99, '数学':95, '英语':95},
		            '田老师':{'语文':98, '数学':65, '英语':100},
		            '刘老师':{'语文':77, '数学':97, '英语':65},
		       	}
for k,v in data.items():
    #print(v.values())
    #print((v.get('语文','0')))
    vv=list(v.values())
    print(vv)
    yuwen[k]=(v.get('语文','0'))
    print(yuwen[k],'22222222222222')
    yingyu[k]=(v.get('英语', '0'))
    shuxue[k]=(v.get('数学', '0'))
    if avg(vv)<60:
        print(k)
print(yuwen)
print('语文最高分：%d ,英语最高分：%d，数学最高分%d'%(max(list(yuwen.values())),max(list(yingyu.values())),max(list(shuxue.values()))))
#print('语文平均分：%d ,英语平均分：%d，数学平均分%d'%(avg(yuwen),avg(shuxue),avg(yingyu)))
