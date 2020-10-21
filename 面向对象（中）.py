# 析构方法
#
# class Animal:
#     def __init__(self, name):
#         self.name = name
#         print("这是构造初始化的方法")
#         pass
#
#     def __del__(self):  # 总是在程序最后执行
#         print('当在某个作用域下面没有被使用【引用】的情况下，解释器会自动调用次函数来释放内存')
#         print("这是析构方法")
#         print("%s被彻底清理" % self.name)
#         pass
#
#
# cat = Animal('小花猫')
#
# dog = Animal('柯基')

# 继承

class Animal:
    def eat(self):
        print('吃饭了')
        pass

    def drink(self):
        print('喝水了')
        pass

    pass


class Dog(Animal):
    def wwj(self):
        print('小狗汪汪叫')
        pass

    pass


class Cat(Animal):
    def mmj(self):
        print('小猫喵喵叫')
        pass

    pass

d1 = Dog()
d1.eat()
