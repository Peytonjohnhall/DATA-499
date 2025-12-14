import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

def svm_predict(filepath):
    # Load dataset
    data = pd.read_excel(filepath)

    # Features and target
    X = data[['FeatureX1', 'FeatureX2']]
    y = data['Class']

    # Train/test split (for evaluation, optional)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Train SVM with linear kernel
    model = SVC(kernel='linear', random_state=42)
    model.fit(X_train_scaled, y_train)

    # Predict for new data point (3.9, 9.0)
    new_point = scaler.transform([[3.9, 9.0]])
    prediction = model.predict(new_point)

    return prediction[0]

if __name__ == "__main__":
    result = svm_predict("SVCpredict.xlsx")
    print("Prediction for (X1=3.9, X2=9.0):", result)
