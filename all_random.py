# 作者：zengziwei
# 创建时间：2021/7/6 14:43
# 文件名：all_random.py
import random
class all_give():
    # bigHappy
    def b_g_r():
        b_r = []
        for i in range(1, 36):
            b_r.append(i)

        return b_r

    def b_g_b():
        b_b = []
        for i in range(1, 13):
            b_b.append(i)
        return b_b

    def get_br():
        rb = random.sample(all_give.b_g_r(), 5)
        return rb

    def get_bb():
        bb = random.sample(all_give.b_g_b(), 2)
        return bb

    # doublebull
    def d_g_r():
        b_r = []
        for i in range(1, 34):
            b_r.append(i)

        return b_r

    def d_g_b():
        b_b = []
        for i in range(1, 17):
            b_b.append(i)
        return b_b

    def get_dr():
        rb = random.sample(all_give.d_g_r(), 6)
        return rb

    def get_db():
        bb = random.sample(all_give.d_g_b(), 1)
        return bb


if __name__ == '__main__':
    # doublebull
    print("doublebull\n")
    for i in range(2):
        p_d = all_give.get_dr()
        p1_d = all_give.get_db()
        for i in range(len(p_d)):
            for j in range(len(p_d) - 1):
                if p_d[j] > p_d[j + 1]:
                    p_d[j], p_d[j + 1] = p_d[j + 1], p_d[j]
        print(p_d + p1_d)


    # bigHappy
    print("bigHappy\n")
    for i in range(5):
        p = all_give.get_br()
        p1 = all_give.get_bb()
        for i in range(len(p)):
            for j in range(len(p) - 1):
                if p[j] > p[j + 1]:
                    p[j], p[j + 1] = p[j + 1], p[j]
        for i in range(len(p1)):
            for j in range(len(p1) - 1):
                if p1[j] > p1[j + 1]:
                    p1[j], p1[j + 1] = p1[j + 1], p1[j]

        print(p + p1)
