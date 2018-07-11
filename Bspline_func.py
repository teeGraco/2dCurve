import numpy as np
import matplotlib.pyplot as plt

def bspline_func(knots):
    n = len(knots) - 2
    div = knots[-1] - knots[0]
    ts = np.arange(knots[0],knots[-1],div / 100)
    Nt = []
    for t in ts:
        n_prime = n
        N1 = N_init(t, n, knots)
        N2 = []
#        print (t)
        while n_prime > 0:
#            print (N1)
            m = n + 1 - n_prime
            for i in range(n_prime):
                val = 0
                if knots[i + m] != knots[i]:
                    val = (t - knots[i]) / (knots[i + m] - knots[i]) * N1[i]
                if knots[i + m + 1] != knots[i + 1]:
                    val = val + (knots[i + m + 1] - t) / (knots[i + m + 1] - knots[i + 1]) * N1[i + 1]
                N2.append(val)
            N1.clear()
            N1 = N2.copy()
            N2.clear()
            n_prime = n_prime - 1
        Nt.append(N1[0])
    return ts, Nt

def N_init(t, n, knots):
    N = [0] * (n + 1)
    for i in range(n + 1):
        if knots[i] <= t and knots[i + 1] > t:
            N[i] = 1
    print (t, N)
    return N

# knot1 = [0,1,1,1,1,1,1,1]
# ts, Nt1 = bspline_func(knot1)
# knot2 = [0,0,1,1,1,1,1,1]
# ts, Nt2 = bspline_func(knot2)
# knot3 = [0,0,0,1,1,1,1,1]
# ts, Nt3 = bspline_func(knot3)
# knot4 = [0,0,0,0,1,1,1,1]
# ts, Nt4 = bspline_func(knot4)
# knot5 = [0,0,0,0,0,1,1,1]
# ts, Nt5 = bspline_func(knot5)
# knot6 = [0,0,0,0,0,0,1,1]
# ts, Nt6 = bspline_func(knot6)
# knot7 = [0,0,0,0,0,0,0,1]
# ts, Nt7 = bspline_func(knot7)
# plt.plot(ts,Nt1)
# plt.plot(ts,Nt2)
# plt.plot(ts,Nt3)
# plt.plot(ts,Nt4)
# plt.plot(ts,Nt5)
# plt.plot(ts,Nt6)
# plt.plot(ts,Nt7)

knot = [0,1,1,2,2]
ts, Nt = bspline_func(knot)
plt.plot(ts, Nt)

plt.show()
