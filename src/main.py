
import seaborn as sns
import pandas as pd
from distributions import gradePlot, genderPlot, agePlot

DATASET = '../dataset/TCGA_InfoWithGrade.csv'
df = pd.read_csv(DATASET)

# gradePlot(df)
# genderPlot(df)
# agePlot(df)
print(df)
