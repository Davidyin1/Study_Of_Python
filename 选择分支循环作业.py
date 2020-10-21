# 猜年龄小游戏，有三点需求
# 1 允许用户最多尝试3次
# 2 每尝试3次后，如果还没猜对，就问用户是否还想继续玩，如果回答Y或y，就继续让其猜3次，以及往复，如果回答N或n，就退出程序
# 3 如果猜对了，就直接退出
import random
# times = 0
# while times <= 2:
#     age = int(input("请输入您要猜的年龄:"))
#     _com_age = random.randint(5,10)
#     if age == _com_age:
#         print("猜对了")
#         break
#         pass
#     elif age < _com_age:
#         print("猜小了")
#         pass
#     else:
#         print("猜大了")
#         pass
#     times+=1
#     if times==3:
#         choose = input("想不想继续？y/n")
#         if choose =='Y' or choose=='y':
#             times=0
#             pass
#         else:
#             break
#             pass
#         pass
#     pass


# 小王身高1.75,体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小王计算他的BMI指数，并根据BMI指数：
# 低于18.5 过轻  18.5-25 正常  25-28 过重   28-32 肥胖  高于32：严重肥胖
# 用if-elif判断并打印结果

length = 1.75
weight = 80.5
BMI = weight/(length**2)
if BMI <18.5:
    print("过轻")
    pass
elif 18.5 <= BMI < 25:
    print("正常")
    pass
elif 25 <= BMI < 28:
    print("过重")
    pass
elif 28<=BMI<32:
    print("肥胖")
    pass
else:
    print("严重肥胖")
    pass





