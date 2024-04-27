(max. 5 slides)
- (1) a specification of the work to be performed (definition of the machine learning problem to address)
- (2) related work with references to works found in a bibliographic search (articles, web pages and/or source code)
- (3) a description of the tools and algorithms to use in the assignment
- (4) implementation work already carried out.

Slide 1: Specification of the Machine Learning Problem
- The goal of this work is to develop some models for glioma grading using clinical and molecular characteristics.
- Glioma grading is a critical step for treatment optimization and improving patient survival rates.
We aim to classify glioma patients as LGG (Lower-Grade Glioma) or GBM (Glioblastoma Multiforme) based on clinical and molecular features, where LGG is considered negative and GBM is considered positive.

Slide 2: Related Work
- Hierarchical Voting-Based Feature Selection and Ensemble Learning Model Scheme for Glioma Grading with Clinical and Molecular Characteristics (2022)
- (o destino verá mais ...)

Slide 3: Tools and Algorithms
- Programming Language: Python
- Libraries: scikit-learn, xverse (risk this)
We decided to use different machine learning algorithms to classify glioma patients as LGG or GBM. The algorithms we chose are:
- Logistic Regression (LR)
- Support Vector Machine (SVM)
- K Nearest Neighbors (KNN)
- Random Forest (RF)
- AdaBoost
- Neural Networks (NN) (?)

We will use the Scikit-Learn Python library to implement these algorithms. We will also use the Pandas library to manipulate the dataset and the Matplotlib and Seaborn libraries to plot the results.

We will also use the xverse library to perform feature selection. We will use the following methods:
  - Weight of Evidence (WOE)
  - Recursive Feature Elimination (RFE)
  - Random Forest (RF)
  - Least Absolute Shrinkage and Selection Operator (LASSO)
  
We will also use ensemble learning to combine the predictions of multiple models. We will use the soft-voting approach to combine the predictions of the models. We will construct 16 ensemble model combinations using 3, 4, and 5 models.

Slide 4: Implementation Work

TODO: (Talvez a matriz de correlação e dois algoritmos)

- Developed a hierarchical voting-based methodology for feature selection and ensemble learning
- Employed four feature selection methods (WOE, RFE, RF, LASSO) and five supervised learning models (LR, SVM, KNN, RF, AdaBoost)
- Constructed 16 ensemble model combinations using soft-voting approach
- Evaluated performance on TCGA and CGGA glioma datasets
