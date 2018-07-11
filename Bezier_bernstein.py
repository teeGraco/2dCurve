import matplotlib.pyplot as plt

def facto(n):
    li = [1]
    i = 1
    while(i < n):
        li.append((len(li) + 1) * li[len(li) - 1])
        i += 1
    return li
#print (facto(20))

def Combination(n,k):
    li = facto(n)
    return li[n - 1] // (li[k - 1] * li[n - k - 1])

def Combination(n):
    li = facto(n)
    combi = [1]
    for num in range(1,n):
        combi.append(li[n - 1] // (li[num - 1] * li[n - num - 1]))
    combi.append(1)
    return combi

def Bernstein_polynomial(n,i,d):
    bern = []
    ts = []
    combi = Combination(n)
    if n >= i:
        for num in range(d + 1):
            ts.append(num / d)
        for t in ts:
            bern.append(combi[i] * t ** i * (1 - t) ** (n - i))
        return ts, bern
    else:
        return 0

n = int(input('Input the order of Bernstein Polynomial >> '))

i = 0
while i <= n:
    x,y = Bernstein_polynomial(n,i,40)
    s = 'Lavel' + str(i)
    plt.plot(x,y,label = s)
    i += 1
plt.show()
