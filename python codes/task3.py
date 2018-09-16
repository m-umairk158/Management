#### Task 3: Solar Iradiance prediction with 100% training data
from sklearn.svm import SVR
import matplotlib.pyplot as plt
import numpy
#from sklearn import datasets, linear_model
import pandas
from sklearn.preprocessing import MinMaxScaler
import my_mse_function as msf
plt.close('all')
dataframe = pandas.read_csv("data_website.csv",delimiter=';')
X_u= dataframe.values
X=X_u[:,5:9]
Y=X_u[:,9]
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
total_samples=len(Y)
trn_samples=round(1*total_samples)
X_trn=X_n[0:trn_samples]
Y_trn=Y_n[0:trn_samples]
X_tst=X_n[trn_samples:total_samples]
Y_tst=Y_n[trn_samples:total_samples]
svr_rbf=SVR(kernel='rbf',degree=10,C=10,gamma='auto')
svr_rbf.fit(X_trn,Y_trn)
predicted_output=svr_rbf.predict(X_trn)
plt.figure(1)
plt.plot(predicted_output,color='red',label='predicted values')
plt.plot(Y_trn, color='yellow',label='actual values')
plt.xlabel('sample')
plt.ylabel('Values')
plt.title('Support Vector Regression')
plt.legend()
plt.show()
from_my_func=msf.my_mse_function(predicted_output,Y_trn)
print("Mean Error from my Function:")
print(from_my_func)
temp = float(input("What is the temprature today? "))
temp_u_n=(temp-temp_min)/(temp_max-temp_min)
humid=float(input("What is the Humidity today? "))
hum_u_n=(humid-hum_min)/(hum_max-hum_min)
prec=float(input("What is percipitation today? "))
prec_u_n=(prec-perc_min)/(perc_max-perc_min)
cloud=float(input("What is the cloud cover today? "))
cloud_u_n=(cloud-cloud_min)/(cloud_max-cloud_min)
X_user=numpy.array([temp_u_n,hum_u_n,prec_u_n,cloud_u_n])
solar_iradiance=svr_rbf.predict(X_user.reshape(1,-1))
###denormalization of solar iradiance
de_nor_so=solar_iradiance*(solar_max-solar_min)+solar_min
print("The predicted solar iradiance today is: ",float(de_nor_so))