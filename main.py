import pandas as pd
from src.constants import DATASET
from src.logistic_regression import logistic_regression

df = pd.read_csv(DATASET)
logistic_regression(df)

