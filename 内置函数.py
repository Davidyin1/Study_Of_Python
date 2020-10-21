# # 常用数学运算函数
# # abs() 求绝对值函数
# # round 对浮点数进行近似取值
# print(round(3.66))
# # pow() 求指数
# print(pow(2,5))
# # max求最大值
# print(max([23,123,421,13,43214]))
# # sum求和
# print(sum(range(50),3)) # 最后结果+3
# # eval 执行表达式
# a,b,c=1,2,3
# print(eval('a+b+c'))
# # bin 二进制转换
# print(bin(10))
#
# # 字典的操作
# dic = dict(name='小明',age=18)
# # print(type(dic))
# # dict['name'] = 'xiaoming'
# print(dic)

# -------------------------------
# 序列操作函数
# all()判断所有元素是否都为TRUE ，除0 FALSE外 都是TRUE
# any()判断所有元素是否全部为FALSE
# sort只用在列表上，sorted用在任何迭代对象上
# zip()将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，返回由元组组成的列表
# def printBookInfo():
#     books = []#存储所有的图书信息
#     id = input("请输入编号：")
#     bookname = input("请输入书名")
#     bookPos = input("请输入位置")
#     idList = id.split(' ')
#     nameList = id.split(' ')
#     posList = id.split(' ')
#
#     bookInfo = zip(idList,nameList,posList)
#     for bookItem in bookInfo:
#         dictInfo =
#         pass

# set 不支持索引和切片，是一个无序的且不重复的容器
# 类似于字典，但是只有key，没有value
# 创建集合
set1 = {1,2,3}
# print(type(set1))
set1.add('python')
print(set1)
set1.clear()
print(set1)
