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

# Sklearn
import sklearn as sl
print('Sklearn: {}\n'.format(sl.__version__))

# Matplotlib
import matplotlib as mp
print('Matplotlib: {}\n'.format(mp.__version__))

# Load dataset from csv file
iris = '../Datasets/iris.csv'

# Define header column
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

# Showing first 15 rows from head
print(dataset.head(15), '\n')
