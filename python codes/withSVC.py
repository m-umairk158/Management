import numpy as np
import pandas
from sklearn.model_selection import train_test_split
import my_accuracy_function as accuracy
from sklearn.svm import SVC
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV

dataframe = pandas.read_csv("TrafficSpeed.csv",delimiter=',')
classes = {'Doctor': 0,'Student': 1, 'Eng.':2,'Teacher':3, 'Unknown':4}
speed = {'underLimit':1,'normal':2,'OverLimit':3}
dataframe.classes = [classes[item] for item in dataframe.classes] 
dataframe.speed = [speed[item] for item in dataframe.speed]
##Data 
data=dataframe.values
X=data[:,0:7]
Y=data[:,7]
total_samples=len(Y)

X_trn, X_tst, Y_trn, Y_tst = train_test_split(X, Y, test_size=0.3, random_state=0)
Cs = [0.001, 0.01, 0.1, 1, 10]
gammas = [0.001, 0.01, 0.1, 1]
param_grid = {'C': Cs, 'gamma' : gammas}
grid_search = GridSearchCV(SVC(kernel='rbf'), param_grid, cv=20)
grid_search.fit(X_trn, Y_trn)
predicted_output1=grid_search.predict(X_trn)
from_my_func1=accuracy.my_accuracy_function(predicted_output1,Y_trn)
predicted_output=grid_search.predict(X_tst)
from_my_func=accuracy.my_accuracy_function(predicted_output,Y_tst)
print("Accuracy from my Function on training data:")
print(from_my_func1)
print("Accuracy from my Function on testing data:")
print(from_my_func)