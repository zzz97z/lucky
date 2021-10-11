#作者：zengziwei
#创建时间：2021/4/16 15:15
#文件名：get_more_result.py

import requests
def get_db_his():
    url_l='http://www.cwl.gov.cn/cwl_admin/front/cwlkj/search/kjxx/findDrawNotice?name=ssq&issueCount=30&issueStart=&issueEnd=&dayStart=&dayEnd='
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
    # print('\n', 'boubleBull:')
    # print('\n','第一区:','\n',l_s1)
    # print('\n','第二区:','\n',l_s2)
    # print('\n','第三区:','\n',l_s3)
    # print('\n','第四区:','\n',l_s4)
    # print('\n','第五区:','\n',l_s5)
    # print('\n','第六区:','\n',l_s6)
    # print('\n','第七区:','\n',l_s7)


    print('\n','boubleBull:','\n','第一区',l_s1,'\n','\n','第二区',l_s2,'\n','\n','第三区',l_s3,'\n','\n','第四区',l_s4,'\n','\n','第五区',l_s5,'\n','\n','第六区',l_s6,'\n','\n','第七区',l_s7)


