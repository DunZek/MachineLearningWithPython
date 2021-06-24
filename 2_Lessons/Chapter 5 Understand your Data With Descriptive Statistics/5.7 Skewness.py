"""Skew of Univariate Distributions"""

# Skew - refers to a distribution that is assumed Gaussian (normal or bell curve) that is shifted or squashed in
# one direction or another.

# Skew for each attribute
from pandas import read_csv
filename = '../../pima-indians-diabetes.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)
skew = data.skew()
print(skew)  # Positive values are right skews and negative values are left skews
