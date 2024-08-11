from sklearn.ensemble import RandomForestRegressor
import pandas as pd    
import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model


import pickle
with open('weather.pkl','rb')as f:
    df=pickle.load(f) 
    
with open('Rf.pkl','rb') as f:
    model=pickle.load(f)

tempreature = st.number_input('Enter a tempreature:', format="%.2f", step=0.01)
Dew_Point_Temp_C=st.number_input('Enter a Dew_Point_Temp_C:', format="%.2f", step=0.01)
Rel_Hum=st.number_input('Enter a Rel_Humidity:', format="%.2f",step=0.01)
Wind_Speed_km_h= st.number_input('Enter Wind Speed_km/h :', format="%.2f", step=0.01)
Press_kPa=st.number_input('Enter Press_kPa', format="%.2f", step=5)


if(st.button('predict')):
    data={
        'Temp_C': tempreature,
        'Dew Point Temp_C': Dew_Point_Temp_C,
        'Rel Hum_%': Rel_Hum,
        'Wind Speed_km/h': Wind_Speed_km_h,
        'Visibility_km': 0,
        'Press_kPa': Press_kPa
    }
    input_df = pd.DataFrame(data, index=[0])
    input_df = input_df.fillna(0)
    st.dataframe(input_df)
    st.write(model.predict(input_df))








