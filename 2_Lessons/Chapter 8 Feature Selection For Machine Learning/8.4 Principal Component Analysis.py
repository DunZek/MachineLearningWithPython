# Principal component Analysis (or PCA) - uses linear algebra to transform the dataset into a compressed form - a type
# of data reduction technique. You can choose the number of dimensions or principal components in the transformed result

# Feature Extraction with PCA
from pandas import read_csv
from sklearn.decomposition import PCA
# Load data
filename = '../../pima-indians-diabetes.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = read_csv(filename, names=names)
array = dataframe.values
# Separate array into input and output components
x = array[:,0:8]
y = array[:, 8]
# Feature extraction
pca = PCA(n_components=3)
fit = pca.fit(x)
# Summarize components
print("Explained Variance {}".format(fit.explained_variance_ratio_))
print(fit.components_)  # The transformed dataset of the 3 principal components will bare little resemblance to the
# source data
