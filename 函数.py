# def printInfo(name,height,weight,hobby,pro):
#     print("%s的身高是%f"%(name,height))
#     print("%s的体重是%f"%(name,weight))
#     print("%s的爱好是%s"%(name,hobby))
#     print("%s的专业是%s"%(name,pro))
#     pass
#
# printInfo('ykn',181,165,'足球','智能车辆')

# def sum(a,b):
#     sum = a+b
#     print(sum)
#     pass

# sum(1,2) # 实参

# 缺省参数
# def sum1(a=20,b=30):
#     print("默认参数的使用=%d"%(a+b))
#     pass
# sum1()
# sum1(10)

# 可变参数(当参数的个数不确定时使用）
# def getComputer(*args):
#     '''
#     计算累加和
#     :param args:可变长的参数类型
#     :return:
#     '''
# #     # print(args)
# #     result = 0
# #     for item in args:
# #         result+=item
# #         pass
# #     print(result)
# #     pass
# #
# # getComputer(1)
# # getComputer(1,2)
# # getComputer(1,2,3,4,5,6)

# 关键字可变参数
# **来定义
# 在函数体内 参数关键字是一个字典类型 key是一个字符串
# def keyFunc(**kwargs):
#     print(kwargs)
#     pass
# 调用
# keyFunc(1,2,3) 不可传递
# dictA = {'name':'ykn','age':21}
# keyFunc(**dictA)
# keyFunc(name ='peter',age = 21)

# def complexFunc(*args,**kwargs):
#     print(args)
#     print(kwargs)
#     pass
# complexFunc(1,2,3,4,name = 'ykn',age = 21)

# def sum(a,b):
#
#     return a+b
# print(sum(1,2))

# def cal_add(num):
#     listA = []
#     result = 0
#     i = 1
#     while i<=num:
#         result += i
#         i+=1
#         listA.append(result)
#         pass
#
#     return listA
#
# # print(cal_add(5))
#
# def return_tuple():
#     '''
#
#     :return: 返回元组
#     '''
#     return 1,2,3
#
# A = return_tuple()

# 函数的嵌套调用

# def fun1():
#     print("-----------------fun1 start-----------------")
#     print("-----------------执行代码省略-----------------")
#     print("-----------------fun1 end-------------------")
#     pass
# def fun2():
#     print("-----------------fun2 start-----------------")
#     fun1()
#     print("-----------------执行代码省略-----------------")
#     print("-----------------fun2 end-------------------")
#     pass

# fun2()
# 函数的分类：根据函数的返回值和函数的参数
# 有参数又返回值
# 有参数无返回值
# 无参数有返回值
# 无参数无返回值

# pro = '计算机信息管理'
# name = 'ykn'
# # 全局变量和局部变量
# def printInfo():
#     name = 'wyw'
#     print('{}.{}'.format(name,pro))
#     pass
#
# def testmethod():
#     name = 'yzc'
#     print(name,pro)
#     pass
# def ChangeGlobal():
#     '''
#     修改全局变量
#     :return:
#     '''
#     global pro
#     pro = '市场营销'
#     pass
#
# ChangeGlobal()
# print(pro)
# printInfo()
# testmethod()

# 参数引用传值

# a = 1
# def func(x):
#     print(id(x))
#     pass
# # 调用函数
#
# print('a的地址:{}'.format(id(a)))
# func(a)
#
# # 可变类型
# li = []
# def testFunc(params):
#     print(id(params))
#     li.append([1,3,4])
#     pass
#
# print(id(li))
# testFunc((li))

# 匿名函数
# test = lambda x,y:x+y
# print(test(1,2))
# _multiply = lambda a,b,c:a*b*c
# print(_multiply(1,2,3))

# 三元运算符： a if b else c
# age = 15
# print("可以参军" if age>18 else "继续上学")

# a = lambda x,y:x if x>y else y
# print(a(1,2))

# ---------------------------分隔符-----------------------------

# 递归函数
# 必须有一个明确的结束条件
# 求阶乘
# def jiecheng(n):
#     result = 1
#     for item in range(1,n+1):
#         result*=item
#         pass
#     return result
#
# print("5的阶乘是{}".format((jiecheng(5))))
#
# # 递归实现
# def jiguiJc(n):
#     '''
#     递归实现
#     :param n:
#     :return:
#     '''
#     if n==1:
#         return 1
#     return jiguiJc(n-1)*n
#
# print(jiguiJc(5))

# 递归案例：模拟实现 树形结构的遍历
# import os # 引入文件操作模块
# def FindFile(file_path):
#     listRs = os.listdir(file_path) # 得到该路径下所有的文件夹
#     for FileItem in listRs:
#         full_path = os.path.join(file_path,FileItem) # 获取完整的文件路径
#         if os.path.isdir(full_path): # 判断是否是文件夹
#             FindFile(full_path)
#         else:
#             print(FileItem)
#             pass
#         pass
#     else:
#         return
#     pass
#
# FindFile()

