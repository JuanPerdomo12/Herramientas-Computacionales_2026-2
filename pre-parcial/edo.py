import numpy as np
import matplotlib.pyplot as plt

def f_x(t, x, v):
    return v

def f_v(t, x, v):
    return -4.0 * v - 13.0 * x

def sol_analitica(t):
    return np.exp(-2.0 * t) * (-np.cos(3.0 * t) - (1.0 / 3.0) * np.sin(3.0 * t))

t0 = 0.0
tf = 10.0
dt = 0.001

N = int((tf - t0) / dt) + 1
t = np.linspace(t0, tf, N)

x_euler = np.zeros(N)
v_euler = np.zeros(N)

x_euler[0] = -1.0
v_euler[0] = 1.0

for i in range(N - 1):
    x_euler[i + 1] = x_euler[i] + dt * f_x(t[i], x_euler[i], v_euler[i])
    v_euler[i + 1] = v_euler[i] + dt * f_v(t[i], x_euler[i], v_euler[i])

x_exacta = sol_analitica(t)

plt.figure(figsize=(10, 6))

plt.plot(t, x_exacta, label='Solución Analítica Exacta', color='black', linewidth=2)
plt.plot(t, x_euler, '--', label=f'Método de Euler (dt={dt})', color='crimson', linewidth=1.5)

plt.title('Solución EDO de 2do Orden: Método de Euler vs Analítica')
plt.xlabel('Tiempo (t)')
plt.ylabel('Posición x(t)')
plt.legend()
plt.grid(True)

plt.savefig('sol.png', dpi=300)
plt.close()