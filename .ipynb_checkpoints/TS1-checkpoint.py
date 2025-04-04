# -*- coding: utf-8 -*-
"""
Created on Wed Apr  2 11:11:41 2025

@author: Usuario
"""
import numpy as np
import matplotlib.pyplot as plt

def mi_funcion_sen(vmax, dc, ff, ph, nn, fs):
    """
    Genera una señal senoidal parametrizable.
    
    Parámetros:
    vmax : Amplitud máxima de la senoidal (volts)
    dc   : Valor medio (volts)
    ff   : Frecuencia de la señal (Hz)
    ph   : Fase de la señal (radianes)
    nn   : Cantidad de muestras digitalizadas por el ADC
    fs   : Frecuencia de muestreo del ADC (Hz)
    
    Retorna:
    tt : Vector de tiempos (s)
    xx : Vector de valores de la señal
    """
    tt = np.arange(0, (nn-1) / fs, 1 / fs)  # Vector de tiempo
    xx = vmax * np.sin(2 * np.pi * ff * tt + ph) + dc  # Señal senoidal
    
    return tt, xx

# Ejemplo de uso:
N = 1000  # Número de muestras
fs = 1000 # Frecuencia de muestreo

tt, xx = mi_funcion_sen(vmax=1, dc=0, ff=2, ph=0, nn=N, fs=fs)

# Graficar la señal
tl, xl = plt.subplots()
plt.plot(tt, xx)
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud (V)")
plt.title("Señal Senoidal")
plt.grid()
plt.show()
