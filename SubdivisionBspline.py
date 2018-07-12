import numpy as np
import matplotlib.pyplot as plt
import sys

class myEventHandler(object):
    def __init__(self):
        cid = fig.canvas.mpl_connect('button_press_event', self.oncpaint)
        pid = fig.canvas.mpl_connect('key_press_event', self.press)
        self.points = []
        self.cx = []
        self.cy = []

    def oncpaint(self,event):
        if event.button == 1:
            self.points.append([event.xdata,event.ydata])
            self.cx.append(event.xdata)
            self.cy.append(event.ydata)
            ax.plot(event.xdata, event.ydata, '.', color='r')
            fig.canvas.draw()

        elif event.button == 3:
            self.cx.append(self.cx[0])
            self.cy.append(self.cy[0])
            plt.plot(self.cx,self.cy)
            plt.show()

    def press(self,event):
        xs = []
        ys = []
        if event.key == '1' or event.key == '2' or event.key == '3':
            ndpoint = np.array(self.points)
            ndpoint = subdivision(self.points,int(event.key))
            self.points = ndpoint.tolist()
            for px,py in self.points:
                xs.append(px)
                ys.append(py)
            xs.append(self.points[0][0])
            ys.append(self.points[0][1])
            plt.plot(xs,ys)
            plt.show()
            
        elif event.key == '4':
            ndpoint = np.array(self.points)
            ndpoint = fourpointScheme(self.points)
            self.points = ndpoint.tolist()
            for px,py in self.points:
                xs.append(px)
                ys.append(py)
            xs.append(self.points[0][0])
            ys.append(self.points[0][1])
            plt.plot(xs,ys)
            plt.show()
        else:
            print ('press 1, 2, or 3 key. The Degree of Subdivision.')



def subdivision(points,m):
    n = len(points)
    Mat = np.zeros((n, 2 * n))

    combination = []
    if m == 1:
        combination = [1,2,1]
    elif m == 2:
        combination = [1,3,3,1]
    elif m == 3:
        combination = [1,4,6,4,1]
    else:
        print ('m is not in range. please input 1, 2, or 3 as m')
        return None

    for i in range(-1,n - 1):
        for j in range(m + 2):
            Mat[i + 1][(2 * i + j) % (2 * n)] = combination[j]

    Mat = Mat.T * 1 / (2 ** m)
    new_points = np.dot(Mat, points)
    return new_points

def fourpointScheme(points):
    n = len(points)
    Mat = np.zeros((2 * n,n))

    for i in range(2 * n):
        if i % 2 == 0:
            Mat[i][i // 2] = 16
        else:
            Mat[i][(i // 2 + 2) % n] = -1
            Mat[i][(i // 2 + 1) % n] = 9
            Mat[i][(i // 2) % n] = 9
            Mat[i][(i // 2 - 1) % n] = -1

    Mat = Mat * 1 / (16)
    new_points = np.dot(Mat, points)
    return new_points

def main():
    global x, y, fig, ax
    x = []
    y = []
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(x, y)
    handler = myEventHandler()
    ax.set_xlim([0,5])
    ax.set_ylim([0,5])
    plt.show()

if __name__ == "__main__":
    main()
