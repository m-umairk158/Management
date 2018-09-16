#### TASK 1: Classification Problem

from sklearn.svm import SVC
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score
from sklearn import datasets
import my_accuracy_function as accuracy

import time
import numpy as np
import matplotlib.pyplot as plt

dataset=datasets.load_iris()

X=dataset.data
Y=dataset.target
total_samples=len(Y)
trn_samples=round(0.7*total_samples)
get_from=30 ##give position from where to get 70%, 0 means 70% from start
X_trn=X[get_from:trn_samples+get_from]
Y_trn=Y[get_from:trn_samples+get_from]
A=X[0:get_from]
B=X[trn_samples+get_from:total_samples]
X_tst=np.concatenate((A,B), axis=0)
C=Y[0:get_from]
D=Y[trn_samples+get_from:total_samples]
Y_tst=np.concatenate((C,D), axis=0)
accuracy_all = []
cvs_all = []
start = time.time()

clf = SVC()
clf.fit(X_trn, Y_trn)
prediction = clf.predict(X_tst)
scores = cross_val_score(clf, X, Y, cv=5)

end = time.time()

accuracy_all.append(accuracy_score(prediction, Y_tst))
cvs_all.append(np.mean(scores))
from_my_function=accuracy.my_accuracy_function(prediction, Y_tst)
print("SVC Accuracy: {0:.2%}".format(accuracy_score(prediction, Y_tst)))
print("from my function SVC Accuracy: {0:.2%}")
print(from_my_function)
print("Cross validation score: {0:.2%} (+/- {1:.2%})".format(np.mean(scores), np.std(scores)*2))
print("Execution time: {0:.5} seconds \n".format(end-start))
plt.plot(prediction,color='red',label='predicted values')
plt.plot(Y_tst, color='yellow',label='actual values')
plt.xlabel('sample')
plt.ylabel('Values')
plt.title('SVC')
plt.legend()
plt.show()