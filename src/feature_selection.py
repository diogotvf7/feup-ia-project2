

import pandas as pd
from sklearn.discriminant_analysis import StandardScaler
from sklearn.feature_selection import SelectFromModel
from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression

#function to print the colloumsn name receiving an ndarray
def get_selected_features_names(selected_features):
    indexes = [i for i, x in enumerate(selected_features) if x]
    return [str(i) + "-" + collumns_names[i] for i in indexes]

def len_selected_features(selected_features):
    return len([i for i, x in enumerate(selected_features) if x])

df = pd.read_csv("dataset/TCGA_InfoWithGrade.csv")

x = df.drop('Grade', axis=1)
y = df['Grade']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

collumns_names = x.columns

# 1. LASSO L1-based feature selection
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

# Create and fit the LASSO model
lasso = Lasso(alpha=0.02) #The higher the alpha parameter, the fewer features selected.
lasso.fit(x_train_scaled, y_train)

model = SelectFromModel(lasso, prefit=True)
print("1. Selected features using LASSO:", len_selected_features(model.get_support()))
print(get_selected_features_names(model.get_support()))
print()

# 2. Tree based feature selection
et = RandomForestClassifier(n_estimators=50)
et.fit(x_train, y_train)

model = SelectFromModel(et, prefit=True)
print("2. Selected features using Random Forest:", len_selected_features(model.get_support()))
print(get_selected_features_names(model.get_support()))
print()

# 3. Recursive feature elimination
rfe = RFE(estimator=LogisticRegression(max_iter=1000)) # we can increase n_features_to_select if we want
rfe.fit(x_train_scaled, y_train)
print("3. Selected features using RFE:", len_selected_features(rfe.support_))
print(get_selected_features_names(rfe.support_))

'''
The recommended way to feature selection in scikit-learn is to use a Pipeline:

clf = Pipeline([
  ('feature_selection', SelectFromModel(LinearSVC(dual="auto", penalty="l1"))),
  ('classification', RandomForestClassifier())
])
clf.fit(X, y)

'''