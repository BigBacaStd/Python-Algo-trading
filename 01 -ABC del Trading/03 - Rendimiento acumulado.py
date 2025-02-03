# Importar librerias

import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

# Definiar accion

ticker = "AMZN"

# Descargar datos

datos = yf.download(ticker, start="2023-01-01", end="2025-01-20", interval="1d")

# Calcular el rendimiento simple

datos["Rendimiento_Simple"] = datos["Close"].pct_change()

# Calcular el rendimiento logaritmico

datos["Rendimiento_Logaritmico"] = np.log(datos["Close"]/ datos["Close"].shift(periods=1))

# Calcular rendimiento simple acumulado

datos["Rendimiento_Simple_Acumulado"] = (1 + datos["Rendimiento_Simple"]).cumprod() - 1

# Calcular rendimiento logaritmico acumulado

datos["Rendimiento_Logaritmico_Acumulado"] = np.exp(datos["Rendimiento_Logaritmico"].cumsum()) - 1

# Mostrar los primeros registros

print("Datos con Rendimiento Simple, Logaritmico, y Acumulado:\n")
print(datos[["Rendimiento_Simple_Acumulado", "Rendimiento_Logaritmico_Acumulado"]].head())

# Graficas

plt.figure(figsize=(14,7))

# Grafica de rendimeinto simple acumulado

plt.subplot(2, 1, 1)
plt.plot(datos.index, datos["Rendimiento_Simple_Acumulado"], label="Rendimiento Simple Acumulado", color="blue")
plt.xlabel("Fecha")
plt.ylabel("Rendimiento Acumulado")
plt.title("Rendimiento Simple Acumulado")
plt.legend()


# Grafica de rendimeinto Logaritmico acumulado

plt.subplot(2, 1, 2)
plt.plot(datos.index, datos["Rendimiento_Logaritmico_Acumulado"], label="Rendimiento Logaritmico Acumulado", color="red")
plt.xlabel("Fecha")
plt.ylabel("Rendimiento Acumulado")
plt.title("Rendimiento Logaritmico Acumulado")
plt.legend()

plt.tight_layout()
plt.show()


# Recordatorio

# - El rendimiento acumulado representa el crecimiento total de una inversion a lo largo de un periodo.

# - Calculando el rendimiento a partir del rendimiento diario compuesto, nos permite observar como se ha acumulado el rendimiento total.

#    Considereando los efectos de la capitalizacion diaria a lo largo del tiempo.