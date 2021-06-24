# Standardization <- best used for attributes with a Gaussian distribution

# Standardize data (0 mean, 1 stdev)
from sklearn.preprocessing import StandardScaler
from numpy import set_printoptions
from pandas import read_csv
filename = '../../pima-indians-diabetes.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = read_csv(filename, names=names)
array = dataframe.values
# Seperate array into input and output components
x = array[:, 0:8]
y = array[:, 8]
# Standardize data with scikit-learn using StandardScaler() class
scaler = StandardScaler().fit(x)
rescaled_x = scaler.transform(x)
# Summarize transformed data
set_printoptions(precision=3)
print(rescaled_x[0:5, :])  # <- values for each attribute will have a mean value of 0 and standard deviation of 1
