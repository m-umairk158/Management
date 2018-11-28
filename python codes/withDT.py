import numpy as np
import pandas
from sklearn.model_selection import train_test_split
import my_accuracy_function as accuracy
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV
from sklearn.feature_selection import SelectFromModel
from sklearn.ensemble import ExtraTreesClassifier

dataframe = pandas.read_csv("TrafficSpeed.csv",delimiter=',')
classes = {'Doctor': 0,'Student': 1, 'Eng.':2,'Teacher':3, 'Unknown':4}
speed = {'underLimit':0,'normal':1,'OverLimit':2}
dataframe.classes = [classes[item] for item in dataframe.classes] 
dataframe.speed = [speed[item] for item in dataframe.speed]
##Data 
data=dataframe.values
X=data[:,0:7]
Y=data[:,7]
clf = ExtraTreesClassifier(criterion='entropy',n_estimators=100)
clf = clf.fit(X, Y)
model = SelectFromModel(clf, prefit=True)
X_new = model.transform(X)

total_samples=len(Y)
X_trn, X_tst, Y_trn, Y_tst = train_test_split(X_new, Y, test_size=0.3, random_state=0)
parameters={'max_depth': np.arange(15, 30), 'min_samples_split':np.arange(15, 32)}
clf = DecisionTreeClassifier(criterion='entropy', splitter='best', max_depth=10, min_samples_split=2, min_samples_leaf=1, min_weight_fraction_leaf=0.0, max_features=None, random_state=None, max_leaf_nodes=None, min_impurity_decrease=0.0, min_impurity_split=None, class_weight=None, presort=False)
grid_search = GridSearchCV(clf, parameters, cv=20, n_jobs=1, refit=True,verbose=1)
grid_search.fit(X_trn, Y_trn) 
predicted_output1=grid_search.predict(X_trn)
from_my_func1=accuracy.my_accuracy_function(predicted_output1,Y_trn)
predicted_output=grid_search.predict(X_tst)
from_my_func=accuracy.my_accuracy_function(predicted_output,Y_tst)
print("Accuracy from my Function on training data:")
print(from_my_func1)
print("Accuracy from my Function on testing data:")
print(from_my_func)