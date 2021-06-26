# Feature Extraction with Univariate Statistical Tests (Chi-squared for classification)
from numpy import set_printoptions
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from pandas import read_csv
# Load data
filename = "../../pima-indians-diabetes.csv"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = read_csv(filename, names=names)
array = dataframe.values
# Separate array into input and output components
X = array[:, 0:8]
Y = array[:, 8]
# Feature extraction
test = SelectKBest(score_func=chi2, k=4)  # select 4 of the best features
fit = test.fit(X, Y)
# Summarize scores
set_printoptions(precision=3)
print(fit.scores_)  # scores for each attribute
features = fit.transform(X)
# Summarize selected features
print(features[0:5, :])  # score of the 4 attributes chosen (those with the highest scores)
