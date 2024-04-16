 
import pandas as pd
import plotly.express as px
import streamlit as st
car_data = pd.read_csv('vehicles_us.csv') # leer los datos

##Data viewer
car_data['manufacturer'] = car_data['model'].str.split(" ").str[0] #Creando la columna manufacturer
st.header('Data viewer')
build_cb = st.checkbox('Include manufacturers with less than 1000 ads')
car_count = car_data['manufacturer'].value_counts()
car_prob = car_count[car_count < 1000].index

if build_cb: #si la casilla de verificación está seleccionada
    car_data[car_data['manufacturer'].isin(car_prob)]
else:
    st.write(car_data)  

##Gráfico de barras

st.header('Vehicles types by manufacturer')

fig = px.bar(car_data, x="manufacturer", color="type")
st.plotly_chart(fig, use_container_width=True)

##Histograma
st.header('Histogram of condition vs model_year')

hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para la condición vs el año modelo de los vehículos')

    fig = px.histogram(car_data, x="model_year", color="condition")
    st.plotly_chart(fig, use_container_width=True)

##Dispersión
st.header('Scatter of odometer vs price')

build_scatter = st.checkbox('Construir un diagrama de dispersión')

if build_scatter: #si la casilla de verificación está seleccionada
    st.write('Construir un diagrama de dispersión para odometro vs precio')
    fig = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión
    #fig.show() # crear gráfico de dispersión
    st.plotly_chart(fig, use_container_width=True)