"""Dimensions of Your Data"""

from pandas import read_csv
filename = '../../pima-indians-diabetes.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)
shape = data.shape
print(shape)  # 768 rows and 9 columns
