import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset procesado
@st.cache
def load_data():
    return pd.read_csv('https://raw.githubusercontent.com/jsaulme/datasets/main/Global_superstore2018__encoded.csv')

data = load_data()

# Título de la aplicación
st.title('Análisis de Global SuperStore')

# Mostrar datos
st.subheader('Datos del Global SuperStore')
st.write(data.head())

# Análisis de pérdidas por categoría
st.subheader('Análisis de Pérdidas por Categoría')
losses = data[data['Profit'] < 0]
losses_by_category = losses.groupby('Category')['Profit'].sum()
st.bar_chart(losses_by_category)

# Filtrar datos por categoría
category = st.selectbox('Selecciona una categoría', data['Category'].unique())
filtered_data = data[data['Category'] == category]
st.write(f'Datos filtrados por la categoría {category}')
st.write(filtered_data)

# Gráfico de ventas vs ganancia
st.subheader('Análisis Gráfico de Ventas vs Ganancia')
fig, ax = plt.subplots()
ax.scatter(data['Sales'], data['Profit'])
ax.set_xlabel('Ventas')
ax.set_ylabel('Ganancia')
st.pyplot(fig)

# Otras visualizaciones y análisis
# Añadir aquí cualquier otro análisis que hayas realizado

