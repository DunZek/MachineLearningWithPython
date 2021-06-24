"""NumPy Crash Course"""

import numpy

# 3.2.1 Create Array
mylist = [1 ,2 ,3]
myarray = numpy.array(mylist)
print(myarray)
print(myarray.shape)

# 3.2.2 Access Data
mylist = [[1, 2, 3], [4, 5, 6]]
myarray = numpy.array(mylist)
print(myarray)
print(myarray.shape)
print("First row: {}".format(myarray[0]))
print("last row: {}".format(myarray[-1]))
print("Specific row and col: {}".format(myarray[0, 2]))
print("Whole column: {}".format(myarray[:, 3]))

# 3.2.3 Arithmetic
myarray1 = numpy.array([2, 2, 2])
myarray2 = numpy.array([3, 3, 3])
print("Addition: {}".format(myarray1 + myarray2))
print("Multiplication: {}".format(myarray1 * myarray2))
