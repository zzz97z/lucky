#作者：zengziwei
#创建时间：2021/4/21 15:57
#文件名：alist_rand.py

import random
class rand:
    def action(self):
        rlist=[2,3,13,14,15,23,24,25,27,28]
        blist=[6,7,10]

        rad = sorted(random.sample(rlist, 5)) + random.sample(blist, 2)
        return rad

    def r_r1():
        r=rand().action()
        return r[0:5]
    def r_b1():
        b=rand().action()
        return b[-2:]

if __name__ == '__main__':
    for i in range(2):
        a=rand().action()
        print(a)
