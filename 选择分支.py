# score = 60
# if score > 60:
#     print("成绩合格")
#     pass
# else:
#     print("成绩不合格")
#     pass
# score = int(input('请输入成绩'))
# if score > 90:
#     print("优秀")
#     pass
# elif score >= 80:
#     print("良好")
#     pass
# elif score >= 70:
#     print("合格")
#     pass
# elif score >= 60:
#     print("差")
#     pass
# else:
#     print("不及格")

# 猜拳游戏
# 石头 0， 剪刀 1  布 2

# import random
# # 计算机  人
# count = 1
# while count <= 10:
#     person = int(input('请出拳'))
#     computer = random.randint(0, 2)
#     if person == 0 and computer == 1:
#         print("厉害了你居然赢了")
#         pass
#     elif person == 1 and computer == 2:
#         print("厉害了你居然赢了")
#         pass
#     elif person == 2 and computer == 0:
#         print("厉害了你居然赢了")
#         pass
#     elif person == computer:
#         print("平手")
#         pass
#     else:
#         print("你输了")
#         pass
#     count += 1

# if-else 的嵌套使用
# xuefen=int(input("请输入你的学分"))
# grade = int(input("请输入你的成绩"))
# if xuefen > 10:
#     if grade >=80:
#         print("您可以升班了，恭喜您！")
#         pass
#     else :
#         print("很遗憾，成绩不达标")
#         pass
#     pass
# else:
#     print("您的表现也太差了吧")
#     pass

# while的使用
# 案例 输出1-100的数据
# index = 1
# while index <= 100:
#     print(index)
#     index += 1
#     pass

# 打印99乘法表
# row = 9
# while row >= 1:
#     col = 1
#     while col<=row:
#         print("%d*%d=%d"%(row,col,row*col),end=" ")
#         col+=1
#         pass
#     print()
#     row-=1
#     pass

# 打印直角三角形

# row = 1
# while row <= 7:
#     j = 1
#     while j <= row:
#         print("*", end=" ")
#         j += 1
#         pass
#     row += 1
#     print()
#     pass
# row = 7
# while row >= 1:
#     j = 1
#     while j <= row:
#         print("*", end=" ")
#         j += 1
#         pass
#     row -= 1
#     print()
#     pass

# 打印等腰三角形
# row = 1
# while row <= 10:
#     j = 1
#     while j <= 10-row:
#         print(" ",end=" ")
#         j += 1
#         pass
#     k = 1
#     while k <= 2*row - 1:
#         print("!", end=" ")
#         k += 1
#         pass
#     print()
#     row += 1
#     pass

# for循环

# tags = '我是一个中国人' # 字符串类型本身就是字符类型的集合
# for item in tags:
#     print(item)
#     pass

# range 此函数可以生成一个数据集合列表
# range(起始值：结束：步长），步长不0
# sum = 0
# for data in range(1,100):# 左包含右不包含
#     sum += data
#     pass
# print("sum=%d"%sum)
# print('--------------for的使用--------------')
# for data in range(50,201,2):
#     print(data,end=" ")
#     pass

# 猜拳游戏,break和continue
# break代表终断结束，只要满足条件直接结束本层循环
# continue 结束本次循环，继续进行下次循环（当continue条件满足的时候，本次循环剩下的语句将不再执行）
# 这两个关键字只能用在循环中
# sum = 0
# for item in range(1,51):
#     if sum>100:
#         print("循环执行到%d就退出了"%item)
#         break
#         pass
#     sum += item
#     pass
# print("sum=%d"%sum)
# print("-----------continue的使用------------")
# for item in range(1,101):
#     if item%2==0:
#         continue
#         pass
#     print(item)
#     pass

# for item in 'I love python':
#     # if item=='e':
#     #     break
#     if item=='o':
#         continue
#         pass
#     print(item)
#     pass

# index = 1
# while index<=100:
#     if index>20:
#         break
#         pass
#     print(index)
#     index+=1
#     pass

# 99乘法表用for实现
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%d*%d=%d "%(j,i,i*j),end=" ")
#         pass
#     print() # 控制换行
#     pass

# for----else
# for item in range(1,11):
#     print(item,end=" ")
#     pass

# account ='wyw'
# pwd='123'
# for i in range(3):
#     zh=input("请输入账号:")
#     pd=input("请输入密码:")
#     if zh==account and pd==pwd:
#         print("登录成功！")
#         break
#         pass
#     pass
# else:
#     print("您的账号被锁定")
#     pass

# while----else
index =1
while index<=10:
    print(index)
    index+=1
    pass
else:
    print('else执行了吗')
    pass
