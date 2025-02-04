import pandas as pd
import yfinance as yf
import mplfinance as mpf
import matplotlib.pyplot as plt

# Indicador: Media Movil Simple (SMA)

def Media_Movil_Simple(df: pd.DataFrame, longitud: int = 21, columna: str = "Close") -> pd.Series:

    """
    La Media Movil Simple (SMA o MA) se utiliza comunmente para indentificar la direccion de la tendencia de una accion
    o para determinar sus niveles de soporte y resistencia. Es un indicador de seguimiento de tendencia - o rezagado - porque
    se basa en los precios pasados.

    Cuanto más largo es el periodo de la media movil, mayor es el rezago. Así que una SMA de 200 dias tendra un mayor grado de
    rezago que una SMA de 20 dias porque contiene precios de los ultimos 200 dias.

    ¿Como operarlo?
    Dado que la SMA se utiliza como niveles de soporte y resistencia, la operacion basica es comprar cerca del soporte en tendencia alcista y
    vender cerca de la resistencia en tendencias bajistas.
    Operar con una SMA puede llevar a malas interpretaciones, y puede ser peligroso. Por eso, operar con SMAs requerira
    una media movil rapida y una lenta. Si la MA rapida cruza de abajo hacia arriba a la MA lenta, esto indica una oportunidad de compra.
    Si la MA rapida cruza de arriba hacia abajo a la MA lenta, esto indica una oportunidad de venta.
    -------------
    Parametros
    -------------
    param: pd.DataFrame: DF : Datos Historicos
    --------------
    param: int : longitud : Ventana a utilizar en el calculo de la SMA (por defecto, se establece 21)
    --------------
    param: str : columna : Columna a utilizar en el calculo de la SMA (por defecto, se establece 'Close')
    --------------
    Salida:
    --------------
    return: pd.Series : Calculo de la media movil simple
    """

    # Calcular

    df = df[columna]
    MA = df.rolling(window=longitud, min_periods=longitud).mean()
    MA.name = "MA"

    return MA

#Obtener datos

df = yf.download("NFLX", start="2024-01-01", end="2025-01-31", interval="1d")

# Calcular indicador

media_mov_9 = Media_Movil_Simple(df, longitud=9, columna="Close")
media_mov_21 = Media_Movil_Simple(df, longitud=21, columna="Close")

# Graficar

media_mov_plots = [
    mpf.make_addplot(media_mov_9, label="Media Movil 9 dias", color= "green", type="line"),
    mpf.make_addplot(media_mov_21, label="Media Movil 21 dias", color= "blue", type="line")
]

mpf.plot(df, type="candle", style="yahoo", volume=True, figsize=(22, 10), addplot=media_mov_plots, figscale=3.0, title="Promedios Moviles")
plt.show()
