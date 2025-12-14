import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

def random_forest_ownhouse(filepath):
    # Load dataset
    data = pd.read_excel(filepath)

    # Features and target
    X = data[['Age', 'OwnAHouse']]
    y = data['BuysProduct']

    # Encode target ("Yes"/"No") into numeric
    le = LabelEncoder()
    y = le.fit_transform(y)   # Yes=1, No=0

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train Random Forest
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Predict for 32-year-old without a house
    new_person = [[32, 0]]
    prediction = model.predict(new_person)

    # Convert back to Yes/No
    decision = le.inverse_transform(prediction)[0]

    return decision

if __name__ == "__main__":
    result = random_forest_ownhouse("OwnHouse.xlsx")
    print("Decision for 32-year-old without a house:", result)
