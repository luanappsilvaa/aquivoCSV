import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar o arquivo CSV
@st.cache  # Cache para melhorar o desempenho
def load_data():
    df = pd.read_csv('facebook_reviews.csv')
    return df

df = load_data()

# Configurar o título do aplicativo
st.title('Análise de Avaliações do Facebook')

# Exibir os primeiros registros do DataFrame (opcional)
st.write("Aqui estão os primeiros registros do DataFrame:")
st.write(df.head())

# Exibir o gráfico
st.write("Gráfico de Avaliações do Facebook:")
sns.histplot(data=df, x='Avaliação', bins=5, kde=True)
st.pyplot()


