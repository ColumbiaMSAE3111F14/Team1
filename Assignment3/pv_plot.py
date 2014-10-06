# Team 1: Sean Ballinger, Ben Israeli, Kathleen Kennedy,
# and Chris Florencio-Aleman
# Homework 3; PP6

import numpy as np
import matplotlib.pyplot as plt

R = 8.205736e-5
T = 25 + 273.14
K = 7/float(5)  # We assumed that the gas was diatomic


def calc_v(n, p, T):
    V = (n*R*T)/float(p)
    return V

# Point A
a_y = 1
a_x = calc_v(1, 1, T)

# Point B
b_y = 3
b_x = calc_v(1, 3, T)

# Calculating isothermal, adiabatic, and linear transformations
y_isotherm = np.linspace(1, 3, 60)
x_isotherm = np.array([calc_v(1, p, T) for p in y_isotherm])

adiabat_const = 1 * calc_v(1, 1, T)**K
y_adiabat = np.linspace(1, 3, 60)
x_adiabat = np.array([(adiabat_const/p)**(1/K) for p in y_adiabat])

m = (y_adiabat[59] - y_adiabat[0])/(x_adiabat[59] - x_adiabat[0])
c = 1 - m * calc_v(1, 1, T)
y_linear = np.linspace(1, 3, 60)
x_linear = np.array([(p-c)/m for p in y_linear])

# Calculating work
print 'Isothermal transformation work: ', np.trapz(y_isotherm, x_isotherm)
print 'Adiabat transformation work: ', np.trapz(y_adiabat, x_adiabat)
print 'Linear transformation work: ', np.trapz(y_linear, x_linear)

# Calculating heat transfers:
# For isothermal transformation delta U is 0, so Q = W
print 'Isothermal transformation Q: ', np.trapz(y_isotherm, x_isotherm)

# For adiabatic transformation Q is by definition 0
print 'Adiabat transformation Q: 0'

# For the linear transformation Q = delta U + W,
# and delta U = C_v * (T_2-T_1)
T_at_C = (3 * x_linear[59])/(1 * R)
Q = (5/float(2)*R)*(T_at_C - T) + np.trapz(y_linear, x_linear)
print 'Linear transformation Q: ', Q

plt.plot(a_x, a_y, 'o')
plt.annotate('A', (a_x, a_y))
plt.plot(b_x, b_y, 'o')
plt.annotate('B', (b_x, b_y))
plt.axis([0, 0.027, 0, 4])
plt.plot(x_isotherm, y_isotherm)
plt.plot(x_adiabat, y_adiabat)
plt.plot(x_linear, y_linear)
plt.plot(x_adiabat[59], y_adiabat[59], 'o')
plt.annotate('C', (x_adiabat[59], y_adiabat[59]))
plt.xlabel('m^3')
plt.ylabel('atm')
plt.title('Transformations of an Ideal Gas')
plt.show()
