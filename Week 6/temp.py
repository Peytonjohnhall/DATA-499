import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
from sklearn.model_selection import train_test_split

datairis = datasets.load_iris()
X = datairis.data
y = datairis.target

nb = GaussianNB()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

nb.fit(X_train, y_train)
nbprediction = nb.predict(X_test)

print(metrics.accuracy_score(nbprediction, y_test))
print(nb.predict([[5, 2.6, 5.9, 1.8]]))
print(datairis)