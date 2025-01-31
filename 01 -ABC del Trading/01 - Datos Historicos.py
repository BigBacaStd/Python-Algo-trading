# Importar librerias

import yfinance as yf
from datetime import datetime, timedelta
import os


# Configuracion de parametros

ticker = "AAPL"  # Ticker de la accion a analizar
fecha_inicial = "2023-01-01"  # Fecha inicial para el analisis
fecha_final = "2025-01-20"
intervalo = "1d"

# Descargar datos historicos de Yahoo Finance

datos = yf.download(ticker, start=fecha_inicial, end=fecha_final, interval=intervalo)

# Mostrar los primeros registros

print("Datos Historicos:")
print(datos.head())

# Guardar los datos en un archivo csv

if not os.path.isdir("../datos"):
    os.mkdir("../datos")
    datos.to_csv("../datos/datos_historicos2.csv")


# Ejemplos de uso de diferentes activos e intervalos de tiempo

# Ejemplo 1: Descargar datos con intervalos de 1 minuto (limitado a aproximadamente 7 dias)


intervalo_1m = yf.download(tickers="EURUSD=X", interval="1m")
print("Datos con intervalo de 1 minuto:")
print(intervalo_1m)

# Ejemplo 2: Descargar datos con intervalos de 15 minutos (limitado a aproximadamente 60 dias)

fecha_final = datetime.now()
fecha_inicial = fecha_final - timedelta(days=30)
fecha_final = fecha_final.strftime("%Y-%m-%d")
fecha_inicial = fecha_inicial.strftime("%Y-%m-%d")
intervalo_15 = yf.download(tickers="BTC-USD", start=fecha_inicial, end=fecha_final, interval="15m")
print("Datos con intervalo de 15 minutos:")
print(intervalo_15)

# Ejemplo 3: Descargar datos con intervalos de 1 dia (No existe limite de tiempo)

intervalo_1d = yf.download(tickers="XYD", start="2010-01-01", end="2024-01-01", interval="1d")
print("Datos con intervalo de 1 dia:")
print(intervalo_1d)

# Ejemplo 4: Descargar todos los datos historicos para un instrumento

accion = yf.Ticker(ticker=ticker)
accion_hist = accion.history(period="max", end=fecha_final, interval="1d")
print("Todos los datos historicos:")
print(accion_hist)
#Imprimir Fechas de Dividendos

print(accion_hist["Dividends"][accion_hist["Dividends"] != 0.0])
#imprimir splits
print(accion_hist["Stock Splits"][accion_hist["Stock Splits"] != 0.0])

# Recordatorio:

#  - Yahoo Finance es un proveedor de datos historicos por excelencia (El más utilizado en el mercado).
#  - Yahoo Finance puede limitar la frecuencia de las consultas si se realizan demasiadas peticiones
#  en un corto periodo de tiempo.