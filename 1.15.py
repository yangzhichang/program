import numpy
import matplotlib.pyplot
a, b = (0., 0.)
r = 4.5
theta = numpy.arange(0, 2*numpy.pi, 0.01)
x = a+r*numpy.cos(theta)
y = b+r*numpy.sin(theta)
fig = matplotlib.pyplot.figure()
axes = fig.add_subplot(111)
axes.plot(x, y)
axes.axis('equal')
matplotlib.pyplot.show()