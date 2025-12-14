from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)

# a) Divide the data
def divide_data():
    data = load_breast_cancer()
    X = data.data
    y = data.target
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

# b) Naive Bayes
def naive_bayes(X_train, X_test, y_train, y_test):
    model = GaussianNB()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    return accuracy_score(y_test, y_pred)

# c) Support Vector Machine with scaling
def support_vector_machine(X_train, X_test, y_train, y_test):
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    model = SVC(kernel='linear', random_state=42)
    model.fit(X_train_scaled, y_train)
    y_pred = model.predict(X_test_scaled)
    return accuracy_score(y_test, y_pred)

# d) Random Forest Classifier
def random_forest_classifier(X_train, X_test, y_train, y_test, n_estimators=100):
    model = RandomForestClassifier(n_estimators=n_estimators, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    return accuracy_score(y_test, y_pred)

# e) Neural Network with scaling (fixed, warning-free)
def neural_network(X_train, X_test, y_train, y_test):
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    model = MLPClassifier(
        hidden_layer_sizes=(100, 100, 100),
        max_iter=1000, # increased iterations
        solver='adam', # more stable for this dataset
        random_state=42
    )
    model.fit(X_train_scaled, y_train)
    y_pred = model.predict(X_test_scaled)
    return accuracy_score(y_test, y_pred)

# f) KNN with scaling
def KNN(X_train, X_test, y_train, y_test, n_neighbors=5):
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    model = KNeighborsClassifier(n_neighbors=n_neighbors)
    model.fit(X_train_scaled, y_train)
    y_pred = model.predict(X_test_scaled)
    return accuracy_score(y_test, y_pred)

if __name__ == "__main__":
    X_train, X_test, y_train, y_test = divide_data()

    print("Naive Bayes Accuracy:", naive_bayes(X_train, X_test, y_train, y_test))
    print("SVM Accuracy:", support_vector_machine(X_train, X_test, y_train, y_test))
    print("Random Forest Accuracy:", random_forest_classifier(X_train, X_test, y_train, y_test))
    print("Neural Network Accuracy:", neural_network(X_train, X_test, y_train, y_test))
    print("KNN Accuracy:", KNN(X_train, X_test, y_train, y_test))

    # g) Best classifier
    scores = {
        "Naive Bayes": naive_bayes(X_train, X_test, y_train, y_test),
        "SVM": support_vector_machine(X_train, X_test, y_train, y_test),
        "Random Forest": random_forest_classifier(X_train, X_test, y_train, y_test),
        "Neural Network": neural_network(X_train, X_test, y_train, y_test),
        "KNN": KNN(X_train, X_test, y_train, y_test)
    }
    best = max(scores, key=scores.get)
    print("Best Classifier:", best, "with Accuracy:", scores[best])
