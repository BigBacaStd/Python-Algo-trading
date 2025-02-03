# Importar librerias

import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
import mplfinance as mpf
import plotly.graph_objects as go
import pandas as pd
import webbrowser

# Parametros de descarga

ticker = "AMZN"
fecha_inicial = "2024-01-01"
fecha_final = "2025-02-03"

# Descarga de datos

datos = yf.download(ticker, start=fecha_inicial, end=fecha_final, interval="1d")

# Eliminar Nivel 1 de Columnas
datos.columns = datos.columns.droplevel(1)

# Grafico 1: Precio de Cierre usanto matplotlib

plt.figure(figsize=(12,6))
plt.plot(datos.index, datos["Close"], label="Precio de Cierre", color="blue")
plt.xlabel("Fecha")
plt.ylabel("Precio de Cierre")
plt.title("Precio de Cierre de Amazon" + ticker)
plt.legend()
plt.grid(True)
plt.show()

# Grafico 2: Subplots para el precio de cierre, bajo, alto y apertura

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(22,2))

# Precio de cierre

axes[0,0].plot(datos.index, datos["Close"], color="green")
axes[0,0].set_title("Precio de Cierre")
axes[0,0].set_ylabel("Precio")
axes[0,0].grid()

# Precio Bajo

axes[0,1].plot(datos.index, datos["Low"], color="red")
axes[0,1].set_title("Precio de Bajo")
axes[0,1].set_ylabel("Precio")
axes[0,1].grid()

# Precio Alto

axes[1,0].plot(datos.index, datos["High"], color="blue")
axes[1,0].set_title("Precio Alto")
axes[1,0].set_ylabel("Precio")
axes[1,0].grid()

# Precio Apertura

axes[1,1].plot(datos.index, datos["Open"], color="purple")
axes[1,1].set_title("Precio Apertura")
axes[1,1].set_ylabel("Precio")
axes[1,1].grid()

plt.tight_layout()
plt.show()

# Grafica 3: Rendimientos usando Seaborn

datos["Rendimiento_Simple"] = datos["Close"].pct_change()
datos.dropna(inplace=True)

plt.figure(figsize=(12,6))
sns.lineplot(x=datos.index, y=datos["Rendimiento_Simple"], color= "orange")
plt.xlabel("Fecha")
plt.ylabel("Rendimiento Simple")
plt.title("Rendimiento simple para el activo")
plt.grid(True)
plt.show()

# Grafico 4: Grafico de candlesticks usando mplfinance

mpf.plot(datos, type="candle", style="yahoo", title="Grafico de Velas", ylabel="Precio", volume=True,figsize=(22, 10),
         figscale=3.0, mav=(9, 21))
plt.show()

# Grafico 5: Grafico de velas usando Plotly

fig = go.Figure(data=[
    go.Candlestick(x=datos.index,
                   open=datos["Open"],
                   high=datos["High"],
                   low=datos["Low"],
                   close=datos["Close"])
])

fig.update_layout(
    title="Grafico de Velas con Plotly",
    xaxis_title="Fecha",
    yaxis_title="Precio",
    width=1500, #Ancho en pixeles
    height=700, #Altura en pixeles

)

# Guardar el grafico en un archivo html
fig.write_html("grafico_de_velas.html")


# Abrir el archivo en el navegador
webbrowser.open("grafico_de_velas.html")

# Recordatorio

# - El uso de herramientas visuales nos ayuda a ver patrones y entender los datos de manera más clara y rapida.