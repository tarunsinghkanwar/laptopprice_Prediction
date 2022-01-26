import streamlit as st
import pickle
import numpy as np
import pandas


import log
import Loaddata


logger=log.get_log("Application has started")
X_train,Y_train=Loaddata.data()

prep=pickle.load(open('Preprocessing.pkl','rb'))
model=pickle.load(open('model.pkl','rb'))



st.title("Laptop Price Predictor")

# brand
Company = st.selectbox('Brand',X_train['Company'].unique())

# type of laptop
TypeName = st.selectbox('Type',X_train['TypeName'].unique())

# Ram
Ram = st.selectbox('RAM(in GB)',[2,4,6,8,12,16,24,32,64])

# weight
Weight = st.number_input('Weight of the Laptop')

# Touchscreen
Touchscreen = st.selectbox('Touchscreen',['No','Yes'])

# IPS
Ips = st.selectbox('IPS',['No','Yes'])

# screen size
screen_size = st.number_input('Screen Size')

# resolution
resolution = st.selectbox('Screen Resolution',['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])

#cpu
Cpubrand = st.selectbox('CPU',X_train['Cpubrand'].unique())

HDD = st.selectbox('HDD(in GB)',[0,128,256,512,1024,2048])

SSD = st.selectbox('SSD(in GB)',[0,8,128,256,512,1024])

Gpubrand = st.selectbox('GPU',X_train['Gpubrand'].unique())

os = st.selectbox('OS',X_train['os'].unique())

if st.button('Predict Price'):
    # query
    ppi = None


    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi = np.round(((X_res**2) + (Y_res**2))**0.5/screen_size,4)

    query = np.array([Company,TypeName,Ram,Weight,Touchscreen,Ips,ppi,Cpubrand,HDD,SSD,Gpubrand,os])

    query = pandas.DataFrame(query.reshape(1,12),columns=X_train.columns)

    query['Weight'] = query['Weight'].astype('float32')
    query['ppi'] = query['ppi'].astype('float64')
    query['Ram'] = query['Ram'].astype('int32')
    query['SSD'] = query['SSD'].astype('int64')
    query['HDD'] = query['HDD'].astype('int64')

    st.title("The predicted price of this configuration is " + str(int(np.exp(model.XGBPredict(query)[0]))))
