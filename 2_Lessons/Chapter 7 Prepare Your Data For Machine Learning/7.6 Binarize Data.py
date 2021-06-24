# Data can be transformed using a binary threshold. Binarizing data includes equating values to either 0 or 1 whether
# these values are below the threshold or above it respectively.
# Useful for when attributes need crisp values, feature engineering, and when features need to be added

# binarization
from sklearn.preprocessing import Binarizer
from numpy import set_printoptions
from pandas import read_csv
filename = '../../pima-indians-diabetes.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = read_csv(filename, names=names)
array = dataframe.values
# separate array into input and output components
x = array[:, 0:8]
y = array[:, 8]
# Binarize data with scikit-learn using the Binarizer class
binarizer = Binarizer(threshold=0.0).fit(x)
binary_x = binarizer.transform(x)
# summarize transformed data
set_printoptions(precision=3)
print(binary_x[0:5, :])
