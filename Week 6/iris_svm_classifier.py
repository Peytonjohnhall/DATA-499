import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

datairis = datasets.load_iris()
X = datairis.data
y = datairis.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

rf = RandomForestClassifier()

rf.fit(X_train, y_train)
rfprediction = rf.predict(X_test)
print(metrics.accuracy_score(rfprediction, y_test))
