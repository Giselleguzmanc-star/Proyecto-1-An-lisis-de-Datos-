import streamlit as pd st
import pandas as pd

# CARGA DE DATOS

ruta_zni = 'data/ZNI.csv'
ruta_divipola = 'data/DIVIPOLA.csv'

df_zni = pd.read_csv(ruta_zni)
df_divipola = pd.read_csv(ruta_divipola)

#🪁🪁🪁🪁🪁🪁🪁🪁🪁🪁🪁🪁🪁🪁🪁🪁🪁🪁🪁🪁🪁🪁🪁🪁🪁🪁🪁🪁🪁🪁🪁🪁🪁🪁🪁🪁🪁🪁🪁🪁🪁🪁
# ANALISIS DE DATOS 

# TRAER EL NOMBRE OFICIAL DEL DEPARTAMENTO
df_zni = df_zni.merge(
    df_divipola[['Código Departamento','Nombre_departamento']].drop_duplicates('Código Departamento'),
    left_on='ID DEPATAMENTO',
    right_on='Código Departamento',
    how='left'
)

df_zni['DEPARTAMENTO'] = df_zni['Nombre_departamento']
df_zni = df_zni.drop(columns=['Código Departamento','Nombre_departamento'])

## 🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈🎈

# TRAER EL NOMBRE OFICIAL DE MUNICIPIO
df_zni = df_zni.merge(
    df_divipola[['Codigo Municipio','Nombre Municipio']].drop_duplicates('Codigo Municipio'),
    left_on='ID MUNICIPIO',
    right_on='Codigo Municipio',
    how='left'
)

df_zni['MUNICIPIO'] = df_zni['Nombre Municipio']
df_zni = df_zni.drop(columns=['Codigo Municipio','Nombre Municipio'])

## 💎💎💎💎💎💎💎💎💎💎💎💎💎💎💎💎💎💎💎💎💎💎💎💎💎💎💎💎💎💎💎💎💎💎💎💎💎💎💎💎💎💎💎💎

# TRAER EL NOMBRE OFICIAL DE LA LOCALIDAD
df_zni = df_zni.merge(
    df_divipola[['Código Centro Poblado','Nombre Centro Poblado']].drop_duplicates('Código Centro Poblado'),
    left_on='ID LOCALIDAD',
    right_on='Código Centro Poblado',
    how='left'
)

df_zni['LOCALIDAD'] = df_zni['Nombre Centro Poblado']
df_zni = df_zni.drop(columns=['Código Centro Poblado','Nombre Centro Poblado'])

# corregir nombres de dia
## todos a mayusculas
df_zni['DÍA DE DEMANDA MÁXIMA'] = df_zni['DÍA DE DEMANDA MÁXIMA'].str.upper()

## listado con y sin tilde
viejos = ['MIERCOLES', 'SABADO']
nuevos = ['MIÉRCOLES', 'SÁBADO']

## Crear un DICCIONARIO con las listas EMPAQUETADAS
Reemplazos = dict(zip(viejos,nuevos))

## Reemplazar usando los diccionarios
df_zni['DÍA DE DEMANDA MÁXIMA'] = df_zni['DÍA DE DEMANDA MÁXIMA'].replace(Reemplazos,regex=True)

# eliminar todos los datos nulos- ojo revisar
# CORREGIR PROBLEMAS CON COLUMNAS NUMERICAS QUE SON OBJECT

df_zni['ENERGÍA ACTIVA'] = df_zni['ENERGÍA ACTIVA'].str.replace('.','',regex=False).astype(int)
df_zni['ENERGÍA REACTIVA'] = df_zni['ENERGÍA REACTIVA'].str.replace('.','',regex=False).astype(int)

df_zni.dropna(inplace = True)
df_zni['POTENCIA MÁXIMA'] = df_zni['POTENCIA MÁXIMA'].str.replace('.','',regex=False)
df_zni['POTENCIA MÁXIMA'] = df_zni['POTENCIA MÁXIMA'].str.replace(',','.',regex=False).astype(float).astype(int)

# AGRUPAR LOS DATOS POR DEPARTAMENTO Y POR MUNICIPIO
# SUMANDO LOS VALORES DE ENERGIA ACTIVA Y REACTIVA

df_agrupado = df_zni.groupby(['DEPARTAMENTO','MUNICIPIO'])[['ENERGÍA ACTIVA','ENERGÍA REACTIVA']].sum()

df_pivote = df_zni.pivot_table(
    index = 'DEPARTAMENTO',
    columns= 'AÑO SERVICIO',
    values= ['ENERGÍA ACTIVA'],
    aggfunc='sum'
)

# CONFIGURACION DE STREAMLIT

# VISUALIZACION DE DATOS ❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️

st.
