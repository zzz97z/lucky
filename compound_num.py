#作者：zengziwei
#创建时间：2021/10/11 15:11
#文件名：compound_num.py
r = [1, 7, 5, 17, 8, 25, 27]
b = [1, 12]

list_num = []
for r1 in r:
    for r2 in r:
        for r3 in r:
            for r4 in r:
                for r5 in r:
                    if r1 not in (r2, r3, r4, r5) and r2 not in (r3, r4, r5) and r3 not in (
                    r4, r5) and r4 != r5:
                        res=[r1,r2,r3,r4,r5]
                        # 使用sort方法排序
                        res.sort(reverse=False)

                        #使用冒泡排序
                        # for i in range(len(res)):
                        #     for j in range(len(res)-1):
                        #         if res[j]>res[j+1]:
                        #             res[j],res[j+1]=res[j+1],res[j]
                        list_num.append(res)

new_num=[]
for r in list_num:
    if r not in new_num:
        new_num.append(r)
print(new_num)
print(len(new_num))
