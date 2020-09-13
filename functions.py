"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: Comparison between pasive and active investment.                                           -- #
# -- script: functions.py : python script for functions collection                                       -- #
# -- author: AraceliCastillo                                                                             -- #
# -- license: GPL-3.0 License                                                                            -- #
# -- repository: https://github.com/AraceliCastillo/myst_if708243_lab1                                   -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""

import numpy as np
import pandas as pd
from datetime import datetime
import data as dt

# -- --------------------------------------------------------------------------------------------------- -Paso 1.5 - #
# Funcion que te devuelve la lista de precios de las acciones segun la fecha que le envies y tickers.


# Funcion que te devuelve la lista de precios de las acciones segun la fecha que le envies
def get_precio(datos, tickers, fecha):
    """
    Funcion que retorna los precios correspondientes a la fecha y ticker que se solicite.

    Parameters
    ---------
    datos: df: DataFrame que contiene los datos en los que se buscara lo que se solicite.
    tickers: lista: lista de los tickers para los que se solicita el precio.
    fecha: lista: lista de fechas para las que se solicita el precio.

    Returns
    ---------

    precios: lista: precios ordenadors por tickers para la fecha correspondiente

    Debuggin
    ---------
    precios = get_precio(f_ticker, '31-01-18')

    """
    # Definimos la lista en la que se guardaran los precios.
    precios = []
    for j in tickers:
        precio_dia = datos.loc[j, 'Close'][fecha]  # Seleccionamos el precio de close
        # para ticker y fecha correspondiente.
        precios.append(precio_dia)  # Guardamos en la lista los precios.
    return precios

# -- --------------------------------------------------------------------------------------------------- -Paso 1.6 - #
# Definimos nuestra posición de Portafolio en la primer fecha


def get_posicion(datos, ticker, inversion, valor_comision, pesos, fecha_i):
    """
    Funcion que retorna la posicion que se tomara para inversion activa, y el valor del portafolio
    en la fecha inicial de inversion.

    Parameters
    ---------
    datos: df: DataFrame que contiene los datos en los que se buscara lo que se solicite.
    ticker: lista: lista de los tickers que compondran la posicion.
    inversion: float: Dinero con el que inicialas el portafolio.
    valor_comision: float: porcentaje de comision para los movimientos.
    pesos: lista: lista que contiene los pesos correspondientes a los tickers en la fecha de invesion.
    fecha_i: str: fecha de inicio de la inversion.

    Returns
    ---------

    valores_port: list: retorna la lista con el valor del portafolio en la primer fecha.
    cant_acciones: float: cantidad de acciones que se utilizaran para cada accion en la inversion
    comision_sum: float: valor total de la comision por la opercion de compra de acciones
    precios: list: lista de precios de las acciones que del portafolio en la primer fecha

    Debuggin
    ---------
    valores_port = get_posicion(data, f_ticker, V_port, Comision, pesos, files_date[0])

    """
    valores_portafolio = list()  # Definir lista para agregar los valores del portafolio
    valores_portafolio.append(inversion)  # Agregar el primer valor, el valor de inversion
    precios = get_precio(datos, ticker, fecha_i)  # Utilizar la funcion de obtener precios
    valor_actual_portafolio = inversion * pesos  # Calcular cuanto dinero tendremos para cada accion
    # Capital disponible por accion
    capital_poraccion = valor_actual_portafolio - (valor_actual_portafolio * valor_comision)
    cant_acciones = np.trunc(capital_poraccion / precios)  # Cantidad de acciones a comprar
    calculo_comision = cant_acciones * valor_comision * precios  # Calculo de la comision por compra de acciones
    comision_sum = np.sum(calculo_comision)  # Calculo de la comision total
    costo = np.multiply(precios, cant_acciones)  # Calculo del costo total de las acciones
    valores_portafolio.append(np.sum(costo))
    return valores_portafolio, cant_acciones, comision_sum, precios


valores_port, Cant_acciones, suma_comision, precios1 = get_posicion(dt.descarga, dt.f_ticker, dt.V_port, dt.Comision,
                                                                    dt.pesos, dt.files_date[0])

# -- --------------------------------------------------------------------------------------------------- -Paso 1.7 - #
# Calcular el valor del portafolio para cada fecha correspondiente a la inversion pasiva


def get_valores_port(datos, fechas, ticker, cant_acciones, valores_portafolio):
    """
    Funcion que retorna el valor de nuestra posicion en nuestro portafolio para cada cierre de mes

    Parameters
    ---------
    datos: df: dataframe del cual solicitaremos los datos con los que haremos los calculos
    fechas: list: lista de las fechas ordenadas.
    ticker: list: lista de tickers a utilizar en la inversion.
    cant_acciones: list: Cantidad de acciones que se utilizaran en el tiempo determinado
    valores_portafolio: list: lista que contiene los valores hasta el momento calculados de la posicion del portafolio.
    En esta lista se iran guardando los datos calculados.

    Returns
    ---------

    valores_port: list: retorna la lista con los valores del portafolio para cada mes.

    Debuggin
    ---------
    valores_port, V_act_port = get_posicion(data ,f_ticker, V_port, Comision, pesos, files_date[0])

    """

    a = 0
    # Iterar sobre las fechas
    for p in fechas:
        a = a + 1  # Nombrar contador
        if a > 1:  # Calculamos a partir de la segunda fecha de inversion
            precios = get_precio(datos, ticker, p)
            costo = np.multiply(precios, cant_acciones)  # Costo total de acciones
            total_gastado = costo
            v_total = np.sum(total_gastado)
            valores_portafolio.append(v_total)
    return valores_portafolio


valores_port_pasiva = get_valores_port(dt.descarga, dt.files_date, dt.f_ticker, Cant_acciones, valores_port)

# -- --------------------------------------------------------------------------------------------------- -Paso 1.8 - #
# Sumar el valor de cash a cada uno de los valores del portafolio


def get_values_pasiva(valores_portafolio, valor_comision):
    """
    Funcion que retorna los valores que seran necesarios para el DataFrame final de la inversion pasiva.
    Los valores del portafolio, las fechas, los rendimientos.

    Parameters
    ---------
    valores_portafolio: list: lista que contiene los valores del portafolio.
    valor_comision: float: valor correspondiente a la comision de la operacion.

    Returns
    ---------

    valores_port: list: retorna la lista con los valores del portafolio para cada mes con el cash sumado.
    rendimientos: list: lista que retorna los rendimientos mensuales del portafolio.


    Debuggin
    ---------
    valores_port, rendimientos, files_date = get_values_pasiva(valores_port, valor_sinc, files_date)

    """

    # Acomodamos en un DataFrame los valores del portafolio obtenidos
    valores_portafolio = pd.DataFrame(valores_portafolio)

    # Calculamos el valor de cash
    cash = ((dt.V_port - valores_portafolio.iloc[1]) - valor_comision)

    # Sumamos el cash a los valores del portafolio
    for w in range(0, len(valores_portafolio)):
        if w == 0:
            valores_portafolio.loc[w] = 1000000
        else:
            valores_portafolio.loc[w] = valores_portafolio.loc[w] + cash

    # Calcular rendimientos de los valores del portafolio
    rend = valores_portafolio.pct_change().dropna()

    return valores_portafolio, rend


valores_port_pasiva, rendimientos_pasiva = get_values_pasiva(valores_port_pasiva, suma_comision)

# -- --------------------------------------------------------------------------------------------------- -Paso 1.9 - #
# Agregamos a la lista de fechas, un dia antes del comienzo de la inversion

val = datetime.strptime('30/1/2018', '%d/%m/%Y').date()
dt.files_date.append(val)
dt.files_date.sort()


# -- --------------------------------------------------------------------------------------------------- -Paso 1.10 - #
# Obtencion del DataFrame de la inversion pasiva


def get_df(fechas, valores_portafolio, rend):
    """
    Funcion que retorna el Datframe final de inversion pasiva.

    Parameters
    ---------
    fechas: list: lista que contiene las fechas ordenadas de la inversion.
    valores_portafolio: list: lista que contiene los valores del portafolio mas su cash.
    rend: list: lista que contiene los rendimientos de nuestr portafolio de forma mensual

    Returns
    ---------
    df_pasiva: df: dataframe que contiene la informacion de la inversion pasiva en un periodo de tiempo dado.


    Debuggin
    ---------
    df_pasiva = get_df(files_date, valores_port, rendimientos)

    """

    # Creacion de DataFrame final
    pasiva = pd.DataFrame(columns=['timestamp', 'capital', 'rend', 'rend_acum'])
    pasiva['timestamp'] = fechas
    pasiva['capital'] = valores_portafolio
    pasiva['rend'] = rend
    pasiva['rend_acum'] = np.cumsum(rend)
    pasiva.index = pasiva['timestamp']
    del pasiva["timestamp"]
    pasiva = pasiva.fillna(0)
    return pasiva


df_pasiva = get_df(dt.files_date, valores_port_pasiva, rendimientos_pasiva)

# -- --------------------------------------------------------------------------------------------------- -Paso 1.11 - #
# Inversion activa, datos iniciales

# Obtener la posicion y ticker de la accion con mayor ponderacion del portafolio
dt.pesos = pd.DataFrame(dt.pesos)
indice_amax = int(np.where(dt.pesos['Peso (%)'] == max(dt.pesos['Peso (%)']))[0])
ticker_amax = dt.pesos.index[indice_amax]

# Reducir la cantidad de titulos de la accion que tenga la mayor ponderacion
Cant_acciones[indice_amax] = Cant_acciones[indice_amax]*.5

# -- --------------------------------------------------------------------------------------------------- -Paso 1.12 - #
# Calculo de los valores iniciales del portafolio de inversion activa

valores_port = []
comision = Cant_acciones*dt.Comision*precios1
valor_sinc = np.sum(comision)
costo_acciones = np.multiply(precios1, Cant_acciones)
valores_port.append(np.sum(costo_acciones))
Cash = float((dt.V_port-valores_port[0])-valor_sinc)

# -- --------------------------------------------------------------------------------------------------- -Paso 1.13 - #
# Calcular las operaciones que se estaran realizando diariamente con la accion seleccionada
# Las operaciones seran unicamente de compra, segun como este el mercado

# Nombrar listas que seran necesarias para guardar las operaciones realizadas en la inversion
date = []  # Lista en la que seran guardadas las fechas en las que va sucediendo la inversion
titulos_t = []  # Lista en la que se guardaran los titulos que ya poseemos
titulos_c = []  # Lista en la que se guardaran titulos que compramos
precio = []  # Lista en la que se guardara el precio de los titulos
comision_1 = []  # Lista en la que se guardara la comision por operacion
gasto_titulos = []  # Lista en la que se guardara el total gastado por los titulos comprados
lista_cash = []  # Lista en la que se guardar el cash por fecha

# Asignar el primer valor que le corresponde a cada lista
date.append(dt.files_date[1])
titulos_t.append(Cant_acciones[indice_amax])
titulos_c.append(Cant_acciones[indice_amax])
precio.append(precios1[indice_amax])
comision_1.append(comision[indice_amax])
gasto_titulos.append(costo_acciones[indice_amax])
lista_cash.append(Cash)

# Calculos para registrar las operaciones realizadas durante el tiempo de inversion de forma diaria


def get_operaciones(datos, fechas, cash_disponible, val_comision):
    """
       Funcion que calcula las operaciones diarias de inversion activa

       Parameters
       ---------
       datos: df: DataFrame que contiene los datos de precios a utilizar
       fechas: list: lista que contiene las fechas ordenadas de la inversion.
       cash_disponible: float: cash calculado con el valor inicial del portafolio
       val_comision: float: porcentjae de comision por operaciones.

       Returns
       ---------
       date: list: lista que contiene las fechas diarias de los calculos
       titulos_t: lista: lista que contiene los titulos que tenemos dia con dia
       titulos_c: lista: lista que contiene los titulos que compramos dia con dia
       precio: lista: lista que contiene los precios de las acciones.
       comision_1: lista: lista que contiene las comisiones de las operaciones.
       lista_cash: lista: lista que contiene los valores de cash para cada fecha.

       Debuggin
       ---------
       date, titulos_t, titulos_c, precio, comision_1 = get_operaciones(dt.descarga, dt.files_date, Cash, dt.Comision)

       """
    for k in range(0, len(datos.columns) - 1):

        t = datos.columns[k + 1]  # Nombro la fecha del dia de hoy
        tm1 = datos.columns[k]  # Nombro la fecha del dia de ayer

        ayer_apertura = float(datos.loc[ticker_amax, 'Open'][tm1])  # Nombro el precio de ayer de apertura
        ayer_cierre = float(datos.loc[ticker_amax, 'Close'][tm1])  # Nombre el precio de ayer de cierre
        hoy_apertura = float(datos.loc[ticker_amax, 'Open'][t])  # Nombro el precio de hoy de apertura
        hoy_cierre = float(datos.loc[ticker_amax, 'Close'][t])  # Nombro el precio de hoy de cierre
        porcen = (ayer_cierre - ayer_apertura) / ayer_cierre  # Porcentaje de cambio entre
        # precio de apertura y cierre ayer
        # Si el cambio es mayor al 1% y el precio de apertura es mayor al de cierre comprar
        if t in fechas:
            precio_dia = hoy_cierre  # Si es cierre de mes usamos el precio de cierre
        else:
            precio_dia = hoy_apertura  # Si es un dia entre el mes usamos precio de apertura

        if porcen < -.01:
            # Verificar si es un cierre de mes
            capital = .1 * cash_disponible  # Utilizaremos el 10% del cash para comprar
            comision_calculada = (capital * val_comision)
            capital = capital - comision_calculada
            cant_titulos = np.trunc(
                capital / precio_dia)  # Calculamos la cantidad de titulos para la que nos alcanza y truncamos
            gasto = precio_dia * cant_titulos
            comision_real = precio_dia * cant_titulos * val_comision
            gasto_titulos.append(gasto)  # Calculamos lo que nos va a costar
            cash_disponible = cash_disponible - gasto - comision_real  # Le restamos al cash lo que nos va a costar
            lista_cash.append(float(cash_disponible))

            date.append(t)
            titulos_c.append(cant_titulos)
            comision_1.append(cant_titulos * val_comision * precio_dia)
            titulos_t.append(titulos_t[k] + titulos_c[k + 1])
            precio.append(precio_dia)
        else:
            date.append(t)
            titulos_t.append(titulos_t[k])
            titulos_c.append(0)
            comision_1.append(0)
            precio.append(0)
            gasto_titulos.append(costo_acciones[indice_amax])
            lista_cash.append(cash_disponible)

    return date, titulos_t, titulos_c, precio, comision_1, lista_cash


date, titulos_t, titulos_c, precios_diarios, comision_1, lista_cash = get_operaciones(dt.descarga, dt.files_date, Cash,
                                                                                      dt.Comision)

# -- --------------------------------------------------------------------------------------------------- -Paso 1.14 - #
# Creacion del DataFrame de las operaciones diarias


def get_df_operaciones(fechas, titulos1, titulos2, precios, comisiones):
    """
       Funcion que regresa el DataFrame diario de las operaciones de inversion activa

       Parameters
       ---------
       fechas: list: lista que contiene las fechas diarias de los calculos
       titulos1: lista: lista que contiene los titulos que tenemos dia con dia
       titulos2: lista: lista que contiene los titulos que compramos dia con dia
       precios: lista: lista que contiene los precios de las acciones.
       comisiones: lista: lista que contiene las comisiones de las operaciones

       Returns
       ---------
       df_operaciones: df: DataFrame que contiene las operaciones diarias de la inversion activa

       Debuggin
       ---------
       date, titulos_t, titulos_c, precio, comision_1 = get_operaciones(dt.descarga, dt.files_date, Cash, dt.Comision)

       """
    operaciones = pd.DataFrame(columns={'timestamp', 'titulos_t', 'titulos_c', 'precio', 'comision', 'comision_acum'})
    operaciones['timestamp'] = fechas
    operaciones['titulos_t'] = titulos1
    operaciones['titulos_c'] = titulos2
    operaciones['precio'] = precios
    operaciones['comision'] = comisiones
    operaciones['comision_acum'] = np.cumsum(comisiones)
    operaciones.index = operaciones['timestamp']
    del operaciones["timestamp"]
    return operaciones


df_operaciones = get_df_operaciones(date, titulos_t, titulos_c, precios_diarios, comision_1)

# -- --------------------------------------------------------------------------------------------------- -Paso 1.14 - #
# Obtener datos y DataFrame de inversion Activa
# Calculo de los valores mensuales de la inversion activa

# Cantidad de titulos que se tuvo en cada cierre de mes
titulos_pormes = []
for i in range(1, len(dt.files_date)):
    titulos_pormes.append(df_operaciones.loc[dt.files_date[i]]['titulos_t'])

# Calculo de los valores del portafolio mensuales de la inversion activa


def get_values_activa(fechas, tickers, val_comision, datos):
    """
        Funcion que calcula los valores mensuales del portafolio inversion activa

        Parameters
        ---------
        fechas: list: lista que contiene las fechas diarias de los calculos
        tickers: list: lista de tikcers que componene nuestro portafolio
        val_comision: float: porcentaje de comision que se cobra por operacion
        datos: df: DataFrame que contiene los valores de los precios a utilizar

        Returns
        ---------
        valores_portafolio: list: lista que contiene los valores del portafolio mensuales de inversion
        activa sin su cash

        Debuggin
        ---------

        """
    comisiones_pormes = []
    valores_portafolio = [1000000]
    for j in range(1, len(fechas)):
        precios = get_precio(datos, tickers, fechas[j])
        Cant_acciones[indice_amax] = titulos_pormes[j-1]
        calculo_comision = Cant_acciones*val_comision*precios
        if j > 1:
            sum_comision = np.sum(calculo_comision[indice_amax])
            comisiones_pormes.append(sum_comision)
        else:
            sum_comision = np.sum(comision)
            comisiones_pormes.append(sum_comision)
        costo = np.multiply(precios, Cant_acciones)
        gasto = np.sum(costo)
        valores_portafolio.append(gasto)
    return valores_portafolio


valores_port = get_values_activa(dt.files_date, dt.f_ticker, dt.Comision, dt.descarga)

# Agregar el cash a cada valor del portafolio correspondiente


def add_cash_activa(fechas1, fechas2, portafolio, l_cash):
    df_cash = pd.DataFrame(columns=['timestamp', 'cash'])
    df_cash['timestamp'] = fechas2
    df_cash['cash'] = l_cash
    df_cash.index = df_cash['timestamp']
    del df_cash['timestamp']

    cash_value = []
    for a in range(1, len(fechas1)):
        cash_value.append(float(df_cash.loc[fechas1[a]]))

    for v in range(0, len(portafolio)):
        if v == 0:
            portafolio[v] = 1000000
        else:
            portafolio[v] = portafolio[v]+cash_value[v-1]

    portafolio = pd.DataFrame(portafolio)

    return portafolio


valores_port_activa = add_cash_activa(dt.files_date, date, valores_port, lista_cash)

# Sacamos los rendimientos de la serie de tiempo de los valores del portafolio)
rendimientos_activa = valores_port_activa.pct_change().dropna()

# Obtener DataFrame Mensual de la inversion activa
df_activa = get_df(dt.files_date, valores_port_activa, rendimientos_activa)

# -- --------------------------------------------------------------------------------------------------- -Paso 1.16 - #
# Obtener el cuadro de comparacion entre ambas inversiones

# Obtencion de datos
# Calculo de Sharpe
rf = (7.7/12) / 100
media_pasiva = float(np.mean(df_pasiva.loc[dt.files_date[1]:]['rend']))
desves_pasiva = float(np.std(df_pasiva.loc[dt.files_date[1]:]['rend']))
media_activa = float(np.mean(df_activa.loc[dt.files_date[1]:]['rend']))
desves_activa = float(np.std(df_activa.loc[dt.files_date[1]:]['rend']))
sharpe_a = (media_activa - rf)/desves_activa
sharpe_p = (media_pasiva - rf)/desves_pasiva

# Creacion de DataFrame

df_medidas = pd.DataFrame(columns=['medida', 'descripcion', 'inv_activa', 'inv_pasiva'])
df_medidas['medida'] = ['rend_m', 'rend_c', 'sharpe']
df_medidas['descripcion'] = ['Rendimiento Promedio Mensual', 'Rendimiento Mensual Acumulado', 'Sharpe Ratio']
df_medidas['inv_activa'] = [media_activa, df_activa.loc[dt.files_date[len(dt.files_date)-1]]['rend_acum'], sharpe_a]
df_medidas['inv_pasiva'] = [media_pasiva, df_pasiva.loc[dt.files_date[len(dt.files_date)-1]]['rend_acum'], sharpe_p]
df_medidas.index = df_medidas['medida']
del df_medidas["medida"]
