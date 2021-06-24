"""Load CSV Files with Pandas"""

# Recommended approach - it is very flexible and returns the data into a DataFrame immediately
from pandas import read_csv

filename = '../../pima-indians-diabetes.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)

# URL-based
# url = 'https://goo.gl/vhm1eU'
# data = read_csv(url, names=names)

print(data.shape)
