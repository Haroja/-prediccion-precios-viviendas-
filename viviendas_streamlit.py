#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

# Cargar los datos
df = pd.read_csv('homeprices.csv')

# Preprocesamiento de datos
df['bedrooms'] = df['bedrooms'].fillna(df['bedrooms'].median())

# Entrenar el modelo
model = LinearRegression()
model.fit(df[['area', 'bedrooms', 'age']], df['price'])

# Función para predecir el precio
def predict_price(area, bedrooms, age):
    prediction = model.predict([[area, bedrooms, age]])
    return prediction[0]

# Interfaz de Streamlit
st.title('Predicción del Precio de Viviendas')

st.markdown("""
Esta aplicación predice el precio de una vivienda basándose en su área, número de habitaciones y antigüedad.
""")

# Entradas del usuario
area = st.number_input('Área (pies cuadrados)', value=2000.0)
bedrooms = st.number_input('Número de habitaciones', value=3.0)
age = st.number_input('Antigüedad (años)', value=20.0)

# Validación de la entrada
input_valid = True  # Variable para rastrear si la entrada es válida

if area < 100:
    st.error("El área debe ser al menos 100 pies cuadrados.")
    input_valid = False
elif area > 5000:
    st.error("El área no puede exceder los 5000 pies cuadrados.")
    input_valid = False
elif bedrooms < 1:
    st.error("El número de habitaciones debe ser al menos 1.")
    input_valid = False
elif bedrooms > 10:
    st.error("El número de habitaciones no puede exceder 10.")
    input_valid = False
elif age < 0:
    st.error("La antigüedad no puede ser negativa.")
    input_valid = False
elif age > 100:
    st.error("La antigüedad no puede exceder 100 años.")
    input_valid = False

# Botón de predicción (solo si la entrada es válida)
if input_valid:
    if st.button('Predecir Precio'):
        predicted_price = predict_price(area, bedrooms, age)
        st.success(f'El precio predicho de la vivienda es: ${predicted_price:,.2f}')

    # Mostrar los coeficientes del modelo (opcional)
    if st.checkbox('Mostrar detalles del modelo'):
        st.subheader('Detalles del Modelo')
        st.write(f'Coeficiente del área: {model.coef_[0]:.2f}')
        st.write(f'Coeficiente de las habitaciones: {model.coef_[1]:.2f}')
        st.write(f'Coeficiente de la antigüedad: {model.coef_[2]:.2f}')
        st.write(f'Intercepto: {model.intercept_:.2f}')


# In[ ]:




