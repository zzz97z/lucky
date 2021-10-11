#作者：zengziwei
#创建时间：2021/4/16 15:15
#文件名：get_more_result.py
import requests
def get_big_his():
    url_l='https://webapi.sporttery.cn/gateway/lottery/getHistoryPageListV1.qry?gameNo=85&provinceId=0&pageSize=30&isVerify=1&pageNo=1'
    headers={
    "Connection":"keep-alive",
    "Accept":"application/json, text/javascript, */*; q=0.01",
    "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
    "Origin":"https://static.sporttery.cn",
    "Sec-Fetch-Site":"same-site",
    "Sec-Fetch-Mode":"cors",
    "Sec-Fetch-Dest":"empty",
    "Referer":"https://static.sporttery.cn/",
    "Accept-Language":"zh-CN,zh;q=0.9"}

    respon=requests.get(url=url_l,headers=headers)
    res=respon.json()['value']['list']
    # print(res)
    result=[]
    k_all=[]
    for i in res:
        r=i['lotteryDrawResult']
        rr1=r.replace(" ",",")
        result.append(rr1)

    red=[]
    blue=[]

    for j in result:
        r=j[0:14]
        red.append(r)
        b=j[-5:]
        blue.append(b)


    l1=[]
    l2=[]
    l3=[]
    l4=[]
    l5=[]
    l6=[]
    l7=[]
    for n in red:
        new_n1=n[0:2]
        l1.append(new_n1)

        new_n2 = n[3:5]
        l2.append(new_n2)

        new_n3 = n[6:8]
        l3.append(new_n3)

        new_n4 = n[9:11]
        l4.append(new_n4)

        new_n5 = n[12:14]
        l5.append(new_n5)

    for m in blue:
        new_n6 = m[0:2]
        l6.append(new_n6)

        new_n7 = m[3:5]
        l7.append(new_n7)


    print('\n','bigHappy:','\n','第一区',l1,'\n','\n','第二区',l2,'\n','\n','第三区',l3,'\n','\n','第四区',l4,'\n','\n','第五区',l5,'\n','\n','第六区',l6,'\n','\n','第七区',l7)

# get_big_his()