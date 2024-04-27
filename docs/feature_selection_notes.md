Feature selection/dimensionality reduction on sample sets is used to either to improve estimators’ accuracy scores or to boost their performance on very high-dimensional datasets.

Because our set is not very high-dimensional, we will only focus on feature selection to improve the accuracy.

1. 
VarianceThreshold is a simple statistical method used to remove low-variance features. It is a simple baseline approach to feature selection. It removes all features whose variance doesn’t meet some threshold. By default, it removes all zero-variance features, i.e., features that have the same value in all samples. In this case, we will use a threshold of 0.8, which means that features with a variance of less than 0.8 will be removed.

```python
sel = VarianceThreshold(threshold=(.8 * (1 - .8)))
sel.fit_transform(X)

# Get selected features indices
selected_features = [i for i, var in enumerate(sel.variances_) if var >= 0.8]
```

2.
LASSO L1-based feature selection
LASSO (Least Absolute Shrinkage and Selection Operator) is a linear model that estimates sparse coefficients. It is useful in some contexts due to its tendency to prefer solutions with fewer non-zero coefficients, effectively reducing the number of features upon which the given solution is dependent. With increasing alpha, more features are set to zero and therefore fewer features are selected.

```python
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Create and fit the LASSO model
lasso = Lasso(alpha=0.1) #The higher the alpha parameter, the fewer features selected.
lasso.fit(X_train_scaled, y_train)

# Get selected features (non-zero coefficients)
selected_features = [i for i, coef in enumerate(lasso.coef_) if coef != 0]
print("Selected features indices:", selected_features)
```

3.
Tree based feature selection
Tree-based estimators can be used to compute feature importances, which in turn can be used to discard irrelevant features. The following example shows how to use ExtraTreesClassifier to compute feature importances and select the most important features.

```python
clf = ExtraTreesClassifier(n_estimators=50)
clf = clf.fit(X, y)
clf.feature_importances_  
//array([ 0.04...,  0.05...,  0.4...,  0.4...])
model = SelectFromModel(clf, prefit=True)
X_new = model.transform(X)
X_new.shape  
```