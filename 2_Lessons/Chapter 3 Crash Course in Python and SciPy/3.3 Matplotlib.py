"""Matplotlib Crash Course"""

import matplotlib.pyplot as plt
import numpy

# 3.3.1 Line Plot
myarray = numpy.array([1, 2, 3])
plt.plot(myarray)
plt.xlabel('some x axis')
plt.ylabel('some y axis')
plt.show()

# 3.3.2 Scatter Plot
x = numpy.array([1, 2, 3])
y = numpy.array([2, 3, 6])
plt.scatter(x, y)
plt.xlabel('some x axis')
plt.ylabel('some y axis')
plt.show()