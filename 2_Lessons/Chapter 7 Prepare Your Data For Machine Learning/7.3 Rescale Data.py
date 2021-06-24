# Rescale data (between 0 and 1) <- rescale attributes to fit the same scale for the ML algorithm.
# Also called as normalization. Attributes are rescaled into a range between 0 and 1.
# Useful for algorithms like gradient descent, algorithms that weight inputs (regression and neural networks), and
# algorithms that use distance measures like kNN.
from numpy import set_printoptions
from sklearn.preprocessing import MinMaxScaler
from pandas import read_csv
filename = '../../pima-indians-diabetes.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = read_csv(filename, names=names)
array = dataframe.values
# Separate array into input and output components
x = array[:, 0:8]  # 1-7
y = array[:, 8]  # class
# Rescale data with scikit-learn using MixMaxScaler class
scaler = MinMaxScaler(feature_range=(0, 1))
rescaled_x = scaler.fit_transform(x)
# Summarize transformed data
set_printoptions(precision=3)  # floating-point precision
print(rescaled_x[0:5, :])  # <- rescaling of values will now result in the attributes being ranged between 0 and 1

