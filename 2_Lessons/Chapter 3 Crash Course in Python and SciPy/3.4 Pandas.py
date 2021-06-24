import numpy
import pandas

# 3.4.1 Series
myarray = numpy.array([1, 2, 3])
rownames = ['a', 'b', 'c']
myseries = pandas.Series(myarray, index=rownames)
print(myseries)
print(myseries[0])
print(myseries['a'])

# 3.4.2 DataFrame
myarray = numpy.array([[1, 2, 3], [4, 5, 6]])
rownames = ['a', 'b', 'c']
colnames = ['one', 'two', 'three']
mydataframe = pandas.DataFrame(myarray, index=rownames, columns=colnames)
print(mydataframe)
print('one column: {}'.format(mydataframe['one']))
print('one column: {}'.format(mydataframe.one))
