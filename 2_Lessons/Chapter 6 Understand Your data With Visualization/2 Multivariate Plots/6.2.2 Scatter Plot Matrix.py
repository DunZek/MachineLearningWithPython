# Scatter plots - useful for spotting structured relationships between variables
# Attributes with structured relationships may also be correlated and good candidates for removal from your dataset
from matplotlib import pyplot
from pandas.plotting import scatter_matrix
from pandas import read_csv
filename = '../../../pima-indians-diabetes.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)
scatter_matrix(data)
pyplot.show()
