import streamlit as st
import pandas as pd

# CARGA DE DATOS ==============================================================================

ruta = 'data\Estado_de_la_prestación_del_servicio_de_energía_en_Zonas_No_Interconectadas_20260422 (1).csv'
df = pd.read_csv(ruta)

## ANALISIS DE DATOS ===========================================================================
filas = df.shape[0]
columnas = df.shape[1]

## VISUALIZACION DE DATOS ======================================================================

col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.text("Número de filas")
        st.subheader(filas)

with col2:
    with st.container(border=True):
        st.text("Número de columnas")
        st.subheader(columnas)

### otra forma de mostrar los indicadores

col3, col4 = st.columns(2)
with col3:
    st.metric("Número de filas", filas, border=True)
with col4:
    st.metric("Número de columnas", columnas, border=True) 

print("holamundo")   


