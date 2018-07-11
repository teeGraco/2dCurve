import matplotlib.pyplot as plt
import numpy as np

place = np.array([[0,0],[6,3],[3,0],[4,0],[7,7],[9,3],[12,5]])
xs = []
ys = []
ox = []
oy = []

def deBoor(nparry):
    x = []
    y = []
    for t in range(101):
        uu2u3 = nparry[0] * (1 - t / 100) / 3 + nparry[1] * (2 + t / 100) / 3
        uu3u4 = nparry[1] * (2 - t / 100) / 3 + nparry[2] * (1 + t / 100) / 3
        uu4u5 = nparry[2] * (3 - t / 100) / 3 + nparry[3] * (t / 100) / 3

        uuu3 = uu2u3 * (1 - t / 100) / 2 + uu3u4 * (1 + t / 100) / 2
        uuu4 = uu3u4 * (2 - t / 100) / 2 + uu4u5 * (t / 100) / 2

        uuu = uuu3 * (1 - t / 100) + uuu4 * (t / 100)

        x.append(uuu[0])
        y.append(uuu[1])
    return x,y

def Bspline_function3(nparry):
    x = []
    y = []
    for t in range(101):
        p = nparry[0] * ((1 - t / 100) ** 3) / 6
        p = p + nparry[1] * (((t / 100) ** 3) / 2 - ((t / 100) ** 2) + 2 / 3)
        p = p + nparry[2] * (-1 * ((t / 100) ** 3) / 2 + ((t / 100) ** 2) / 2 + t / 200 + 1 / 6)
        p = p + nparry[3] * ((t / 100) ** 3) / 6

        x.append(p[0])
        y.append(p[1])
    return x,y

# N = int(input('how many points? >> '))	#制御点数
# original = [0,0] * N
# for i in range(N):
#     original[2 * i],original[2 * i + 1] = map(int, input('x y >>').split())	#制御点の座標
#
# place = np.array(original).reshape(N,2)
# print (place)

for i in range(len(place) - 3):
    x,y = Bspline_function3(place[i:i+4])
    xs = xs + x
    ys = ys + y

for i in range(len(place)):
    ox.append(place[i][0])
    oy.append(place[i][1])



plt.plot(xs,ys,label='B-Spline')
plt.plot(ox,oy,label='Original')
plt.show()
