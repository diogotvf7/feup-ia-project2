import seaborn as sns
import matplotlib.pyplot as plt
from constants import GRADE, GENDER


def gradePlot(df):
    gradeCounts = df['Grade'].value_counts()
    plt.figure()
    plot = gradeCounts.plot(
        kind="pie", 
        x=GRADE, 
        labels=GRADE, 
        legend=True, 
        y='Grade', 
        figsize=(5, 5)
    ) 
    plt.savefig('../plots/grade_distribution.png')

def genderPlot(df, show):
    genderCounts = df['Gender'].value_counts()
    plt.figure()
    plt.pie(genderCounts)
    plt.legend(True)
    plt.show()
    genderCounts.plot(
        kind="pie", 
        x=GENDER, 
        labels=GENDER, 
        legend=True, 
        y='Gender', 
        figsize=(5, 5)
    )
    plt.savefig('../plots/gender_distribution.png')

def agePlot(df):
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.hist(df['Age_at_diagnosis'], bins=20, color='skyblue', edgecolor='black')
    plt.xlabel('Age at Diagnosis')
    plt.ylabel('Frequency')
    plt.title('Age at Diagnosis Distribution')

    # Box plot
    plt.subplot(1, 2, 2)
    plt.boxplot(df['Age_at_diagnosis'], vert=False)
    plt.xlabel('Age at Diagnosis')
    plt.title('Age at Diagnosis Distribution')

    plt.tight_layout()
    plt.show()