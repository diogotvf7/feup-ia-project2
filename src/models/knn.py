import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.metrics import classification_report
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def knn(df):
    X = df.drop('Grade', axis=1)
    y = df['Grade']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    print(X_train.shape)
    print(X_test.shape)

    model = KNeighborsClassifier(n_neighbors=7, metric='minkowski')
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    model.score(X_test, y_test)

    cm = confusion_matrix(y_test, y_pred)
    print(cm)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm)

    print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")

DATASETS = ['dataset/TCGA_GBM_LGG_Mutations_all.csv', './dataset/TCGA_InfoWithGrade.csv']
knn(pd.read_csv(DATASETS[1]))