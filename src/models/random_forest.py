import matplotlib.pyplot as plt
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score

def random_forest(df):
    X = df.drop('Grade', axis=1)
    y = df['Grade']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    print(X_train.shape)
    print(X_test.shape)

    model = RandomForestClassifier(n_estimators=150, criterion='gini', min_samples_split=2, min_samples_leaf=2, max_depth=None, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    model.score(X_test, y_test)

    print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")

DATASETS = ['dataset/TCGA_GBM_LGG_Mutations_all.csv', './dataset/TCGA_InfoWithGrade.csv']
random_forest(pd.read_csv(DATASETS[1]))