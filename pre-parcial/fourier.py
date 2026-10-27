import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('signalP.csv', header=None)
tiempo = data.iloc[:, 0].values
amplitud = data.iloc[:, 1].values

dt = tiempo[1] - tiempo[0]
N = len(tiempo)

fft_signal = np.fft.fft(amplitud)
frecuencias = np.fft.fftfreq(N, d=dt)

masca_pasabandas = (np.abs(frecuencias) >= 500) & (np.abs(frecuencias) <= 1000)

fft_filtrada = fft_signal.copy()
fft_filtrada[~masca_pasabandas] = 0

senal_filtrada = np.fft.ifft(fft_filtrada).real

plt.figure(figsize=(12, 6))

plt.plot(tiempo, amplitud, label='Señal Original', alpha=0.6, color='blue')
plt.plot(tiempo, senal_filtrada, label='Señal Filtrada (500Hz - 1000Hz)', color='red', linewidth=1.5)

plt.title('Filtrado Pasabandas de la Señal FFT')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')
plt.legend()
plt.grid(True)
plt.savefig('filtro.png', dpi=300)
plt.close()