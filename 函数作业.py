# 1：写函数，接受n个数字，求这些参数数字的和

def cal_add(*args):
    result = 0
    for item in args:
        result += item
        pass
    return result

sum = cal_add(1,2,3,4,5)
print(sum)

# 写函数，找出传入的列表或元组的奇数位对应的元素，并返回一个新的列表

def solve_func(container):
    length = len(container)
    listA = []
    i = 0
    while i <length:
        listA.append(container[i])
        i += 2
        pass
    return listA
    pass

container =[1,2,3,4,5,6,7]
ListB = solve_func(container)
print(ListB)

# 写函数，检查传入字典的每一个value的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。PS：字典中的value只能是字符串或者列表

def proc_dict(dictA):
    '''
    处理新字典
    :param dictA: 传入的字典
    :return: 新字典
    '''
    result = {}
    for key,value in dictA.items():
        if len(value)>2:
            result[key] = value[:2]
            pass
        else:
            result[key] = value
            pass
        pass
    return result
dictB = {'name':'ykn','hobby':['sing','run','coding'],'pro':'mechiam'}
print(proc_dict(dictB))
