# Recursive Feature Elimination (RFE) - works by recursively removing attributes to build a model on those attributes
# that remain. Uses model accuracy to identify attributes and combinations thereof that contribute the most to predict
# the target attribute.

# Feature Extraction with RFE
from pandas import read_csv
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
# Load data
filename = '../../pima-indians-diabetes.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = read_csv(filename, names=names)
array = dataframe.values
# Separate dataframe into input and output components
x = array[:, 0:8]
y = array[:, 8]
# Feature extraction
model = LogisticRegression()
rfe = RFE(model, 3)
fit = rfe.fit(x, y)
print('Num Features: {}'.format(fit.n_features_))  # Number of chosen top features
print('Selected Features: {}'.format(fit.support_))  # Top 3 chosen features marked True
print('Feature Ranking: {}'.format(fit.ranking_))  # Chooses top 3 features (preg, mass, pedi)
