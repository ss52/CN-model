"""
CN model Mintec
"""
from scipy import integrate
import pylab
import numpy as np

k = 0.15        # leaching rate constant
g0 = 24.1       # total gold grade ppm
g_ref = 15 / 100  # refractory gold component of ore %
n = 1.5         # variable order leaching parameter

# Verninsaja results (CN 2 g/l)
res_x = [0, 2, 4, 24, 46]
res_y = [g0, 10.86, 8.16, 3.66, 3.57]

def Eq(g, t):    # f(x) Mintec CN model (Deventer 2001)
    return -k * ((g - g0 * g_ref) ** n)

time = np.linspace(0.0, 50.0)
y = integrate.odeint(Eq, g0, time)

pylab.plot(time, y, label="model")
pylab.plot(res_x, res_y, "bo", label="Exp")
pylab.xlabel('Time (h)')
pylab.ylabel('Au (ppm)')
pylab.legend()
pylab.grid()
pylab.show()

