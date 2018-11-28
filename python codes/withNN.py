import numpy as np
import pandas
from sklearn.model_selection import train_test_split
import my_accuracy_function as accuracy
from sklearn.neural_network import MLPClassifier
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.metrics import confusion_matrix

names = ['car id','timestamp','local x', 'local y', 'global x', 'global y', 'speed', 'classes']
dataframe = pandas.read_csv("TrafficSpeed.csv",delimiter=',',usecols=names)
classes = {'Doctor': 1,'Student': 2, 'Eng.':3,'Teacher':4, 'Unknown':5}
speed = {'underLimit':1,'normal':2,'OverLimit':3}
dataframe.classes = [classes[item] for item in dataframe.classes] 
dataframe.speed = [speed[item] for item in dataframe.speed]
data=dataframe.values
X=data[:,0:7]
Y=data[:,7]
##Data 
data=dataframe.values
X=data[:,0:6]
Y=data[:,6]
total_samples=len(Y)
X_trn, X_tst, Y_trn, Y_tst = train_test_split(X, Y, test_size=0.3, random_state=0)
clf= MLPClassifier(solver='adam', alpha=1e-3,hidden_layer_sizes=(1,10), random_state=2, max_iter=2000, verbose=True,tol=1e-7,learning_rate_init=.0001)
clf.fit(X_trn, Y_trn) 
predicted_output1=clf.predict(X_trn)
from_my_func1=accuracy.my_accuracy_function(predicted_output1,Y_trn)
predicted_output=clf.predict(X_tst)
from_my_func=accuracy.my_accuracy_function(predicted_output,Y_tst)
print("Accuracy from my Function on training data:")
print(from_my_func1)
print("Accuracy from my Function on testing data:")
print(from_my_func)
C_mat=confusion_matrix(Y_tst, predicted_output)
