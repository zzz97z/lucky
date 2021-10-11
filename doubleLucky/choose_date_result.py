#作者：zengziwei
#创建时间：2021/4/7 11:00
#文件名：choose_date_result.py

from bs4 import BeautifulSoup
import requests

l_date=21104
url='http://kaijiang.500.com/shtml/ssq/{}.shtml?0_ala_baidu'.format(l_date)
response=requests.get(url)
response.encoding='GB18030'
content=response.text
soup=BeautifulSoup(content,'html.parser')

soup_task=soup.find_all(class_="ball_red")
soup_task2=soup.find_all(class_="ball_blue")
get_title=soup.find_all(class_="span_right")
get_date=soup.find_all(class_="iSelect")
get_act=soup.find_all(class_="kjxq_box02_title_mid")
for act in get_act:
    action=act.text
for date in get_date:
    g_date="第"+date.text+"期"

l_title=[]
for k in get_title:
    tt=k.text
    l_title.append(tt)

title=l_title[0]
# print(soup_task)
red=[]
blue=[]
def get_act():
    return action

def get_date():
    return g_date

def get_title():
    return title
def get_red():
    for i in soup_task:
        toInt=int(i.text)
        red.append(toInt)
    return red

def get_blue():
    for j in soup_task2:
        toInt = int(j.text)
        blue.append(toInt)
    return blue
