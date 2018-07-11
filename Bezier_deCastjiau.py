import matplotlib.pyplot as plt

def deCasteljau(li_x,li_y,num_t):
    x = []
    y = []
    xt = []
    yt = []
    for i in range(num_t + 1):
        t = i / num_t
        xs = li_x.copy()
        ys = li_y.copy()
        #print (t)
        while len(xs) > 1:
            for num in range(len(xs) - 1):
                x.append((1 - t) * xs[num] + t * xs[num + 1])
                y.append((1 - t) * ys[num] + t * ys[num + 1])
            xs = x.copy()
            ys = y.copy()
            x.clear()
            y.clear()
            #print (xs,ys)
        xt.append(xs[0])
        yt.append(ys[0])
    return xt, yt

N = int(input('how many points? >> '))	#制御点数
original_x = [0] * N
original_y = [0] * N
for i in range(N):
    original_x[i],original_y[i] = map(int, input('x y >>').split())	#制御点の座標
x,y = deCasteljau(original_x,original_y,100)
plt.plot(x,y,label = 'Bezier')
plt.plot(original_x,original_y, label='original')
plt.show()
