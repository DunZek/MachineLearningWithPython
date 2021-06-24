# Histograms - Visualize the distribution of numeric values within each attribute

# Univariate Histograms
from matplotlib import pyplot
from pandas import read_csv
filename = '../../../pima-indians-diabetes.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)
data.hist()
pyplot.show()
