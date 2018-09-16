# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 10:51:46 2018

@author: hp
"""

import pandas
from sklearn.linear_model import BayesianRidge as BR
from sklearn.svm import SVR
import matplotlib.pyplot as plt
import my_mse_function as msf
import my_r2_function as r2
from sklearn.metrics import r2_score
plt.close('all')
dataframe = pandas.read_csv("chille 2 weeks.csv",delimiter=';') 
X_u= dataframe.values
X=X_u[:,[5,6,8]] #input
Y=X_u[:,15] #output

total_samples=len(Y)
trn_samples=int(round(0.2*total_samples))
X_trn=X[0:trn_samples]
Y_trn=Y[0:trn_samples]
X_tst=X[trn_samples:int(0.3*total_samples)]
Y_tst=Y[trn_samples:int(0.3*total_samples)]
svr_rbf=SVR(kernel='rbf',degree=10,C=10,gamma='auto')
svr_rbf.fit(X_trn,Y_trn)
out=svr_rbf.predict(X_trn)

clf=BR()
clf.fit(X_trn,Y_trn)
out1=clf.predict(X_trn)
from_my_func=msf.my_mse_function(out,Y_trn)
from_my_func1=msf.my_mse_function(out1,Y_trn)
r2my=r2.my_r2_function(out,Y_trn)
r2myy=r2.my_r2_function(out1,Y_trn)
r2mybi=r2_score(out,Y_trn)
r2myybi=r2_score(out1,Y_trn)
plt.figure(1)
plt.plot(out1,color='blue',label='predicted values')
plt.plot(Y_trn, color='red',label='actual values')
plt.xlabel('sample')
plt.ylabel('Values')
plt.title('NB regression')
plt.legend()
plt.show()
plt.figure(2)
plt.plot(out,color='blue',label='predicted values')
plt.plot(Y_trn, color='red',label='actual values')
plt.xlabel('sample')
plt.ylabel('Values')
plt.title('SVR')
plt.legend()
plt.show()
print("mse from SVR regression")
print(from_my_func)
print("mse from NB regression")
print(from_my_func1)
### use split command
print("from SVR regression r2")
print(r2my)
print("from NB regression r2")
print(r2myy)
print("from SVR regression r2 built in")
print(r2mybi)
print("from NB regression r2 built in")
print(r2myybi)