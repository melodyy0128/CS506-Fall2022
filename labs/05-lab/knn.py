import matplotlib.pyplot as plt

# unused but required import for doing 3d projections with matplotlib < 3.2
import mpl_toolkits.mplot3d

class KNN:

    def __init__(self, k, X_train, y_train):
        self.k = k
        self.X_train = X_train
        self.y_train = y_train
        self.distance_matrix = None
    
    def train(self):
        self.distance_matrix = ...

    def predict(self, example):
        return ...

    def get_error(self, predicted, actual):
        return sum(map(lambda x : 1 if (x[0] != x[1]) else 0, zip(predicted, actual))) / len(predicted)

    def test(self, test_input, labels):
        actual = labels
        predicted = (self.predict(test_input))
        print("error = ", self.get_error(predicted, actual))


from sklearn import datasets
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split

# Add the dataset here
iris = datasets.load_iris()
X = iris.data  # we only take the first two features.
y = iris.target

print(X.shape)
# Split the data 70:30 and predict.
num_data = len(X)
# import sklearn
# from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=4)

print(X_train.shape)
print(X_test.shape)

# create a new object of class KNN

# plot a boxplot that is grouped by Species. 
# You may have to ignore the ID column

# predict the labels using KNN

# use the test function to compute the error
