"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: A SHORT DESCRIPTION OF THE PROJECT                                                         -- #
# -- script: data.py : python script for data collection                                                 -- #
# -- author: YOUR GITHUB USER NAME                                                                       -- #
# -- license: GPL-3.0 License                                                                            -- #
# -- repository: YOUR REPOSITORY URL                                                                     -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""

import data as dt
import functions as ft

# -- ------------------------------------------------------------------------ Obtener, limpiar y acomodar los datos - #

# Obtener los archivos que se van a utilizar
files = dt.files
# Obtener lista de los archivos ordenados por fecha
files_date = dt.files_date
# Obtener datos descargados de Yahoo Finance para hacer los calculos
descarga = dt.descarga
# Obtener los datos correspondientes a la fecha de inversion necesarios para hacer los calculos
f_ticker = dt.f_ticker
pesos = dt.pesos
V_port = dt.V_port
Comision = dt.Comision

# -- -------------------------------------------- Obtener valores del portafiolio y rendimientos de inversion pasiva- #

# Calcular el valor de la posicion del portafolio para inversion pasiva en la primera fecha
# Calcular el valor del portafolio para cada cierre de mes en la inversion pasiva
valores_port = ft.valores_port
# Obtener los valores de rendimientos
rendimientos = ft.rendimientos

# -- ------------------------------------------------------ DataFrame que contiene los datos de la inversion pasiva - #

# Obtener el dataframe para ver la evolucion de nuestro portafolio a lo largo de los meses.
df_pasiva = ft.df_pasiva

# -- ------------------------------------------------------------------------ Datos iniciales de la inversion Activa- #

# Indice y ticker de la accion que tenga mayor ponderacion en el portafolio
ticker = ft.ticker_amax
indice = ft.indice_amax

# Reducir la cantidad de titulos de la accion que tenga la mayor ponderacion
acciones_amax = ft.Cant_acciones[indice]

# -- ------------------------------------------------------ DataFrame que contiene los datos de la inversion activa - #

# Obtener el dataframe para ver la evolucion de nuestro portafolio a lo largo de los meses.
df_activa = ft.df_activa

# -- ---------------------------------------- DataFrame que contiene las operaciones diarias de la inversion activa - #

df_operaciones = ft.df_operaciones

# -- -------------------------------------------------- DataFrame que contiene una comparacion de ambas inversiones - #

df_medidas = ft.df_medidas
