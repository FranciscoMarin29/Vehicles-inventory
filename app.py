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

    x_axis = st.selectbox('Selecciona la columna para el eje X:', ['price', 'odometer', 'model_year', 'cylinders'])
    y_axis = st.selectbox('Selecciona la columna para el eje Y:', ['price', 'odometer', 'model_year', 'cylinders'])
    
    # Seleccionar columna para color
    color_axis = st.selectbox('Selecciona la columna para color (categoría):', ['condition', 'fuel', 'transmission', 'type', 'paint_color'])

    # Crear el gráfico de dispersión
    fig_scatter = px.scatter(
        car_data,
        x=x_axis,
        y=y_axis,
        color=color_axis,
        marginal_y="violin",
        marginal_x="box",
        trendline="ols",
        template="simple_white",
        title=f'Gráfico de dispersión: {x_axis} vs {y_axis}'
    )
    # Mostrar el gráfico
    st.plotly_chart(fig_scatter, use_container_width= True)
