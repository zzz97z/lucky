from xlwt import *
import random
# import time
class rand():
    def action():
        i1 = [2]
        j1 = [9]
        k1 = [5]
        l1 = [21]
        m1 = [26,11]
        n1 = [18,32]
        p1 = [14,13]
        list1=[]

        for i in i1:
            for j in j1:
                for k in k1:
                    for l in l1:
                        for m in m1:
                            for n in n1:
                                for p in p1:
                                    if i not in(j,k,l,m,n) and j not in(k,l,m,n) and k not in(l,m,n) and l not in(m,n) and m!=n:
                                            result = i, j, k, l, m, n, p
                                            list1.append(result)

        rad=random.choices(list1,k=1)
        l_r=[]
        for j in rad:
            for k in j:
                l_r.append(k)
        return l_r
    #取出前6位数
    def rr():
        l=rand.action()
        return l[0:6]

    # 取出最后一位数
    def bb():
        l = rand.action()
        return l[-1:]

if __name__ == '__main__':
    for i in range(5):
        a=rand.action()
        r=a[0:6]
        b=a[6:8]
        #冒泡排序
        # for i in range(len(r)):
        #     for j in range(len(r)-1):
        #         if r[j]>r[j+1]:
        #             r[j],r[j+1]=r[j+1],r[j]

        # 使用sort方法排序
        sorted(r)
        print(r+b)