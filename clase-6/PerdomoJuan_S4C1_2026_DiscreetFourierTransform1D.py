#EJERCICIO 1

import numpy as np
import matplotlib.pylab as plt
from scipy.fftpack import fft, fftfreq

# Construcción de la señal
N = 128 # number of point in the whole interval
f = 200.0 #  frequency in Hz
dt = 1 / (f * 32 ) #32 samples per unit frequency
t = np.linspace( 0, (N-1)*dt, N)
y = np.cos(2 * np.pi * f * t) - 0.4 * np.sin(2 * np.pi * (2*f) * t )+ 0.17*np.sin(2 * np.pi * (15*f) * t )

# 1) implemente la transformada de fourier discreta

X_k = np.zeros(N, dtype = complex)
n = np.linspace(0, N-1, N, dtype = int)

for k in range(N):
    X_k[k] = np.sum(y * np.exp(-1*1j*2*np.pi*k*n/N))

X_k = X_k/np.max(X_k)

# 2) Genere el arreglo de las frecuencias (ver documentación de fftfreq):

#freq_mp =

# 3) Haga una gráfica comparando su método propio con la implementación de scipy.fftpack.fft

fft_x = fft(y) / N  # FFT Normalized
freq = fftfreq(N, dt) # Recuperamos las frecuencias

plt.plot(freq, np.abs(fft_x))
plt.plot(freq, np.abs(X_k))
plt.show()

#EJERCICIO 2

# 1) Almacene los datos de signal.dat. La columna 1 es el tiempo y la columna 2 es su señal f(t).
#Grafique su señal en función del tiempo.

signal_matrix = np.genfromtxt('signal.dat', delimiter =',')
time = signal_matrix[:, 0]
signal = signal_matrix[:, 1]

plt.plot(time, signal)
plt.show()

# 2) Use fftfreq (BONO si usa su implementación propia) y haga una gráfica de su transformada de fourier en función de las frecuencias.



# 3) Haga un filtro pasa bajos que le permita filtrar el ruido de la señal del punto 1. #
#Use la gráfica de la transformada de fourier del punto 3 para determinar un valor apropiado de la frecuencia de corte que debe usar para filtrar dicho ruido de alta frecuencia.



# 4) Grafique la señal filtrada



#EJERCICIO 3

# 1) Almacene los datos de violin.wav (use wav.read('violin.wav')).
#Grafique su señal en función del tiempo y guarde dicha gráfica.



# 2) Use fftfreq (BONO si usa su implementación propia) y haga una gráfica de su transformada de fourier en función de las frecuencias.



# 3) Haga un filtro que elimine el pico principal. Grafique su señal filtrada.
#Escuche (OJO con el volumen!) sus datos filtrados.
#Repita lo anterior haciendo un filtro pasaaltos y uno pasabajos.



#NOTA: para el manejo de archivos .wav mire la documentacion de python de input-output en https://docs.scipy.org/doc/scipy-0.14.0/reference/io.html)

# 4) repita lo anterior para trumpet.wav que es la señal correspondiente al sonido
#de una trompeta tocando la misma nota que el violín del puntos anterior.



#Mire en la transformada de Fourier cuáles son las diferencias entre la señal del violin y de la trompeta.
# Qué hace que siendo la misma nota (misma frecuencia)el tiembre del violin de la trompeta sean tan diferentes...

