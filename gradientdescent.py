#function f(x)=x^2+5*sin(x)
import numpy as np
import matplotlib.pyplot as plt
import math 
def f(x):
    return x**2+np.sin(x)

def grad(x):
    return 2*x + 5*np.cos(x)

def myGD(alpha,x0):
    x=[x0]
    for i in range(100):
        x_new=x[-1]-alpha*grad(x[-1])
        if abs(grad(x_new))<1e-6:
            break
        x.append(x_new)
    return (x,i)


beg= -6
end=6
leng=math.pi/1000

x=np.linspace(beg,end,leng)

y=f(x)
pltGrad=grad(x)

(x1,i1)=myGD(0.1,-5)

print("Solution x1 = %f, cost = %f, obtained after %d iterations"%(x1[-1], f(x1[-1]), i1))

#plt.plot(x,y,'ro',markersize=0.1)
#plt.plot(x,pltGrad,'bo',markersize=0.1)
#plt.show()