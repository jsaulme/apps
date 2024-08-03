import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

st.title('Análisis Exploratorio de Datos del Dataset Iris')

iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['target'] = iris.target

st.header('Datos del Dataset Iris')
st.write(df)

st.header('Estadísticas Descriptivas')
st.write(df.describe())

st.header('Gráficos')
option = st.selectbox('Selecciona el tipo de gráfico',
                      ['Histogramas', 'Pairplot'])

if option == 'Histogramas':
    st.subheader('Histogramas')
    fig, axes = plt.subplots(2, 2, figsize=(10, 8))
    sns.histplot(df.iloc[:, 0], ax=axes[0, 0], kde=True)
    sns.histplot(df.iloc[:, 1], ax=axes[0, 1], kde=True)
    sns.histplot(df.iloc[:, 2], ax=axes[1, 0], kde=True)
    sns.histplot(df.iloc[:, 3], ax=axes[1, 1], kde=True)
    st.pyplot(fig)

elif option == 'Pairplot':
    st.subheader('Pairplot')
    fig = sns.pairplot(df, hue='target')
    st.pyplot(fig)
