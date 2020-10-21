# Test = 'python'
# for items in Test:
#     print(items,end = ' ')
# name = 'peter'
# print("姓名首字母转换大写%s"%name.capitalize())
# a = '      hello      '
# b = a.strip()# strip 去除字符串的空格
# c = a.lstrip()
# d = a.rstrip()
# print(b)
# print(a)
# print(c)
# print(d)

# dataStr = 'I love python'
# print(dataStr.find('o')) # 可以查找目标对象在序列对象中的位置，找不到对应的数据会返回-1
# print(dataStr.index('o')) # index如果没有找到对应的数据就会报错
# print(dataStr.startswith('O')) # 判断
# print(dataStr.lower()) # 转化为小写
# print(dataStr.upper()) #转化为大写

# strMsg = 'hello world'
# slice [start:end:step]
# print(strMsg)
# print(strMsg[0])
# print(strMsg[2:5]) # 切片左闭右开
# print(strMsg[2:]) # 取到最后
# print(strMsg[0:3])
# print(strMsg[::-1]) # 倒序输出

# 列表
#li = []
# print(type(li))
# li = [1,2,3,'你好']
# print(li)
# print(len(li))

# listA = ['abcd', 785, 12.23, 'ykn', True]
# print(listA)
# print(listA[0])

# print("-----------增加-----------")
# listA.append('ykn')
# listA.insert(1,'wyw') # 插入操作
#
# print(listA)
# rsData = list(range(10)) # 强制转化为list对象
# # print(rsData)
# listA.extend(rsData)
# print(listA)

# 元组
# 元组的创建
# tupleA = ('abdc', 89, 9.12, 'peter', [11,22,33])
# print(tupleA)
# 元组的查询
# for item in tupleA:
#     print(item, end=' ')
# print(tupleA[2])
# print(tupleA[::-1])
# print(tupleA[-2:-1:])

# 字典
# dictA = {'pro':'艺术','school':'beijing'} # 空字典
# dictA['name'] = 'ykn'
# dictA['age'] = '30'
# dictA['pos'] = 'singer'
# print(dictA)
# print(dictA['name']) # 通过键获取对应的值
# dictA['name'] = '谢霆锋'
# print(dictA)
# print(dictA.keys())
# print(dictA.values())
# print(dictA.items())
# for key,value in dictA.items():
#     print('key=%s,value=%s'%(key,value))

# dictA['school']='hongkong'
# dictA.update({'age':32})
# print(dictA)

# 删除操作
# del dictA['name']
# dictA.pop('age')
# print(dictA)
# 如果排序 按照key排序
# print(sorted(dictA.items(),key=lambda d:d[1]))

# 共有方法 + * in
strA = '人生苦短'
strB = '我用python'
listA = list(range(10))
listB = list(range(11,20))
# print(listA+listB)
# print(strA+strB)
print(strB*3)

# in 对象是否存在
print('生'in strA)