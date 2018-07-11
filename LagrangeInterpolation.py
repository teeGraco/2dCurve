import numpy as np
import matplotlib.pyplot as plt

place = [[-5,25],[-4,16],[-3,9],[-2,4],[-1,1],[0,0],[1,1],[2,4],[3,9],[4,16],[5,25]]
# N = int(input('how many points? >> '))	#制御点数
# original = [0,0] * N
# for i in range(N):
#     original[2 * i],original[2 * i + 1] = map(int, input('x y >>').split())	#制御点の座標
#
# arr = np.array(original).reshape(N,2)
# place = arr.tolist()
# print (place)

ox = []
oy = []

def denominator(n):
    ret = []
    for i in range(n + 1):
        ans = 1
        for j in range(n + 1):
            if j == i:
                pass
            else:
                ans = ans * (i - j)
        ret.append(ans)
    return ret

def Lni(t, li, n):
    ret = []
    for i in range(n + 1):
        ans = 1
        for j in range(n + 1):
            if j == i:
                pass
            else:
                ans = ans * (t - j)
        ans = ans / li[i]
        ret.append(ans)
    return ret

def LagrangeFunction(place):
    m = len(place)              #点の数
    n = m - 1                   #次数
    denom_list = denominator(n)
    ans_x = []
    ans_y = []
    for t in range(n * 25 + 1):
        x = 0
        y = 0
        LNI = Lni(t / 25, denom_list, n)
        for i in range(n + 1):
            x = x + place[i][0] * LNI[i]
            y = y + place[i][1] * LNI[i]
        ans_x.append(x)
        ans_y.append(y)
    return ans_x, ans_y


def Aitken(points):
    m = len(points)
    ans_x = []
    ans_y = []
    for t in range((m - 1) * 25 + 1):
        p1 = points.copy()
        p2 = []
        deg = m
        while deg > 1:
            r = m + 1 - deg
            for i in range(deg - 1):
                x = (p1[i][0] * (i + r - t / 25) + p1[i + 1][0] * (t / 25 - i))/ r
                y = (p1[i][1] * (i + r - t / 25) + p1[i + 1][1] * (t / 25 - i))/ r
                p2.append([x,y])
            p1.clear()
            p1 = p2.copy()
            p2.clear()
            deg = deg - 1
        ans_x.append(p1[0][0])
        ans_y.append(p1[0][1])
    return ans_x, ans_y


x,y = Aitken(place)
x1,y1 = LagrangeFunction(place)


for i in range(len(place)):
    ox.append(place[i][0])
    oy.append(place[i][1])

plt.plot(x,y,label='Lagrange')
plt.plot(x1,y1,label='LagFunc')
plt.plot(ox,oy,label='Original')
plt.show()
