# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 10:17:34 2018

@author: hp
"""

import sklearn.datasets
from sklearn.naive_bayes import GaussianNB
import my_accuracy_function as accuracy
import matplotlib.pyplot as plt
data=sklearn.datasets.load_iris()
X=data.data
Y=data.target
total_samples=len(Y)
trn_samples=int(round(0.7*total_samples))
X_trn=X[0:trn_samples]
Y_trn=Y[0:trn_samples]
X_tst=X[trn_samples:total_samples]
Y_tst=Y[trn_samples:total_samples]
####Classification
clf=GaussianNB()
clf.fit(X_trn,Y_trn)
out=clf.predict(X_tst)
###Evaluate
from_my_function=accuracy.my_accuracy_function(out, Y_tst)
plt.plot(out,color='red',label='predicted values')
plt.plot(Y_tst, color='yellow',label='actual values')
plt.xlabel('sample')
plt.ylabel('Values')
plt.title('Naive Bayes')
plt.legend()
plt.show()
