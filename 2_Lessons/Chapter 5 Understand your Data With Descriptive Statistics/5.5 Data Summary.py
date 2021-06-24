"""Class Distribution (Classification Only)"""

from pandas import read_csv
filename = '../../pima-indians-diabetes.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)
class_counts = data.groupby('class').size()
print(class_counts)  # Nearly double the number of observations with class 0 than with class 1 (onset of diabetes)
