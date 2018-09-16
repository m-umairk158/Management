#### Task 2: Regression Problem
from sklearn.svm import SVR
import matplotlib.pyplot as plt
import numpy
#from sklearn import datasets, linear_model
import pandas
import my_mse_function as msf
import my_r2_function as r2
from sklearn.metrics import r2_score
plt.close('all')
dataframe = pandas.read_csv("data_website.csv",delimiter=';') 
X_u= dataframe.values
X=X_u[:,5:9] #input
Y=X_u[:,9] #output
###Plotting the data
A=X_u[:,0]
B1=X[:,0]
B2=X[:,1]
B3=X[:,2]
B4=X[:,3]
fig = plt.figure()
ax1 = fig.add_subplot(411)
ax2 = fig.add_subplot(412)
ax3 = fig.add_subplot(413)
ax4 = fig.add_subplot(414)

ax1.plot(A, B1, color='red')
ax2.plot(A, B2, color='blue')
ax3.plot(A, B3, color='yellow')
ax4.plot(A, B4, color='green')

# Set common labels

ax1.set_title('Temprature')
ax2.set_title('Humidity')
ax3.set_title('Precipitation')
ax4.set_title('Cloud Formation')
#######min-max values of parameters
temp_min=min(X[:,0])
temp_max=max(X[:,0])
hum_min=min(X[:,1])
hum_max=max(X[:,1])
perc_min=min(X[:,2])
perc_max=max(X[:,2])
cloud_min=min(X[:,3])
cloud_max=max(X[:,3])
solar_min=min(Y)
solar_max=max(Y)
##normalizing data using min-max normalization
Y_n=(Y-min(Y))/(max(Y)-min(Y))
temp_n=(X[:,0]-min(X[:,0]))/(max(X[:,0]-min(X[:,0])))
hum_n=(X[:,1]-min(X[:,1]))/(max(X[:,1]-min(X[:,1])))
prec_n=(X[:,2]-min(X[:,2]))/(max(X[:,2]-min(X[:,2])))
cloud_n=(X[:,3]-min(X[:,3]))/(max(X[:,3]-min(X[:,3])))
X_n=numpy.column_stack((temp_n,hum_n,prec_n,cloud_n))
####################################################
total_samples=50000
trn_samples=round(0.7*total_samples)
X_trn=X_n[0:trn_samples]
Y_trn=Y_n[0:trn_samples]
X_tst=X_n[trn_samples:total_samples]
Y_tst=Y_n[trn_samples:total_samples]
Y_umair=Y[trn_samples:total_samples]
svr_rbf=SVR(kernel='rbf',degree=10,C=0.001,gamma='auto')
svr_rbf.fit(X_trn,Y_trn)
predicted_output=svr_rbf.predict(X_trn)
plt.figure(2)
plt.plot(predicted_output,color='red',label='predicted values')
plt.plot(Y_trn, color='yellow',label='actual values')
plt.xlabel('sample')
plt.ylabel('Values')
plt.title('Support Vector Regression')
plt.legend()
plt.show()

predicted_output=svr_rbf.predict(X_tst)
plt.figure(3)
plt.plot(predicted_output,color='red',label='predicted values')
plt.plot(Y_tst, color='yellow',label='actual values')
plt.xlabel('sample')
plt.ylabel('Values')
plt.title('Support Vector Regression')

de_nor_so=predicted_output*(solar_max-solar_min)+solar_min
plt.figure(4)
plt.plot(de_nor_so,color='blue',label='predicted values')
plt.plot(Y_umair, color='red',label='actual values')
plt.xlabel('sample')
plt.ylabel('Values')
plt.title('Support Vector Regression')
plt.legend()
plt.show()
from_my_func=msf.my_mse_function(predicted_output,Y_tst)
from_my_func1=msf.my_mse_function(de_nor_so,Y_umair)
print("Mean Error from my Function:")
print(from_my_func)
print("Mean Error from my Function of denormalized:")
print(from_my_func1)
from_my_r2=r2.my_r2_function(de_nor_so,Y_umair)
from_my_r21=r2.my_r2_function(predicted_output,Y_tst)
from_builtin_r2_n=r2_score(Y_tst,predicted_output)
from_builtin_r2an=r2_score(Y_umair,de_nor_so)

print("R2 of denormalized and actual")
print(from_my_r2)
print("R2 of normalized and actual")
print(from_my_r21)
print("R2 of denormalized and actual builtin func")
print(from_builtin_r2an)
print("R2 of normalized and actual buithin func")
print(from_builtin_r2_n)