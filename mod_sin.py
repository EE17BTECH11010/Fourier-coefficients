from scipy.integrate import quad
import numpy as np
from math import sin,cos

Vr = 12*np.sqrt(2) - 1.4
f = 100
n = int(input())

def func(x):
	return Vr*2*sin(x)*cos(n*x)/np.pi

f = (-4*Vr)/(np.pi*(n^2 - 1))


ans, err = quad(func, 0, np.pi)
print(ans)

