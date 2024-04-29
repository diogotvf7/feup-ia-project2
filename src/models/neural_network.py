"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.metrics import classification_report
from src.constants import GENES

def logistic_regression(df):
    X = df.drop('Grade', axis=1)
    y = df['Grade']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    print(X_train.shape)
    print(X_test.shape)

    model = LogisticRegression(max_iter=2000)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    model.score(X_test, y_test)

    print(confusion_matrix(y_test, y_pred))
    cm = confusion_matrix(y_test, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm)
    disp.plot()
    plt.show()

    cr = classification_report(y_test, y_pred)
    print(cr)

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

Neural network::
sklearn.neural_network.MLPClassifier
"""
import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.metrics import classification_report

def neural_network(df):
    X = df.drop('Grade', axis=1)
    y = df['Grade']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    print(X_train.shape)
    print(X_test.shape)

    model = MLPClassifier(hidden_layer_sizes=(100, 100), max_iter=1000)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    model.score(X_test, y_test)

    cm = confusion_matrix(y_test, y_pred)
    print(cm)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm)
    disp.plot()

    cr = classification_report(y_test, y_pred)
    print(cr)

    DATASETS = ['dataset/TCGA_GBM_LGG_Mutations_all.csv', './dataset/TCGA_InfoWithGrade.csv']
    neural_network(pd.read_csv(DATASETS[1]))

    


