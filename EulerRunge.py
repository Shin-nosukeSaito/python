import matplotlib.pyplot as plt
import numpy as np
from pylab import *



#初期値x(0)
x = 0.01
y = 0.01

#刻み幅
dt = 0.001
dt1 = 0.001


def g(t,x):
	return x*(1-x)

def f(t,y):
	return y*(1-y)

def j(t):
	return np.exp(t)

t2 = np.arange(0.0,1,0.01)


#計算

#plt.figure(1)

plt.subplot(111)

#まずはオイラー法
for i in range(200):
	t = i*dt
	#print("{0}","{1}".format(t,x))
	x = (1+dt)*x
	#plt.subplot(211)
	plt.grid(True)
	plt.plot(t,x,"ro-")
	
	
	#plt.plot(t,f(t),'k')

	#次にルンゲ・クッタ法
	t1 = i*dt1
	#print("{0}{1}".format(t,y))

	k1 = f(t,y)
	k2 = f(t1 + dt1*0.5, y + k1*dt1*0.5)
	k3 = f(t1 + dt1*0.5, y + k2*dt1*0.5)
	k4 = f(t1 + dt1, y + k3*dt1)
	y += (k1 + 2*k2 + 2*k3 + k4)*dt1/6
	#plt.subplot(212)
	plt.grid(True)
	plt.plot(t1,y,"bo-")

	#plt.plot(t2,j(t2),"kx")

#ぐらふのびょうが
plt.rcParams['font.family'] = 'Times New Roman' #全体のフォントを設定
plt.rcParams['font.size'] = 15 #フォントサイズを設定
plt.rcParams['axes.linewidth'] = 1.5 #軸の太さを設定。目盛りは変わらない
#plt.legend() # 凡例
plt.legend(['Eular','RungKutta'])
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()



