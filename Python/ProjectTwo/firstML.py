# Check version of libraries
print('This is my first Python ML trial\n')

# Python
import sys
print('Python: {}\n'.format(sys.version))

# Scipy
import scipy as sp
print('Scipy: {}\n'.format(sp.__version__))

# Numpy
import numpy as np
print('Numpy: {}\n'.format(np.__version__))

# Pandas
import pandas as pd
print('Pandas: {}\n'.format(pd.__version__))

# Panda packages
from pandas.plotting import scatter_matrix

# Sklearn
import sklearn as sl
print('Sklearn: {}\n'.format(sl.__version__))

# Sklearn packages
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

# Matplotlib
import matplotlib as mp
print('Matplotlib: {}\n'.format(mp.__version__))

# Matplotlib packages
from matplotlib import pyplot

# Load dataset from csv file
iris = '../Datasets/iris.csv'

# Define header row
col_names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']

# Read CSV file with panda and add header column
dataset = pd.read_csv(iris, names=col_names)

# Showing only the shape of dataset (rows, columns)
print('Shape of dataset: {}\n'.format(dataset.shape))

# Showing only information about the axes
print(dataset.axes, '\n')

# Showing only information about the head column
print(dataset.columns, '\n')

# Showing only information about the datatypes
print(dataset.dtypes, '\n')

# Printing whole dataset
print('Iris dataset:\n', dataset, '\n')

# Showing first 10 rows from head
print(dataset.head(10), '\n')

# Statistical Summary of each attribute
print(dataset.describe(), '\n')

# Class distributions
print(dataset.groupby('sepal-length').size(), '\n')
print(dataset.groupby('sepal-width').size(), '\n')
print(dataset.groupby('petal-length').size(), '\n')
print(dataset.groupby('petal-width').size(), '\n')
print(dataset.groupby('class').size(), '\n')

# Box and univariate whisker plots
dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
pyplot.show()

# Univariate histograms
dataset.hist()
pyplot.show()

# Multivariate scatter plot matrices
scatter_matrix(dataset)
pyplot.show()

# Split-out validation dataset
array = dataset.values
X = array[:,0:4]
y = array[:,4]
X_train, X_validation, Y_train, Y_validation = train_test_split(X, y, test_size=0.20, random_state=1)

# Spot check algorithms
# Linear algorithms:
#   LR = Logistic Regression
#   LDA = Linear Discriminant Analysis
# Nonlinear algorithms:
#   KNN = K-Nearest Neighbors
#   CART = Classification and Regression Trees
#   GNB = Gaussian Naive Bayes
#   SVM = Support Vector Machines
models = []
models.append(('LR', LogisticRegression(solver='liblinear', multi_class='ovr')))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('GNB', GaussianNB()))
models.append(('SVM', SVC(gamma='auto')))

# Evaluate each model in turn
results = []
names = []
for name, model in models:
	kfold = StratifiedKFold(n_splits=10, random_state=1, shuffle=True)
	cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring='accuracy')
	results.append(cv_results)
	names.append(name)
	print('%s: %f (%f)' % (name, cv_results.mean(), cv_results.std()))

print()

# Compare algorithms
pyplot.boxplot(results, labels=names)
pyplot.title('Algorithm Comparison')
pyplot.show()

# Make predictions on validation dataset
model = SVC(gamma='auto')
model.fit(X_train, Y_train)
predictions = model.predict(X_validation)

# Evaluate predictions
print(accuracy_score(Y_validation, predictions))
print(confusion_matrix(Y_validation, predictions))
print(classification_report(Y_validation, predictions))
