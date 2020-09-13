"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: Comparison between pasive and active investment.                                           -- #
# -- script: visualizations.py : python script for visualization collection                              -- #
# -- author: AraceliCastillo                                                                             -- #
# -- license: GPL-3.0 License                                                                            -- #
# -- repository: https://github.com/AraceliCastillo/myst_if708243_lab1                                   -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""
import pandas as pd
import functions as ft
import plotly.express as px
import data as dt

# -- --------------------------------------------------------------------------------------------------- -Paso 1.17 - #
# Visualización de los valores del portafolio a traves del tiempo activa y pasiva


def get_chart_valoresportafolio(fecha, activo, pasivo):
    """
    Funcion que retorna la gráfica comparativa de los valores del portafolio en el tiempo

    Parameters
    ---------
    fecha: list: lista de fechas de la inversion de forma mensual.
    activo: df: DataFrame que contiene los valores de inversion activa en el tiempo.
    pasivo: df: DataFrame que contiene los valores de inversion activa en el tiempo.

    Returns
    ---------
    Grafica de los valores del portafolio.

    Debuggin
    ---------
    vs.get_chart_valoresportafolio(dt.files_date, ft.valores_port_activa, ft.valores_port_pasiva)

    """
    df = pd.DataFrame(columns=['fecha', 'Inversion_activa', 'Inversion_pasiva'])
    df['fecha'] = fecha
    df['Inversion_activa'] = activo
    df['Inversion_pasiva'] = pasivo
    df.index = df['fecha']
    del df["fecha"]

    fig = px.line(df, height=400, width=900, title='Valores del Portafolio')
    fig.show()

# -- --------------------------------------------------------------------------------------------------- -Paso 1.18 - #
# Visualización de los rendimientos para activa y para pasiva a lo largo del tiempo


def get_chart_rendimientos(fecha1, r_activo, r_pasivo):
    """
     Funcion que retorna la gráfica comparativa de los valores del portafolio en el tiempo

     Parameters
     ---------
     fecha1: list: lista de fechas de la inversion de forma mensual.
     r_activo: df: DataFrame que contiene los rendimientos mensuales de la inversion de inversion activa.
     r_pasivo: df: DataFrame que contiene los rendimientos mensuales de la inversion de inversion pasiva.

     Returns
     ---------
     Grafica de los rendimientos del portafolio

     Debuggin
     ---------
     vs.get_chart_valoresportafolio(dt.files_date, ft.rendimientos_activa, ft.rendimientos_pasiva)

     """
    df = pd.DataFrame(columns=['fecha', 'Rendimientos_activa', 'Rendimientos_pasiva'])
    df['fecha'] = fecha1
    df['activa'] = r_activo
    df['pasiva'] = r_pasivo
    df.index = df['fecha']
    del df["fecha"]

    fig = px.line(df, height=400, width=900, title='Valores del Portafolio')
    fig.show()


get_chart_valoresportafolio(dt.files_date, ft.rendimientos_activa, ft.rendimientos_pasiva)

# -- --------------------------------------------------------------------------------------------------- -Paso 1.19 - #
# Visualización de los pesos del portafolio


def get_chart_pesos(peso):
    """
     Funcion que retorna la gráfica de los pesos de cada accion en el portafolio

     Parameters
     ---------
     peso: list: ponderacion de las acciones en el portafolio


     Returns
     ---------
     Grafica de las ponderaciones del portafolio para cada accion

     Debuggin
     ---------
     vs.get_chart_pesos(dt.pesos)

     """

    fig = px.bar(peso, y='Peso (%)', title="Pesos para las acciones que componen la inversion", height=400, width=800)
    fig.show()
