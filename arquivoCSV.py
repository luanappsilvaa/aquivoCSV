import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o arquivo CSV
df = pd.read_csv('facebook_reviews.csv')

# Configurar o título do aplicativo
st.title('Análise de Avaliações do Facebook')

# Exibir os primeiros registros do DataFrame (opcional)
st.write("Aqui estão os primeiros registros do DataFrame:")
st.write(df.head())

# Exibir o gráfico
st.write("Gráfico de Avaliações do Facebook:")
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Avaliação', bins=5, kde=True)
plt.xlabel('Avaliação')
plt.ylabel('Contagem')
st.pyplot()

