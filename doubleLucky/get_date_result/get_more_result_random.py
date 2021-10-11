#作者：zengziwei
#创建时间：2021/4/16 15:15
#文件名：get_more_result.py
from tool.requests import *
import requests
import random
class rand():
    def action():
        url_l='http://www.cwl.gov.cn/cwl_admin/kjxx/findDrawNotice?name=ssq&issueCount=50'
        headers={
        "Proxy-Connection":"keep-alive",
        "Accept":"application/json, text/javascript, */*; q=0.01",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
        "X-Requested-With":"XMLHttpRequest",
        "Referer":"http://www.cwl.gov.cn/kjxx/ssq/kjgg/",
        "Accept-Language":"zh-CN,zh;q=0.9",
        "Cookie":"UniqueID=L7kKY47HG2L1rsxh1618813669106; Sites=_21; _ga=GA1.3.50556367.1618813671; _gid=GA1.3.1563164673.1618813671; _gat_gtag_UA_113065506_1=1; 21_vq=5"}

        respon=requests.get(url=url_l,headers=headers)
        res=respon.json()['result']
        red=[]
        blue=[]
        k_all=[]
        for i in res:
            r=i['red']
            red.append(r)
            b=i['blue']
            blue.append(b)
            title=i['code']
            kk='\n'+'第'+title+'期'+'\n'+r+','+b
            k_all.append(kk)
            # print(kk)
        # print(blue[0])
        index=0
        l_s1=[]
        l_s2=[]
        l_s3=[]
        l_s4=[]
        l_s5=[]
        l_s6=[]
        l_s7=[]

        for j in range(30):
            s1=red[index][0:2]
            s2=red[index][3:5]
            s3=red[index][6:8]
            s4=red[index][9:11]
            s5=red[index][12:14]
            s6=red[index][15:17]
            s7=blue[index]
            l_s1.append(s1)
            l_s2.append(s2)
            l_s3.append(s3)
            l_s4.append(s4)
            l_s5.append(s5)
            l_s6.append(s6)
            l_s7.append(s7)
            index += 1

        # print('\n','第一区:','\n',l_s1)
        # print('\n','第二区:','\n',l_s2)
        # print('\n','第三区:','\n',l_s3)
        # print('\n','第四区:','\n',l_s4)
        # print('\n','第五区:','\n',l_s5)
        # print('\n','第六区:','\n',l_s6)
        # print('\n','第七区:','\n',l_s7)

        # print(l_s1)
        # print(k_all)
        # print('第一区出现的数',list(set(l_s1)))
        # print('第二区出现的数',list(set(l_s2)))
        # print('第三区出现的数',list(set(l_s3)))
        # print('第四区出现的数',list(set(l_s4)))
        # print('第五区出现的数',list(set(l_s5)))
        # print('第六区出现的数',list(set(l_s6)))
        # print('第七区出现的数',list(set(l_s7)))

        l_r1 = []
        rr1=list(set(l_s1))
        for i in rr1:
            l_r1.append(int(i))



        l_r2=[]
        rr2=list(set(l_s2))
        for i in rr2:
            l_r2.append(int(i))


        l_r3=[]
        rr3=list(set(l_s3))
        for i in rr3:
            l_r3.append(int(i))



        l_r4=[]
        rr4=list(set(l_s4))
        for i in rr4:
            l_r4.append(int(i))



        l_r5=[]
        rr5=list(set(l_s5))
        for i in rr5:
            l_r5.append(int(i))



        l_r6=[]
        rr6=list(set(l_s6))
        for i in rr6:
            l_r6.append(int(i))



        l_r7=[]
        rr7=list(set(l_s7))
        for i in rr7:
            l_r7.append(int(i))

        # a=r1()
        # print(a)
        list1=[]
        for i in l_r1:
            for j in l_r2:
                for k in l_r3:
                    for l in l_r4:
                        for m in l_r5:
                            for n in l_r6:
                                for p in l_r7:
                                    if i not in (j, k, l, m, n) and j not in (k, l, m, n) and k not in (l, m, n) and l not in (
                                    m, n) and m != n and i < j < k < l < m < n:
                                        result = i, j, k, l, m, n, p
                                        list1.append(result)
        # for i in range(50):
        #     rad=random.choices(list1,k=1)
        #     print(rad)
        for i in range(1):
            rad=random.choices(list1,k=1)
            # print(rad)
        l_r=[]
        for j in rad:
            for k in j:
                l_r.append(k)
        return l_r
    def rr():
        l=rand.action()
        return l[0:6]
    def bb():
        l = rand.action()
        return l[-1:]

# if __name__ == '__main__':
#         a=rand.action()
#         print(a)