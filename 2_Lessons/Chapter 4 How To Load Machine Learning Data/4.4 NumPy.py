"""Load CSV Files with NumPy"""

# Assumes no header row and all data has the same format
from numpy import loadtxt
filename = '../../pima-indians-diabetes.csv'
raw_data = open(filename, 'rb')
data = loadtxt(raw_data, delimiter=',')
print(data.shape)
