"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: Comparison between pasive and active investment.                                           -- #
# -- script: functions.py : python script for data collection                                            -- #
# -- author: AraceliCastillo                                                                             -- #
# -- license: GPL-3.0 License                                                                            -- #
# -- repository: https://github.com/AraceliCastillo/myst_if708243_lab1                                   -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""


# Librerias a utilizar

import pandas as pd
from os import listdir
from os.path import isfile
from datetime import datetime
import yfinance as yf

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)

# -- --------------------------------------------------------------------------------------------------- -Paso 1.1 - #
# Obtener los archivos que se van a utilizar

# Definir la ruta en donde se buscaran los archivos
ruta: str = r'files\\NAFTRAC_holdings\\'


def ls1(path):
    """
    Funcion que retorna el nombre de los archivos contenidos en una carpeta local.

    Parameters
    ---------
    path: str: str en el que se especifica la ubicacion de la carpeta a utilizar.

    Returns
    ---------
    files: list: lista que contiene los nombres de los archivos contenidos en la carpeta.

    Debuggin
    ---------
    files = ls1(ruta)

    """
    archivos = [obj for obj in listdir(path) if isfile(path + obj)]
    return archivos


# Archivos contenidos en la carpeta
files = ls1(ruta)

# -- --------------------------------------------------------------------------------------------------- -Paso 1.2 - #
# Ordenar los files obtenidos por fechas


def sort_bydate(archivos):
    """
    Funcion que ordena los archivos obtenidos de la carpeta por fechas.

    Parameters
    ---------
    archivos: list: lista que contiene los nombres de los archivos contenidos en la carpeta.

    Returns
    ---------
    files_date: list: lista que contiene los archivos ordenados por fechas

    Debuggin
    ---------
    files_date = sort_bydate(files)

    """
    # Lista que se usara para guardar las fechas de cada file
    archivos_fecha = []
    # Iteramos sobre cada archivo y realizamos lo que se necesite
    for i in archivos:
        i = i.replace('NAFTRAC_', '')  # Eliminamos la palabra Naftrac
        i = i.replace('.csv', '')  # Eliminamos el .csv
        dia = i[0:2]  # Definimos el día
        mes = i[2:4]  # Definimos el mes
        ano = i[4:6]  # Definimos el ano
        i = dia + '/' + mes + '/' + '20' + ano  # Lo convertimos al formato de la fecha
        i = datetime.strptime(i, '%d/%m/%Y').date()  # Lo convertimos a formato fecha
        archivos_fecha.append(i)  # Lo guardamos en la carpeta correspondiente
    return archivos_fecha


files_date = sort_bydate(files)
files_date.sort()  # Ordenamos los files por fecha

# -- --------------------------------------------------------------------------------------------------- -Paso 1.3 - #
# Obtener tickers y pesos del primer DataFrame para los primeros calculos


def get_datos(file):
    """
    Funcion que retorna los tickers y los pesos del primer Dataframe para hacer inversion pasiva.

    Parameters
    ---------
    file: str: str en el que se especifica de que archivo obtener los datos.

    Returns
    ---------

    f_tickers: lista: lista de los tickers contenidos en la fecha de inversion.
    pesos: lista: lista que contiene los pesos correspondientes a los tickers en la fecha de invesion.

    Debuggin
    ---------
    f_ticker, pesos = get_datos(ruta, 'NAFTRAC_310118' + '.csv')

    """
    # Hacer lo correspondiente a lo que se necesita del primer archivo
    path = ruta + file
    p_archivo = pd.read_csv(path, skiprows=2, usecols=['Ticker', 'Peso (%)'], index_col='Ticker')
    p_archivo = p_archivo.dropna()
    p_archivo = p_archivo.drop(['MXN', 'KOFL', 'BSMXB'], axis=0)

    # Eliminar y agregar al ticker para que los nombres sean correctos
    ticker = []
    for i in p_archivo.index:
        i = i.replace('*', '')
        ticker.append(i + '.MX')

    # Modificar tickers de la lista
    ticker = [i.replace('GFREGIOO.MX', 'RA.MX') for i in ticker]
    ticker = [i.replace('MEXCHEM.MX', 'ORBIA.MX') for i in ticker]
    ticker = [i.replace('LIVEPOLC.1.MX', 'LIVEPOLC-1.MX') for i in ticker]

    p_archivo.index = ticker
    peso = p_archivo['Peso (%)'] / 100

    return ticker, peso


# Nombrar datos constantes para los calculos
f_ticker, pesos = get_datos('NAFTRAC_310118' + '.csv')
V_port = 1000000
Comision = .00125

# -- --------------------------------------------------------------------------------------------------- -Paso 1.4 - #
# Descarga de datos desde yfinance


def get_yfinance(tickers, fecha_i, fecha_f):
    """
    Funcion que descarga los precios para un periodo de tiempo determinado de los tickers unicos.
    La descarga se realiza de Yahoo finance.

    Parameters
    ---------
    tickers: list: lista que contiene los tickers utilizados en la inversion.
    fecha_i: str: fecha de inicio de descarga.
    fecha_f: str: fecha de fin de descarga.

    Returns
    ---------
    data: DataFrame: df que contiene la informacion correspondiente a cada ticker descargado.

    Debuggin
    ---------
    data: get_yfinance(g_tickers, files_date[0], files_date[len(files_date)-1])

    """
    datos = yf.download(tickers, start=fecha_i, end=fecha_f, actions=False,
                        group_by="close", interval='1d', auto_adjust=False, prepost=False,
                        threads=True)
    return datos.T


descarga = get_yfinance(f_ticker, files_date[0], '2020-08-22')
