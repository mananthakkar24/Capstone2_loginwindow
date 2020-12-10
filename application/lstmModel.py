import pandas as pd
import numpy as np
import scipy
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
from scipy import integrate
import io
import requests
import seaborn as sns
from multiprocessing.pool import ThreadPool
from keras.preprocessing.sequence import TimeseriesGenerator
from keras.models import Sequential
from keras.layers import Dense 
from keras.layers import Dropout
from keras.layers import LSTM 
from sklearn.preprocessing import StandardScaler
from keras.models import model_from_yaml
import pickle

if __name__ == "__main__":
    scaler=StandardScaler()
    acd = pd.read_csv('https://api.covid19india.org/csv/latest/case_time_series.csv')
    acd["Active"]=acd["Total Confirmed"]-acd["Total Deceased"]-acd['Total Recovered']
    Indian = acd.groupby(["Date_YMD"])["Active"].sum().reset_index().sort_values("Date_YMD")
    acdf = Indian[['Date_YMD','Active']]
    datee = Indian[['Date_YMD']]
    acdf.reset_index()
    acdf = acdf.set_index('Date_YMD')
    # print(acdf)
    acdf['Active']=scaler.fit_transform(acdf['Active'].values.reshape(-1,1))
    len(acdf)
    ind=int(0.8*len(acdf))
    acdf_train=acdf.iloc[:ind,:]
    acdf_test=acdf.iloc[ind:,:]
    exp=acdf.iloc[0:]
    exp=pd.DataFrame(exp)

    obs_lag = 20
    n_feature= 1
    l=exp.values.tolist()
    #TimeseriesGenerator will convert the samples into supervised learning
    generator = TimeseriesGenerator(l,l, length=obs_lag, batch_size=1)
    model=Sequential()
    #input
    model.add(LSTM(200,activation='selu',input_shape=(obs_lag,n_feature)))
    #hidden
    model.add(Dropout(0.10))
    model.add(Dense(1))
    model.summary()
    model.compile(optimizer='adam',loss='mse',metrics=['acc'])
    model.fit_generator(generator,epochs=25,verbose=1)

    model_yaml = model.to_yaml()
    with open("model1.yaml", "w") as yaml_file:
        yaml_file.write(model_yaml)
    
    model.save_weights("model1.h5")
    