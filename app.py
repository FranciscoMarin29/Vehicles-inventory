import pandas as pd
import plotly.express as px 
import streamlit as st 

car_data = pd.read_csv('vehicles_us.csv')

# Encabezado de la aplicación
st.header('Análisis de Datos de Vehículos.')

# Botones para generar gráficos
hist_button = st.button('Construir un histograma')
scatter_plot_button = st.button('Construir gráfico de dispersión')

# Crear un histograma cuando se presione el botón
if hist_button:
    
    st.write('Creación de un histograma para el conjunto de datos.')
    
    fig_hist = px.histogram(car_data, x= 'odometer', nbins= 20)
    
    st.plotly_chart(fig_hist, use_container_width= True)
    

if scatter_plot_button:
    # Seleccionar columnas para el gráfico de dispersión
    
    st.write('Creación de un gráfico de dispersión para el conjunto de datos.')

    fig = px.scatter(car_data, x="odometer", y="price")

    # Mostrar el gráfico
    st.plotly_chart(fig, use_container_width=True)
