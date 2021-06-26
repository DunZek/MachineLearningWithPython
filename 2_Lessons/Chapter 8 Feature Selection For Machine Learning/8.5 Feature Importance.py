# Random Forest / Extra Trees - bagged decision trees which can be used to estimate the importance of features

# Feature Importance with Extra Trees classifier
from pandas import read_csv
from sklearn.ensemble import ExtraTreesClassifier
# Load data
filename = '../../pima-indians-diabetes.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = read_csv(filename, names=names)
array = dataframe.values
# Separate array into input and output components
x = array[:, 0:8]
y = array[:, 8]
# Feature extraction
model = ExtraTreesClassifier()
model.fit(x, y)
# Components
print(model.feature_importances_)  # we are given an importance score for each attribute (greatest 3 = plas, age, mass).
# Bigger scores suggest greater importance in the model.
