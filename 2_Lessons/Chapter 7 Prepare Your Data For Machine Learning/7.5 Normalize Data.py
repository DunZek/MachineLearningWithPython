# Normalizing <- rescaling each observation (row) to have a length of 1 (called a unit norm or vector with the length of
# 1 in linear algebra. Useful pre-processing method for sparse datasets (lots of zeros) with attributes of varying
# scales when using algorithms that weight input values (neural networks and algorithms) that use distances measures
# such as kNN

# Normalize data (length of 1)
from sklearn.preprocessing import Normalizer
from numpy import set_printoptions
from pandas import read_csv
filename = '../../pima-indians-diabetes.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = read_csv(filename, names=names)
array = dataframe.values
# separate array into input and output components
x = array[:, 0:8]
y = array[:, 8]
# Normalize data with scikit-learn using Normalizer class
scaler = Normalizer().fit(x)
normalized_x = scaler.transform(x)
# summarize transformed data
set_printoptions(precision=3)
print(normalized_x[0:5, :])  # <- the rows are normalized to length 1
