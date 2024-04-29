import matplotlib.pyplot as plt
import pandas as pd
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score

def adaboost(df):
    X = df.drop('Grade', axis=1)
    y = df['Grade']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    print(X_train.shape)
    print(X_test.shape)

    model = AdaBoostClassifier(n_estimators=50, learning_rate=0.5, algorithm='SAMME', random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    model.score(X_test, y_test)

    print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")

DATASETS = ['dataset/TCGA_GBM_LGG_Mutations_all.csv', './dataset/TCGA_InfoWithGrade.csv']
adaboost(pd.read_csv(DATASETS[1]))