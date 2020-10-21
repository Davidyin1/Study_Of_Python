# # 定义类和对象
# # 类的结构 类名 属性 方法
# class Person:
#     '''
#     对应人的特征
#     '''
#
#     age = 22
#     '''
#     方法
#     '''
#     def __init__(self):
#         self.name = 'Hamilton' # 实例属性
#         pass
#
#     def eat(self):
#         print("大口吃饭")
#         pass
#     def run(self):
#         print("多人运动")
#         pass
#     pass
#
# ykn = Person() # 创建对象
# ykn.eat() # 调用函数
# ykn.run()
# print("年龄是{}".format(ykn.name))

# class People:
#     def eat(self):
#         '''
#         吃的行为
#         :return:
#         '''
#         print("喜欢吃榴莲")
#
#     pass
#
# ykn = People()
# ykn.hobby = '踢足球'
# ykn.sex = '男神'
# ykn.age = 20
# print(ykn.age)

# 如果有n个这个对象被实例化，那么就需要添加很多次这样的属性了，显然比较麻烦
# -------------------使用init方法改进--------------------
# class People:
#     def __init__(self,name,sex,age):  # 魔术方法
#         '''
#         实例属性的申明
#         '''
#         self.name = name
#         self.sex = sex
#         self.age = age
#         pass
#     def eat(self,food):
#         '''
#         吃的行为
#         :return:
#         '''
#         print(self.name+"喜欢吃"+food)
#
#     pass

# xm = People()
# print(xm.name) # 直接输出的默认值
# xm.name = 'xiaoming'
# print(xm.name)
# ykn = People('殷康宁','male',22)
# ykn.eat('香蕉')

# 总结 __init__
# 1：python自带的内置函数，具有特殊的函数  使用双下划线包起来的【魔术方法】
# 2：是一个初始化的方法，用来定义实例属性和初始化数据的，在创建对象的时候自动调用 不用手动去调用
# 3：利用传参的机制可以让我们定义功能更加强大的类

# ------------------------self的理解----------------------------
# self和对象只向同一个内存地址，可以认为self就是对象的引用

# class Person:
#     def eat(self,name,food):
#         # print(self)
#         print('%s 喜欢吃 %s'%(name,food))
#         pass
#     pass
#
# people = Person()
# people.eat('ykn','ddd')
# 小结 self特点
# self只有在类中定义实例方法的时候才有意义，在调用的时候不必传入相应的参数，而是有解释器自动去指向
# self的名称可以更改
# self指的是类实例对象本身，相当于java中的this

# -----------------__new__--------------
# __new__和__init__的区别
# __new__类的实例化方法：必须要返回该实例，否则对象创建不成功
# __init__用来做数据属性初始化工作，也可以认为是实例的构造方法，接受类的实例self并对其进行构造
# __new__至少有一个参数是cls代表要实例化的类，此参数在实例化时由python解释器自动提供
# __new__函数执行要早于__init__

