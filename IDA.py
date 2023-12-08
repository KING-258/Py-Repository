import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

def get_user_input():
    fixed_acidity = float(input("Enter fixed acidity: "))
    volatile_acidity = float(input("Enter volatile acidity: "))
    citric_acid = float(input("Enter citric acid: "))
    residual_sugar = float(input("Enter residual sugar: "))
    chlorides = float(input("Enter chlorides: "))
    free_sulfur_dioxide = float(input("Enter free sulfur dioxide: "))
    total_sulfur_dioxide = float(input("Enter total sulfur dioxide: "))
    density = float(input("Enter density: "))
    pH = float(input("Enter pH: "))
    sulphates = float(input("Enter sulphates: "))
    alcohol = float(input("Enter alcohol content: "))

    data = {
        'fixed acidity': [fixed_acidity],
        'volatile acidity': [volatile_acidity],
        'citric acid': [citric_acid],
        'residual sugar': [residual_sugar],
        'chlorides': [chlorides],
        'free sulfur dioxide': [free_sulfur_dioxide],
        'total sulfur dioxide': [total_sulfur_dioxide],
        'density': [density],
        'pH': [pH],
        'sulphates': [sulphates],
        'alcohol': [alcohol],
    }

    return pd.DataFrame(data)

from sklearn.datasets import load_wine
wine = load_wine()
X = wine.data
y = (wine.target == 1).astype(int)  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LogisticRegression()
model.fit(X_train, y_train)
user_data = get_user_input()
prediction = model.predict(user_data)
if prediction[0] == 1:
    print("The model predicts that the wine is of good quality.")
else:
    print("The model predicts that the wine is of bad quality.")
plt.figure(figsize=(10, 6))
plt.bar(user_data.columns, user_data.values.flatten(), color='purple')
plt.title('Entered Wine Details')
plt.xlabel('Features')
plt.ylabel('Values')
plt.show()