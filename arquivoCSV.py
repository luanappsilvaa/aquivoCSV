import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados do arquivo CSV
@st.cache
def load_data():
    df = pd.read_csv('heart_failure_clinical_records_dataset.csv')
    return df

# Função para criar o gráfico
def create_plot(df):
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, x='sex', hue='DEATH_EVENT')
    plt.title('Death Event Count by Gender')
    plt.xlabel('Gender')
    plt.ylabel('Count')
    plt.legend(title='Death Event', loc='upper right')
    st.pyplot()

# Carregar os dados
df = load_data()

# Título do Streamlit
st.title('Heart Failure Clinical Records Dataset')

# Visualizar os dados
st.write(df)

# Criar e exibir o gráfico
create_plot(df)


