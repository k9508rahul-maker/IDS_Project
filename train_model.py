import os
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder


# Create required folders
os.makedirs("dataset", exist_ok=True)
os.makedirs("model", exist_ok=True)


# Sample IDS dataset
data = {
    "packet_size": [
        120, 150, 200, 180, 130,
        900, 850, 950, 1000, 870,
        140, 160, 190, 210, 170,
        920, 880, 970, 910, 990
    ],

    "connection_count": [
        2, 3, 4, 3, 2,
        80, 70, 90, 100, 75,
        3, 2, 4, 5, 3,
        85, 95, 70, 88, 100
    ],

    "failed_connections": [
        0, 0, 1, 0, 0,
        15, 20, 18, 25, 17,
        0, 1, 0, 0, 1,
        22, 19, 30, 20, 27
    ],

    "duration": [
        10, 15, 20, 12, 18,
        2, 3, 1, 2, 4,
        14, 17, 21, 13, 16,
        2, 1, 3, 2, 1
    ],

    "label": [
        "Normal", "Normal", "Normal", "Normal", "Normal",
        "Attack", "Attack", "Attack", "Attack", "Attack",
        "Normal", "Normal", "Normal", "Normal", "Normal",
        "Attack", "Attack", "Attack", "Attack", "Attack"
    ]
}


# Create DataFrame
df = pd.DataFrame(data)

# Save dataset
df.to_csv("dataset/network_traffic.csv", index=False)

print("Dataset created successfully!")
print(df)


# Features
X = df[
    [
        "packet_size",
        "connection_count",
        "failed_connections",
        "duration"
    ]
]

# Target
y = df["label"]


# Convert labels into numbers
encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)


# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y_encoded,
    test_size=0.25,
    random_state=42,
    stratify=y_encoded
)


# Create Random Forest model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


# Train
model.fit(X_train, y_train)


# Prediction
predictions = model.predict(X_test)


# Accuracy
accuracy = accuracy_score(y_test, predictions)

print("\nModel Accuracy:", accuracy)


# Classification report
print("\nClassification Report:")

print(
    classification_report(
        y_test,
        predictions,
        target_names=encoder.classes_,
        zero_division=0
    )
)


# Save model
joblib.dump(model, "model/ids_model.pkl")

# Save label encoder
joblib.dump(encoder, "model/label_encoder.pkl")


print("\nModel saved successfully!")
print("Model: model/ids_model.pkl")
print("Encoder: model/label_encoder.pkl")