import pandas as pd
from src.constants import DATASET
from src.models.logistic_regression import logistic_regression
from src.models.knn import knn

df = pd.read_csv(DATASET)
#logistic_regression(df)

knn(df)
