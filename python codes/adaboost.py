import numpy as np
import pandas
from sklearn.model_selection import train_test_split
import my_accuracy_function as accuracy
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score
from sklearn.ensemble import AdaBoostClassifier

names = ['car id','timestamp','local x', 'local y', 'global x', 'global y', 'speed', 'classes']
dataframe = pandas.read_csv("TrafficSpeed.csv",delimiter=',',usecols=names)
classes = {'Doctor': 0,'Student': 1, 'Eng.':2,'Teacher':3, 'Unknown':4}
speed = {'underLimit':0,'normal':1,'OverLimit':2}
dataframe.classes = [classes[item] for item in dataframe.classes] 
dataframe.speed = [speed[item] for item in dataframe.speed]
data=dataframe.values
X=data[:,0:7]
Y=data[:,7]
total_samples=len(Y)
X_trn, X_tst, Y_trn, Y_tst = train_test_split(X, Y, test_size=0.1, random_state=4)
parameters={'max_depth': np.arange(10, 30), 'min_samples_split':np.arange(50, 100)}
clf = AdaBoostClassifier(DecisionTreeClassifier(max_depth=2),
    n_estimators=1000,learning_rate=1)
clf.fit(X_trn, Y_trn) 
predicted_output1=clf.predict(X_trn)
from_my_func1=accuracy.my_accuracy_function(predicted_output1,Y_trn)
predicted_output=clf.predict(X_tst)
from_my_func=accuracy.my_accuracy_function(predicted_output,Y_tst)
print("Accuracy from my Function on training data:")
print(from_my_func1)
print("Accuracy from my Function on testing data:")
print(from_my_func)
C_mat=confusion_matrix(predicted_output,Y_tst)
f=f1_score(predicted_output,Y_tst,average='average')
