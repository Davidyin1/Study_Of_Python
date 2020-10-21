# 有两个人物，西门吹雪和叶孤城
# 属性：name：玩家的名字  blood：玩家的血量
# 方法：tong()捅对方一刀，对方掉10滴血
# kanren()砍对方一刀，对方掉15滴血
# chiyao()吃一颗药，补10滴血
# __str__打印玩家状态
import time
# class People:
#     def __init__(self,name,blood):
#         '''
#         构造初始化函数
#         :param name:角色名字
#         :param blood: 角色血量
#         '''
#         self.name = name
#         self.blood = blood
#         pass
#     def tong(self,enemy):
#         enemy.blood-=10
#         info = '%s捅了%s一刀'%(self.name,enemy.name)
#         print(info)
#         pass
#     def kanren(self,enemy):
#         enemy.blood-=15
#         info = '%s砍了%s一刀' % (self.name, enemy.name)
#         print(info)
#         pass
#     def chiyao(self):
#         self.blood+=10
#         info = '%s吃了一颗药，增加10滴血' % self.name
#         print(info)
#         pass
#     def __str__(self):
#         return '%s还剩%s的血量'%(self.name,self.blood)
#     pass

# 创建两个实例化对象
class People:
    def __init__(self,name,blood):
        self.name = name
        self.blood = blood
        pass
    def tong(self,enemy):
        enemy.blood-=10
        info = '%s捅了%s一刀'%(self.name,enemy)
        print(info)
        pass
    def kanren(self,enemy):
        enemy.blood-=15
        info = '%s砍了%s一刀' % (self.name, enemy)
        print(info)
        pass
    def chiyao(self):
        self.blood+=10
        info = '%s吃了一颗药，血量+10'%self.name
        print(info)
        pass
    def __str__(self):
        return '%s还剩%s的血量'%(self.name,self.blood)
    
xmcx = People('西门吹雪',100)
ygc = People('叶孤城',100)

while True:
    if xmcx.blood<=0 or ygc.blood<=0:
        break
        pass
    xmcx.tong(ygc)
    print(ygc)
    print(xmcx)
    print('****************************')
    
    ygc.tong(xmcx)
    print(ygc)
    print(xmcx)
    print('****************************')
    xmcx.chiyao()
    print(ygc)
    print(xmcx)
    time.sleep(1) # 休眠一秒
    pass
print("对战结束...")



