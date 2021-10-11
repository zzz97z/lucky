from xlwt import *
import random
# import time
class rand:
    def action(self):
        rlist=[20, 22, 28,15,13,14,32,1,3,6,4,9]
        blist=[15]
        rad=sorted(random.sample(rlist,6))+random.sample(blist,1)
        return rad
    #取出前6位数
    def r_r1(self):
        res=rand().action()
        r=res[0:6]
        return r
    #取出最后一位数
    def r_b1(self):
        res = rand().action()
        b=res[-1:]
        return b
if __name__ == '__main__':
    # 从列表中组合随机数
    for i in range(10):
        a=rand().action()
        print(a)




