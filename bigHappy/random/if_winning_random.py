# 作者：zengziwei
# 创建时间：2021/4/7 10:35
# 文件名：if_winning_random.py
from bigHappy.get_the_result import *
from bigHappy.random.radom import r_n

red = get_red()
blue = get_blue()
title = get_title()
count = 10

r1 = []
r2 = []
r3 = []
r4 = []
r5 = []
r6 = []
r7 = []
r8 = []
r9 = []
r0 = []

j_list=[]

for i in range(count):
    r = r_n.rr()
    b = r_n.bb()

    # r=[1, 2, 6, 11, 21, 26]
    # b=[11]
    # o=int(input("请输入第一个号码："))
    # t=int(input("请输入第二个号码："))
    # th=int(input("请输入第三个号码："))
    # f=int(input("请输入第四个号码："))
    # fi=int(input("请输入第五个号码："))
    # six=int(input("请输入第六个号码："))
    # s=int(input("请输入第七个号码："))

    print(title)
    print("您参与的号码", r + b)
    j_list.append(list(r+b))
    print("本期中奖号码", red + blue)
    level = {
        '9': '一等奖',
        '8': '二等奖',
        '7': '三等奖',
        '6': '四等奖',
        '5': '五等奖',
        '4': '六等奖',
        '3': '七等奖',
        '2': '八等奖',
        '1': '九等奖',
    }
    money = {
        '1': '5',
        '2': '15',
        '3': '100',
        '4': '200',
        '5': '300',
        '6': '3000',
        '7': '10000',
        '8': '1000000',
        '9': '10000000',
    }

    r_in = [val for val in red if val in r]
    b_in = [val for val in blue if val in b]
    print(len(r_in), '+', len(b_in))
    if len(r_in) == 3 and len(b_in) == 0 or len(r_in) == 2 and len(b_in) == 1 or len(r_in) == 1 and len(
            b_in) == 2 or len(r_in) == 0 and len(b_in) == 2:
        # print('恭喜获得{},您有{}元奖金可兑换'.format(level['1'],money['1']))
        w9 = '恭喜获得{},您有{}元奖金可兑换\n'.format(level['1'], money['1'])
        r9.append(w9)
        print(w9)
    elif len(r_in) == 3 and len(b_in) == 1 or len(r_in) == 2 and len(b_in) == 2:
        # print('恭喜获得{},您有{}元奖金可兑换'.format(level['2'], money['2']))
        w8 = '恭喜获得{},您有{}元奖金可兑换\n'.format(level['2'], money['2'])
        r8.append(w8)
        print(w8)
    elif len(r_in) == 4 and len(b_in) == 0:
        # print('恭喜获得{},您有{}元奖金可兑换'.format(level['3'], money['3']))
        w7 = '恭喜获得{},您有{}元奖金可兑换\n'.format(level['3'], money['3'])
        r7.append(w7)
        print(w7)
    elif len(r_in) == 3 and len(b_in) == 2:
        # print('恭喜获得{},您有{}元奖金可兑换'.format(level['4'], money['4']))
        w6 = '恭喜获得{},您有{}元奖金可兑换\n'.format(level['4'], money['4'])
        r6.append(w6)
        print(w6)
    elif len(r_in) == 4 and len(b_in) == 1:
        # print('恭喜获得{},您有{}元奖金可兑换'.format(level['5'], money['5']))
        w5 = '恭喜获得{},您有{}元奖金可兑换\n'.format(level['5'], money['5'])
        r5.append(w5)
        print(w5)
    elif len(r_in) == 4 and len(b_in) == 2:
        # print('恭喜获得{},您有{}元奖金可兑换'.format(level['6'], money['6']))
        w4 = '恭喜获得{},您有{}元奖金可兑换\n'.format(level['6'], money['6'])
        r4.append(w4)
        print(w4)
    elif len(r_in) == 5 and len(b_in) == 0:
        # print('恭喜获得{},您有{}元奖金可兑换'.format(level['7'], money['7']))
        w3 = '恭喜获得{},您有{}元奖金可兑换\n'.format(level['7'], money['7'])
        r3.append(w3)
        print(w3)
    elif len(r_in) == 5 and len(b_in) == 1:
        # print('恭喜获得{},您有{}元奖金可兑换'.format(level['8'], money['8']))
        w2 = '恭喜获得{},您有{}元奖金可兑换\n'.format(level['8'], money['8'])
        r2.append(w2)
        print(w2)
    elif len(r_in) == 5 and len(b_in) == 2:
        # print('恭喜获得{},您有{}元奖金可兑换'.format(level['9'], money['9']))
        w1 = '恭喜获得{},您有{}元奖金可兑换\n'.format(level['9'], money['9'])
        r1.append(w1)
        print(w1)
    else:
        w0 = ('很遗憾，您未中奖\n')
        r0.append(w0)
        print(w0)


l_r1 = []
l_r2 = []
l_r3 = []
l_r4 = []
l_r5 = []
l_r6 = []
l_r7 = []
l_r8 = []
l_r9 = []
l_r0 = []
w_all=r1+r2+r3+r4+r5+r6+r7+r8+r9
for kk in w_all:
    if '一等奖' in kk:
        l_r1.append(kk)
    if '二等奖' in kk:
        l_r2.append(kk)
    if '三等奖' in kk:
        l_r3.append(kk)
    if '四等奖' in kk:
        l_r4.append(kk)
    if '五等奖' in kk:
        l_r5.append(kk)
    if '六等奖' in kk:
        l_r6.append(kk)
    if '七等奖' in kk:
        l_r7.append(kk)
    if '八等奖' in kk:
        l_r8.append(kk)
    if '九等奖' in kk:
        l_r9.append(kk)
    if '未中奖' in kk:
        l_r0.append(kk)
t1 = len(l_r1) * int(money['9'])
t2 = len(l_r2) * int(money['8'])
t3 = len(l_r3) * int(money['7'])
t4 = len(l_r4) * int(money['6'])
t5 = len(l_r5) * int(money['5'])
t6 = len(l_r6) * int(money['4'])
t7 = len(l_r7) * int(money['3'])
t8 = len(l_r8) * int(money['2'])
t9 = len(l_r9) * int(money['1'])


total = t1 + t2 + t3 + t4 + t5 + t6 + t7 + t8 + t9
ben = count * 2
pv = total - ben
print('\n', "获得一等奖的次数：", len(l_r1), ' ', "中奖金额：", t1, '\n', "获得二等奖的次数：", len(l_r2), ' ', "中奖金额：", t2, '\n',
      "获得三等奖的次数：", len(l_r3), ' ', "中奖金额：", t3, '\n', "获得四等奖的次数：", len(l_r4), ' ', "中奖金额：", t4, '\n', "获得五等奖的次数：",
      len(l_r5), ' ', "中奖金额：", t5, '\n', "获得六等奖的次数：", len(l_r6), ' ', "中奖金额：", t6, '\n', "获得七等奖的次数：", len(l_r7), ' ',
      "中奖金额：", t7, '\n', "获得八等奖的次数：", len(l_r8), ' ', "中奖金额：", t8, '\n', "获得九等奖的次数：", len(l_r9), ' ', "中奖金额：", t9, '\n',
      "未中奖的次数：", len(l_r0))
print('\n', "抽奖总数：", count, '\n', "成本：", ben, '\n', "中奖金额总数：", total, '\n', "获利：", pv)

# print("\n","打印参与数组:")
# for i in j_list:
#     print(i)