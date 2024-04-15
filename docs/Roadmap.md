# About
Machine learning models and algorithms related to supervised learning.

# Deadlines

- Checkpoint: 29 April
- Delivery: 21 May
- Final presentations and demonstrations: 27-28 May


Initial exploratory data analysis: (class distribution, values per attribute,and so on). 
Different learning algorithms should be employed and compared using appropriate evaluation metrics (performance during learning, confusion matrix, precision, recall, accuracy, F1 measure) and the time spent to train/test the models.
Supervised learning includes the following steps: 
- dataset analysis to check for the need for data pre-processing
- identification of the target concept
- definition of the training and test sets
- selection and parameterization of the learning algorithms to employ, 
- evaluation of the learning process (in particularon the test set). 

At least 3 supervised learning (classification) algorithms should be employed (Decision Trees, Neural Networks, K-NN, SVM, …), but more may be employed and compared using the Scikit-Learn Python library and considering the characteristics of the dataset. 
Results should be compared using tables or plots (e.g., using Seaborn or Matplotlib libraries).

## Checkpoint
Presentation (max. 5 slides), in PDF format. 
The presentation should contain 
- (1) a specification of the work to be performed (definition of the machine learning problem to address)
- (2) related work with references to works found in a bibliographic search (articles, web pages and/or source code)
- (3) a description of the tools and algorithms to use in the assignment
- (4) implementation work already carried out.

## Final Delivery
A presentation (max. 10 slides), in PDF format:
In addition to the aforementioned for the checkpoint,
- details on data pre-processing
- the developed models and their evaluation and comparison, using appropriate graphical elements (tables, plots, etc.).

Implemented code, properly commented, including a “readme” file with instructions on how to compile, run
and use the program. The code and comments may be submitted as a complete Jupyter Notebook.

# Dataset

[link](https://www.kaggle.com/datasets/vinayjose/glioma-grading-clinical-and-mutation-features)

Gliomas are the most common primary tumors of the brain. They can be graded as LGG (Lower-Grade Glioma) or GBM (Glioblastoma Multiforme) depending on the histological/imaging criteria. Clinical and molecular/mutation factors are also very crucial for the grading process. Molecular tests are expensive to help accurately diagnose glioma patients.

In this dataset, the most frequently mutated 20 genes and 3 clinical features are considered from TCGA-LGG and TCGA-GBM brain glioma projects.

The prediction task is to determine whether a patient is LGG or GBM with a given clinical and molecular/mutation features. The main objective is to find the optimal subset of mutation genes and clinical features for the glioma grading process to improve performance and reduce costs.


[link](https://www.kaggle.com/datasets/vinayjose/glioma-grading-clinical-and-mutation-features)