import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn import neighbors

cardata = pd.read_excel("Car.xlsx")
print(cardata[0:3])

X = cardata[["Buying", "Maintanance", "LugBoot"]].values
y = cardata[["Class"]]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

knn = neighbors.KNeighborsClassifier(n_neighbors=5, weights="uniform")
knn.fit(X_train, np.ravel(y_train))
knnprediction = knn.predict(X_test)

print(metrics.accuracy_score(knnprediction, y_test))
