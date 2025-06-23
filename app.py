import streamlit as st
import numpy as np
import joblib

# Carregar o modelo
modelo = joblib.load('modelo_calorias.pkl')

st.title('Previsão de Calorias Queimadas')

st.write('Preencha os campos abaixo para prever as calorias queimadas por sessão de treino:')

# Campos de entrada
fat_percentage = st.number_input('Percentual de Gordura Corporal (%)', min_value=0.0, max_value=100.0, value=20.0)
weight = st.number_input('Peso (kg)', min_value=0.0, value=70.0)
session_duration = st.number_input('Duração da Sessão (horas)', min_value=0.0, value=1.0)
height = st.number_input('Altura (m)', min_value=0.0, value=1.70)
avg_bpm = st.number_input('Média de BPM durante o treino', min_value=0, value=120.0)
age = st.number_input('Idade', min_value=0, value=25)
water_intake = st.number_input('Consumo de Água (litros)', min_value=0, value=2.0)
resting_bpm = st.number_input('BPM em repouso', min_value=0, value=70.0)

# Botão para prever
if st.button('Prever Calorias Queimadas'):
    entrada = np.array([[fat_percentage, weight, session_duration, height,
                         avg_bpm, age, water_intake, resting_bpm]])
    predicao = modelo.predict(entrada)
    st.success(f'Calorias estimadas por sessão: {predicao[0]:.2f}')
