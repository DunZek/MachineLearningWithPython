# Density plots - used to visualize the distribution of the numeric values of each attribute

# Univariate Density Plots
from matplotlib import pyplot
from pandas import read_csv
filename = '../../../pima-indians-diabetes.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)
data.plot(kind='density', subplots=True, layout=(3, 3), sharex=False)
pyplot.show()
