import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

datairis = datasets.load_iris()
X = datairis.data
y = datairis.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

nnw = MLPClassifier(hidden_layer_sizes=(10, 10, 10), max_iter=500)
nnw.fit(X_train, y_train)
nnwprediction = nnw.predict(X_test)

print(metrics.accuracy_score(nnwprediction, y_test))
print(nnw.predict([[5, 2.6, 5.9, 1.8]]))
