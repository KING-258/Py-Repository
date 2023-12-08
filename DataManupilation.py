import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler
def main():
    # Step 1: Load and preprocess the dataset
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00225/Indian%20Liver%20Patient%20Dataset%20(ILPD).csv"
    columns = ['age', 'total_bilirubin', 'direct_bilirubin', 'alkaline_phosphotase',
               'alamine_aminotransferase', 'aspartate_aminotransferase', 'total_proteins',
               'albumin', 'albumin_and_globulin_ratio', 'liver_disease']

    data = pd.read_csv(url, names=columns)

    # Data exploration and preprocessing
    # (You may need to handle missing values, encode categorical variables, etc.)

    # Step 2: Train-Test Split
    X = data.drop('liver_disease', axis=1)
    y = data['liver_disease']
    X_train, X_test, y_train, tesY = train_test_split(X, y, test_size=0.2, random_state=42)

    # Step 3: Data preprocessing (scaling)
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Step 4: Model Selection
    model = LogisticRegression()

    # Step 5: Model Training
    model.fit(X_train, y_train)

    # Step 6: Model Evaluation
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(tesY, y_pred)
    print(f"Accuracy: {accuracy}")
    print(classification_report(tesY, y_pred))

    # Confusion Matrix
    cm = confusion_matrix(tesY, y_pred)
    plt.figure(figsize=(8, 6))
    plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
    plt.title('Confusion Matrix')
    plt.colorbar()
    plt.xticks([0, 1])
    plt.yticks([0, 1])
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.show()


    # Predict if a person of age 49 has the disease or not
    age_49_features = [[49, 1.0, 0.9, 650, 55, 42, 7.6, 2.6, 0.55]]  # Assuming some values for the other features
    age_49_features = scaler.transform(age_49_features)
    prediction = model.predict(age_49_features)
    print(f"Predicted class for age 49: {'Disease' if prediction[0] == 1 else 'No Disease'}")

if __name__ == "__main__" :
    main()