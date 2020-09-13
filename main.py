"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: Comparison between pasive and active investment.                                           -- #
# -- script: main.py : python script for main statements                                                 -- #
# -- author: AraceliCastillo                                                                             -- #
# -- license: GPL-3.0 License                                                                            -- #
# -- repository: https://github.com/AraceliCastillo/myst_if708243_lab1                                   -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""


import data as dt
import functions as ft

# -- Paso 1.1 --
# -- ------------------------------------------------------------------------ Obtener, limpiar y acomodar los datos - #

# Obtener los archivos que se van a utilizar
files = dt.files
# Obtener lista de los archivos ordenados por fecha
files_date = dt.files_date
# Obtener los datos correspondientes a la fecha de inversion necesarios para hacer los calculos
f_ticker = dt.f_ticker
pesos = dt.pesos
V_port = dt.V_port
Comision = dt.Comision
# Obtener datos descargados de Yahoo Finance para hacer los calculos
descarga = dt.descarga

# -- Paso 1.2 --
# -- ---------------------------------- Obtener valores del portafiolio y rendimientos mensuales de inversion pasiva- #

# Calcular el valor de la posicion del portafolio para inversion pasiva en la primera fecha
# Calcular el valor del portafolio para cada cierre de mes en la inversion pasiva
valores_port_pasiva = ft.valores_port_pasiva
# Obtener los valores de rendimientos
rendimientos_pasiva = ft.rendimientos_pasiva

# -- Paso 1.3 --
# -- ------------------------------------------------------ DataFrame que contiene los datos de la inversion pasiva - #

# Obtener el dataframe para ver la evolucion de nuestro portafolio a lo largo de los meses.
df_pasiva = ft.df_pasiva

# -- Paso 1.4 --
# -- ------------------------------------------------------------------------ Datos iniciales de la inversion Activa- #

# Indice y ticker de la accion que tenga mayor ponderacion en el portafolio
ticker = ft.ticker_amax
indice = ft.indice_amax

# Reducir la cantidad de titulos de la accion que tenga la mayor ponderacion
acciones_amax = ft.Cant_acciones[indice]

# -- Paso 1.5 --
# -- ----------------- Datos obtenidos de forma diaria para el control del avance del portafolio y la creacion de df- #

fechas_diarias = ft.date
titulos_pertenecientes = ft.titulos_t
titulos_comprados = ft.titulos_c
precios_diarios = ft.precios_diarios
comision_diaria = ft.comision_1
cash_diario = ft.lista_cash

# -- Paso 1.6 --
# -- ---------------------------------- Obtener valores del portafiolio y rendimientos mensuales de inversion activa- #

# Calcular el valor de la posicion del portafolio para inversion pasiva en la primera fecha
# Calcular el valor del portafolio para cada cierre de mes en la inversion pasiva
valores_port_activa = ft.valores_port_activa
# Obtener los valores de rendimientos
rendimientos_activa = ft.rendimientos_activa

# -- Paso 1.7 --
# -- ------------------------------------------------------ DataFrame que contiene los datos de la inversion activa - #

# Obtener el dataframe para ver la evolucion de nuestro portafolio a lo largo de los meses.
df_activa = ft.df_activa

# -- Paso 1.8 --
# -- ---------------------------------------- DataFrame que contiene las operaciones diarias de la inversion activa - #

df_operaciones = ft.df_operaciones

# -- Paso 1.9 --
# -- -------------------------------------------------- DataFrame que contiene una comparacion de ambas inversiones - #

df_medidas = ft.df_medidas
