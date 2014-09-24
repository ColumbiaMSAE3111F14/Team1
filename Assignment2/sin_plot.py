from pylab import *
import math

if len(sys.argv) > 2:
    wavelength = float(sys.argv[1])
    amplitude = float(sys.argv[2])
else:
    wavelength = float(raw_input('Enter wavelength: '))  # use input() in Python 3
    amplitude = float(raw_input('Enter amplitude: '))

x_max = 10
resolution = 100

x_data = [float(i)/resolution for i in xrange(0, x_max*resolution)]
y_data = [amplitude*math.sin(i*2*math.pi/wavelength) for i in x_data]

fig = figure(1)
plt.plot(x_data, y_data, '-')
plt.show(fig)
