"""Descriptive Statistics"""

# describe() <- lists 8 statistical properties of each attribute (column):
# Count
# Mean
# Standard Deviation
# Minimum Value
# 25th Percentile
# 50th Percentile (Median)
# 75th Percentile
# Maximum value

# Statistical Summary
from pandas import read_csv, set_option
filename = '../../pima-indians-diabetes.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)
set_option('display.width', 100)
set_option('precision', 3)
description = data.describe()
print(description)
