#作者：zengziwei
#创建时间：2021/4/7 11:00
#文件名：choose_date_result.py

from bs4 import BeautifulSoup
import requests
a_date=21076
url='http://kaijiang.500.com/shtml/dlt/{}.shtml?0_ala_baidu'.format(a_date)
response=requests.get(url)
response.encoding='GB18030'
content=response.text
soup=BeautifulSoup(content,'html.parser')

# soup_task=soup.find_all(class_="ball_box01")
soup_task=soup.find_all(class_="ball_red")
soup_task1=soup.find_all(class_="ball_blue")
title=soup.find_all(class_="span_left")
red=[]
blue=[]
def get_title():
    for k in title:
        return k.text

def get_red():
    for i in soup_task:
        toInt=int(i.text)
        red.append(toInt)
    return red

def get_blue():
    for j in soup_task1:
        toInt=int(j.text)
        blue.append(toInt)
    return blue
# a=get_title()
# print(a)


