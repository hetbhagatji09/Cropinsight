
import pandas as pd    
import streamlit as st
min_year = 2018
max_year = 2024

import pickle
with open('dataframe.pkl','rb') as f:
    New_data=pickle.load(f)
    
with open('pipeline.pkl','rb') as f:
    pipeline=pickle.load(f)
#st.dataframe(New_data.iloc[0])
District_list=New_data['District Name'].unique()
st.title('CropInsight')

#movies_list=['title'].values
selected_district = st.selectbox(
     "Select District",
     (District_list))
# st.button("Recommened", type="primary")
Market_list =New_data[New_data['District Name']==selected_district]['Market Name'].unique()
Market_Name=st.selectbox("Choose Market", (Market_list));

Commodity_list=New_data[New_data['Market Name']==Market_Name]['Commodity'].unique()
Commodity_Name=st.selectbox("Choose Commodity", (Commodity_list));

Minimum_value = st.slider('Select the Minimum Value:', min_value=0, max_value=5000, value=0)
Max_Value = st.slider('Select the Maximum Value:', min_value=0, max_value=5000, value=0)


day = st.number_input('Enter day:', min_value=1, max_value= 31, value=1, step=1)
month = st.number_input('Enter Month:', min_value=1, max_value= 12, value=1, step=1)
year = st.number_input('Enter a year:', min_value=min_year, max_value=max_year, value=min_year, step=1)



if(st.button('predict')):
    data = {
    "District Name": [selected_district],
    "Market Name": [Market_Name],
    "Commodity": [Commodity_Name],
    "Min Price(Rs.)": [Minimum_value],
    "Max Price(Rs.)": [Max_Value],
    "Year": [year],
    "Month": [month],
    "Day": [day]
    }
    df = pd.DataFrame(data)
    st.dataframe(df)
    st.write(pipeline)
    #st.write(pipeline.predict(df))

