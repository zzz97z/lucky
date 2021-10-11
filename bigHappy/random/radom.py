import random
class r_n():
    def action():
        i1 = [2]
        j1 = [8]
        k1 = [11,14,16,17,18]
        l1 = [30,31,21,23,25]
        m1 = [31,32,33,34,35]
        n1 = [3,1,7,6]
        p1 = [2,12]
        list1=[]

        for i in i1:
            for j in j1:
                for k in k1:
                    for l in l1:
                        for m in m1:
                            for n in n1:
                                for p in p1:
                                    if i not in(j,k,l,m) and j not in(k,l,m) and k not in(l,m) and l !=m and m!=n:
                                            result = i, j, k, l, m, n, p
                                            list1.append(result)

        rad=random.choices(list1,k=1)
        l_r=[]
        for j in rad:
            for k in j:
                l_r.append(k)
        return l_r
    def rr():
        l=r_n.action()
        return l[0:5]

    def bb():
        l = r_n.action()
        return l[-2:]
if __name__ == '__main__':

    for i in range(5):
        a=r_n.action()
        r=a[0:5]
        b=a[5:7]
        for i in range(len(r)):
            for j in range(len(r)-1):
                if r[j]>r[j+1]:
                    r[j],r[j+1]=r[j+1],r[j]
        for j in range(1):
            if b[j]>b[j+1]:
                b[j],b[j+1]=b[j+1],b[j]
        print(r+b)
