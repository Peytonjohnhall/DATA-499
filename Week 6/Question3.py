import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

def knn_height_weight(filepath):
    # Load dataset (Excel file)
    data = pd.read_excel(filepath)

    # Use correct column names
    X = data[['Height (cm)', 'Weight (kg)']]
    y = data['Class']

    # Split data (optional, just for evaluation)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Train KNN model
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X_train_scaled, y_train)

    # Predict for new person (170cm, 73kg)
    new_person = scaler.transform([[170, 73]])
    prediction = knn.predict(new_person)

    return prediction[0]

if __name__ == "__main__":
    result = knn_height_weight("KNNHeightWeight.xlsx")
    print("The new person (170cm, 73kg) belongs to class:", result)
