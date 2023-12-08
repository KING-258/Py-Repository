import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def trainvstest(x, y):
    trX, tesX, trY, tesY = train_test_split(
        x, y, test_size=0.2, random_state=42
    )
    model = LogisticRegression(max_iter=1000)
    model.fit(trX, trY)
    prdY = model.predict(tesX)
    return accuracy_score(tesY, prdY)


def main():
    df = pd.read_csv("Indian Liver Patient Dataset (ILPD).csv",
                     names=["Age", "Gender", "TB", "DB", "Alkphos", "Sgpt", "Sgot", "TP", "ALB", "A/G Ratio",
                            "Liver Disease"])
    df.dropna(inplace=True)
    df["Gender"] = df["Gender"].apply(lambda x: 1 if x == 'Male' else 0)
    X = df.drop("Liver Disease", axis=1)
    y = df["Liver Disease"]
    trX, tesX, trY, tesY = train_test_split(X, y, test_size=0.2, random_state=42)
    scaler = StandardScaler()
    trX = scaler.fit_transform(trX)
    tesX = scaler.transform(tesX)
    trX, tesX, trY, tesY = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LogisticRegression()
    model.fit(trX, trY)
    prdY = model.predict(tesX)
    accuracy = accuracy_score(tesY, prdY)
    confusion_mat = confusion_matrix(tesY, prdY)
    class_report = classification_report(tesY, prdY)
    print(df.describe())
    print(f"Accuracy: {accuracy}")
    print(f"Confusion Matrix:\n{confusion_mat}")
    print(f"Report : \n{class_report}")
    plt.figure(figsize=(8, 6))
    plt.imshow(confusion_mat, interpolation='nearest', cmap=plt.cm.Blues)
    plt.title('Disparity in Readings')
    plt.colorbar()
    plt.xticks([0, 1])
    plt.yticks([0, 1])
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.show()
    num_iterations = 10
    accuracy_scores = []

    for _ in range(num_iterations):
        accuracy = trainvstest(X, y)
        accuracy_scores.append(accuracy)
    plt.plot(range(1, num_iterations + 1), accuracy_scores, marker="o")
    plt.xlabel("Iteration")
    plt.ylabel("Accuracy")
    plt.title("Accuracy Curve")
    plt.show()


if __name__ == "__main__":
    main()
