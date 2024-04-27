Gliomas can be currently broadly categorized into two groups, low-grade gliomas (LGG) and high-grade gliomas (HGG).

According to the guidelines of the World Health Organization
(WHO) classiﬁcation of Central Nervous System (CNS) tumors, gliomas can be currently
broadly categorized into two groups, low-grade gliomas (LGG) and high-grade gliomas
(HGG), with glioblastoma multiforme (GBM), a high-grade glioma, based on histological
and molecular parameters [ 6]. GBM is the most common, aggressive, invasive, and primary
type of tumor. Glioma accounts for almost 80% of all primary malignant tumors of the
brain, and GBM also accounts for more than 60% of all brain tumors in adults, emphasizing
the importance of grading in this neuro-oncology scenario


vast and heterogenous number of available molecular parameters emphasizing the importance of the identiﬁcation and selection of the necessary
molecular alterations, and the goal of reducing the cost of molecular testing to allow for its
more widespread use and mitigation of health disparities.

Clinical features such as age and gender [12 ] contribute
to the tumor grading process, but there is a paucity of higher-level robust clinical annotation
in publicly available datasets limiting links between pertinent molecular features and
clinical data, which could advance value-added care as more widespread molecular testing
may eventually beneﬁt from the increase in reimbursement.


What was done/studied in the past?
Today, feature selection is widely used in many data analysis applications,
pattern recognition, and mining tasks [16, 17]. As example studies of brain tumor grad-
ing, Ref. [18 ] performed subtyping and grading of lower-grade gliomas using integrated
SVM recursive feature elimination and a correlation method using transcriptome data.
In another study [19 ], molecular three-subtype classiﬁcation of low-grade gliomas using
magnetic-resonance-imaging-based radiomic features and employing genetic-algorithm-
based feature selection with an eXtreme Gradient Boosting classiﬁer was provided. In [ 20],
a joint similarity network fusion (Joint-SNF) method was proposed to integrate different
omic data types for subtype identiﬁcation of Chinese lower-grade glioma. In [21], a deep-
learning-based framework was developed for the precise and accurate classiﬁcation of
GBM subtypes by employing transcriptome and methylome data types. Although there
is no single algorithm that could outperform every other machine learning model for all
problems [22 , 23 ] (i.e., no free lunch theorem), many studies in the literature have shown
that an ensemble of models generally outperforms individual models [22,24 ,25 ]. In recent
years, ensemble learning methods have been considered state-of-the-art approaches for
solving machine learning challenges [ 23 –27 ]. In [28 ], the performances of advanced ensem-
ble learning methods have been found to be more robust than the well-known Random
Forest and AdaBoost ensemble classiﬁers. Currently, bagging and boosting models are
one of the most popular ensemble learning methods, with Random Forest and AdaBoost
being the most prominent and common implementations, respectively [ 29 ]. These meth-
ods cover a large scale of applications including face recognition, anomaly detection, and
medicine [29]. 


The performance (e.g., the accuracy rate) of a machine learning model can be
improved by training multiple learning models and combining their predictions (namely,
classiﬁer ensembles) [ 23,26 ,27 ,30,31 ]. This operation can be performed by employing var-
ious schemes such as bagging, boosting, or voting.


possible combinations of
supervised models in the soft-voting-based process employing two glioma datasets, TCGA
and CGGA, that are currently in widespread use


Really good info:
 The predictive models utilized are LR, SVM,
KNN, RF, and AdaBoost. The combinations of 3, 4, and 5 of these models are used for the
soft-voting-based ensemble learning scheme. The total number of ensemble learning model
combinations is 16 (i.e., C(5,3) + C(5,4) + C(5,5) = 16

A 10-fold cross-validation
technique was also applied on the TCGA and CGGA datasets to construct and test the mean
performance results of the learning models employed.

n this study, the GBM class was
considered positive and the LGG class was used as negative for the evaluation of learning
models.

The default values were assigned as the corresponding parameter values for the
utilized classiﬁers (i.e., num of neighbors = 5, metric = ‘minkowski’ for KNN; C = 1 , and
kernel = ‘rbf’, gamma = ’scale’ for SVM; penalty = ‘l2’, *, dual = False, tol = 0.0001, C = 1.0 ,
ﬁt_intercept = True, intercept_scaling = 1, class_weight = None for LR; n_estimators = 100,
*, criterion = ‘gini’, max_depth = None, min_samples_split = 2, min_samples_leaf = 1 for
RF; n_estimators = 50, learning_rate = 1.0, algorithm = ‘SAMME.R’ for AdaBoost). 

We set
the random state number to 0 for all employed learning models in order to obtain the same
computational results with the same random state number on the datasets used

The dataset consistent in both TCGA (The Cancer
Genome Atlas) and CGGA (Chinese Glioma Genome Atlas)
TCGA dataset consists of 3 clinical features