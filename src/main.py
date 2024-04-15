import pandas as pd
import matplotlib.pyplot as plt


DATASET = '../dataset/TCGA_InfoWithGrade.csv'

GRADE = ['LGG','GBM']
PROJECT = ['TCGA-GBM', 'TCGA-GBM']
GENDER = ['Male', 'Female']
RACE = ['White', 'Black or African American', 'Asian', 'American Indian or Alaska Native']
GENE = ['Not Mutated', 'Mutated']


def gradePlot(df):
    gradeCounts = df['Grade'].value_counts()
    plot = gradeCounts.plot.pie(y='Grade', x=GRADE, figsize=(5, 5)) 
    plot.get_figure().savefig('../plots/grade_distribution.png')




df = pd.read_csv(DATASET)
print(df.head())
gradePlot(df)
    