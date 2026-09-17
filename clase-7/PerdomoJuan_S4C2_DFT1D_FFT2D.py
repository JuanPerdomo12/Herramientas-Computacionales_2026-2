#EJERCICIO 1

import numpy as np
import matplotlib.pylab as plt
from scipy.fftpack import fft, fftfreq, ifft, fft2, ifft2, fftshift

# Construcción de la señal
N = 128 # number of point in the whole interval
f = 200.0 #  frequency in Hz
dt = 1 / (f * 32 ) #32 samples per unit frequency
t = np.linspace( 0, (N-1)*dt, N)
y = np.cos(2 * np.pi * f * t) - 0.4 * np.sin(2 * np.pi * (2*f) * t )+ 0.17*np.sin(2 * np.pi * (15*f) * t )

# 1) implemente de la transformada de fourier discreta

def fourier_transform(f, N):
    X_k = np.zeros(N, dtype = complex)
    n = np.arange(N)

    for k in range(N):
        X_k[k] = np.sum(f * np.exp(-1*1j*2*np.pi*k*n/N))

    X_k_order = np.concatenate((X_k[N//2:], X_k[:N//2]))
    return X_k_order

Y_k = fourier_transform(y, N)
Y_k = Y_k/np.max(Y_k)

# 2) Genere el arreglo de las frecuencias (ver documentación de fftfreq):

def fourier_freqs(N, dt):
    freq_pos = np.arange(0, N//2)/(N*dt)
    freq_neg = np.arange(-N//2, 0)/(N*dt)
    freqs = np.concatenate((freq_neg, freq_pos))
    return freqs

freq_y = fourier_freqs(N, dt)

# 3) Haga una gráfica comparando método propio con implementación de scipy.fftpack.fft

fft_x = fft(y) / N # FFT Normalized
freq = fftfreq(N, dt) # Recuperamos las frecuencias

plt.plot(freq, np.abs(fft_x))
plt.plot(freq_y, np.abs(Y_k))
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

Sig_k = fourier_transform(signal, len(signal))

dt_sig = time[1]-time[0]

freq_sig = fourier_freqs(len(signal), dt_sig)

plt.plot(freq_sig, np.abs(Sig_k))
plt.show()

# 3) Haga un filtro pasa bajos que le permita filtrar el ruido de la señal del punto 1. #
#Use la gráfica de la transformada de fourier del punto 3 para determinar un valor apropiado de la frecuencia de corte que debe usar para filtrar dicho ruido de alta frecuencia.

def filter_lowfreqs(size, freqs, X_k, cutoff):
    for i in range(size):
        if np.abs(freqs[i]) > cutoff:
            X_k[i] = 0
    return X_k

Sig_k_filter = filter_lowfreqs(len(signal), freq_sig, Sig_k, 500)

# 4) Grafique la señal filtrada

def inverse_fourier_transform(f, N):
    f_normal = np.concatenate((f[N//2:], f[:N//2]))

    x_n = np.zeros(N, dtype = complex)
    k = np.arange(N)

    for n in range(N):
        x_n[n] = 1/N*np.sum(f_normal * np.exp(1j*2*np.pi*k*n/N))

    return np.real(x_n)

Sig_n_filter = inverse_fourier_transform(Sig_k_filter, len(signal))

plt.plot(time, Sig_n_filter)
plt.show()

#EJERCICIO 3

# 1) Almacene los datos de violin.wav (use wav.read('violin.wav')).
#Grafique su señal en función del tiempo y guarde dicha gráfica.

from scipy.io import wavfile as wav

violin_rate, violin_data = wav.read('violin.wav')

dt_violin = 1/violin_rate
N_violin = len(violin_data)

time_violin = np.linspace(0, (N_violin-1)*dt_violin, N_violin)

plt.figure(figsize=(10, 4), dpi=120)
plt.plot(time_violin, violin_data)
plt.title('Señal del Violín')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.savefig('violin_signal.png')
plt.show()

# 2) Use fftfreq (BONO si usa su implementación propia) y haga una gráfica de su transformada de fourier en función de las frecuencias.

fft_violin = fft(violin_data) / N_violin
freq_violin = fftfreq(N_violin, dt_violin)

plt.figure(figsize=(10, 4), dpi=120)
plt.plot(freq_violin, np.abs(fft_violin))
plt.title("Transformada de Fourier - Violín")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud")
plt.savefig('violin_fft.png')
plt.show()

# 3) Haga un filtro que elimine el pico principal. Grafique su señal filtrada.
#Escuche (OJO con el volumen!) sus datos filtrados.
#Repita lo anterior haciendo un filtro pasaaltos y uno pasabajos.

freq_pico_violin = np.abs(freq_violin[np.argmax(np.abs(fft_violin))])
bw_violin = 20.0

fft_filtro_pico_violin = fft_violin.copy()
fft_filtro_pico_violin[np.abs(np.abs(freq_violin) - freq_pico_violin) < bw_violin] = 0

violin_filtro_pico = np.real(ifft(fft_filtro_pico_violin * N_violin))
wav.write('violin_filtro_pico.wav', violin_rate, np.int16(violin_filtro_pico))

cutoff_highfreqs_violin = 1000.0
fft_highfreqs_violin = fft_violin.copy()
fft_highfreqs_violin[np.abs(freq_violin) < cutoff_highfreqs_violin] = 0

violin_highfreqs = np.real(ifft(fft_highfreqs_violin * N_violin))
wav.write('violin_highfreqs.wav', violin_rate, np.int16(violin_highfreqs))

cutoff_lowfreqs_violin = 1000.0
fft_lowfreqs_violin = fft_violin.copy()
fft_lowfreqs_violin[np.abs(freq_violin) > cutoff_lowfreqs_violin] = 0

violin_lowfreqs = np.real(ifft(fft_lowfreqs_violin * N_violin))
wav.write('violin_lowfreqs.wav', violin_rate, np.int16(violin_lowfreqs))

plt.figure(figsize=(12, 8), dpi=120)
plt.subplot(3, 1, 1)
plt.plot(time_violin, violin_filtro_pico)
plt.title('Señal Filtrada - Sin Pico Principal')

plt.subplot(3, 1, 2)
plt.plot(time_violin, violin_highfreqs)
plt.title('Señal Filtrada - Pasaaltos (> 1000 Hz)')

plt.subplot(3, 1, 3)
plt.plot(time_violin, violin_lowfreqs)
plt.title('Señal Filtrada - Pasabajos (< 1000 Hz)')

plt.tight_layout()
plt.savefig('violin_filters.png')
plt.show()

#NOTA: para el manejo de archivos .wav mire la documentacion de python de input-output en https://docs.scipy.org/doc/scipy-0.14.0/reference/io.html)

# 4) repita lo anterior para trumpet.wav que es la señal correspondiente al sonido de una trompeta tocando la misma nota que el violín del puntos anterior.

trumpet_rate, trumpet_data = wav.read('trumpet.wav')

dt_trumpet = 1/trumpet_rate
N_trumpet = len(trumpet_data)

time_trumpet = np.linspace(0, (N_trumpet-1)*dt_trumpet, N_trumpet)

plt.figure(figsize=(10, 4), dpi=120)
plt.plot(time_trumpet, trumpet_data)
plt.title('Señal de la Trompeta')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.savefig('trumpet_signal.png')
plt.show()

fft_trumpet = fft(trumpet_data) / N_trumpet
freq_trumpet = fftfreq(N_trumpet, dt_trumpet)

plt.figure(figsize=(10, 4), dpi=120)
plt.plot(freq_trumpet, np.abs(fft_trumpet))
plt.title("Transformada de Fourier - Trompeta")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud")
plt.savefig('trumpet_fft.png')
plt.show()

freq_pico_trumpet = np.abs(freq_trumpet[np.argmax(np.abs(fft_trumpet))])
bw_trumpet = 20.0

fft_filtro_pico_trumpet = fft_trumpet.copy()
fft_filtro_pico_trumpet[np.abs(np.abs(freq_trumpet) - freq_pico_trumpet) < bw_trumpet] = 0

trumpet_filtro_pico = np.real(ifft(fft_filtro_pico_trumpet * N_trumpet))
wav.write('trumpet_filtro_pico.wav', trumpet_rate, np.int16(trumpet_filtro_pico))

cutoff_highfreqs_trumpet = 1000.0
fft_highfreqs_trumpet = fft_trumpet.copy()
fft_highfreqs_trumpet[np.abs(freq_trumpet) < cutoff_highfreqs_trumpet] = 0

trumpet_highfreqs = np.real(ifft(fft_highfreqs_trumpet * N_trumpet))
wav.write('trumpet_highfreqs.wav', trumpet_rate, np.int16(trumpet_highfreqs))

cutoff_lowfreqs_trumpet = 1000.0
fft_lowfreqs_trumpet = fft_trumpet.copy()
fft_lowfreqs_trumpet[np.abs(freq_trumpet) > cutoff_lowfreqs_trumpet] = 0

trumpet_lowfreqs = np.real(ifft(fft_lowfreqs_trumpet * N_trumpet))
wav.write('trumpet_lowfreqs.wav', trumpet_rate, np.int16(trumpet_lowfreqs))

plt.figure(figsize=(12, 8), dpi=120)
plt.subplot(3, 1, 1)
plt.plot(time_trumpet, trumpet_filtro_pico)
plt.title('Señal Filtrada - Sin Pico Principal')

plt.subplot(3, 1, 2)
plt.plot(time_trumpet, trumpet_highfreqs)
plt.title('Señal Filtrada - Pasaaltos (> 1000 Hz)')

plt.subplot(3, 1, 3)
plt.plot(time_trumpet, trumpet_lowfreqs)
plt.title('Señal Filtrada - Pasabajos (< 1000 Hz)')

plt.tight_layout()
plt.savefig('trumpet_filters.png')
plt.show()

#EJERCICIO 4

# 1) Almacene los datos de la imagen (use imread: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imread.html)

from matplotlib.pyplot import imread, imshow

moon_data = imread('moon.jpg', )
moon_size = np.shape(moon_data)
N = moon_size[0]
M = moon_size[1]
d1, d2 = 1.0, 1.0

moon_image = imshow(moon_data)
plt.show()

# 2) Use la librería de scipy de transformada de fourier en 2d y la trasnformada inversa
#(https://docs.scipy.org/doc/scipy/reference/generated/scipy.fft.fft2.html)
#para hacer un código que filtre el ruido periodico que tiene la imagen de la luna.

moon_fft = fft2(moon_data)
moon_freqs_x = fftfreq(M, d=d1)
moon_freqs_y = fftfreq(N, d=d2)
moon_fft_organized = fftshift(moon_fft)

freq_ruido_moon = np.abs(moon_freqs_x[np.argmax(np.abs(moon_fft))])
bw_moon = 20
fft_filtro_ruido_moon = moon_fft_organized.copy()
fft_filtro_ruido_moon[np.abs(np.abs(moon_freqs_x) - freq_ruido_moon) < bw_moon] = 0

moon_filtro_ruido = np.real(ifft2(fft_filtro_ruido_moon * moon_size))

#3) haga una gráfica de la imagen filtrada y guárdela en LunaFiltrada.png

moon_image_filter = imshow(moon_filtro_ruido)
plt.show()

#imagen: https://blogs.3ds.com/simulia/wp-content/uploads/sites/18/2019/07/NASA_Moon.jpg

#EJERCICIO 5

#Recupere la imagen original a partir de la fase y la amplitud de la transformada de fourier (archivos amplitude.dat y phase.dat).
#Recuerde que la transformada de fourier tiene una parte real y una imaginaria
#y recuerde tambien que un numero complejo se puede escribir a partir de la fase y la magnitud que son los datos que usted tiene
#(http://webpages.ursinus.edu/lriley/ref/complex/node1.html)


#1)Descargue los datos de fase y magnitud



#2) construya la transformada de fourier



#3) Obtenga la imagen haciendo la transformada inversa
