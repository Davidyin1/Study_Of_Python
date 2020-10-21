# 1：求三组连续自然数的和：求出1到10、20到30和35到45的三个和

def sumRange(m,n):
    '''
    求从m到n的连续自然数的和
    :param m:
    :param n:
    :return: sum
    '''
    return sum(range(m,n+1))
print(sumRange(1,10))
print(sumRange(20,30))
print(sumRange(30,45))
# 2：100个和尚吃100个馒头，大和尚一人吃3个馒头，小和尚三个人吃1个馒头。请问大小和尚各多少人

def PersonCount():
    for a in range(1,34):
        if a*3+(100-a)*(1/3)==100:
            return (a,100-a)
        pass
    pass

rsObj = PersonCount()
print("大和尚{}人，小和尚{}人".format(rsObj[0],rsObj[1]))
# 3：指定一个列表，列表里含有唯一一个只出现过一次的数字。写程序找出这个"独一无二"的数字

ListA = [1,3,4,3,3,5,2,4,2,5,2]
set1 = set(ListA)
# print(set1)
for i in set1:
    ListA.remove(i)
    pass
set2 = set(ListA)
set3 = set1-set2
print(set3)