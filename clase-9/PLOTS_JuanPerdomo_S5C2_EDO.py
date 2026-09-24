import matplotlib.pyplot as plt
import numpy as np

euler_01 = np.loadtxt("EDO_euler_0.01.txt")
t_euler_01 = euler_01[:,0]
y_euler_01 = euler_01[:,1]

euler_001 = np.loadtxt("EDO_euler_0.001.txt")
t_euler_001 = euler_001[:,0]
y_euler_001 = euler_001[:,1]

rk4_01 = np.loadtxt("EDO_rk4_0.01.txt")
t_rk4_01 =rk4_01[:,0]
y_rk4_01 = rk4_01[:,1]

rk4_001 = np.loadtxt("EDO_rk4_0.001.txt")
t_rk4_001 =rk4_001[:,0]
y_rk4_001 = rk4_001[:,1]

t = np.linspace(0.0, 2.0, 1000)

fig, ax = plt.subplots(figsize=(8, 6), dpi=120)

ax.plot(
    t,
    np.exp(-t),
    label="Curva Analitica",
    color="#030303",
    linestyle="-",
    linewidth=1,
    marker="*",
    markevery=5,
    markersize=4,
)

ax.plot(
    t_euler_01,
    y_euler_01,
    label="Metodo de Euler con h = 0.01",
    color="#1f77b4",
    linestyle="-",
    linewidth=1,
    marker="o",
    markevery=5,
    markersize=3,
)

ax.plot(
    t_euler_001,
    y_euler_001,
    label="Metodo de Euler con h = 0.001",
    color="#1fb43a",
    linestyle="-",
    linewidth=1,
    marker="^",
    markevery=10,
    markersize=3,
)

ax.plot(
    t_rk4_01,
    y_rk4_01,
    label="Metodo de Runge-Kutta con h = 0.01",
    color="#c93513",
    linestyle="-",
    linewidth=1,
    marker="s",
    markevery=5,
    markersize=3,
)

ax.plot(
    t_rk4_001,
    y_rk4_001,
    label="Metodo de Runge-Kutta con h = 0.001",
    color="#a81fb4",
    linestyle="-",
    linewidth=1,
    marker="v",
    markevery=10,
    markersize=3,
)

ax.minorticks_on()

ax.tick_params(
    axis="both",
    which="both", 
    direction="in", 
    top=True,
    bottom=True, 
    left=True, 
    right=True, 
)

ax.tick_params(axis="both", which="major", length=7, width=1.2, labelsize=11)
ax.tick_params(axis="both", which="minor", length=3, width=0.8)

ax.set_xlabel("t", fontsize=13, fontweight="medium")
ax.set_ylabel("y", fontsize=13, fontweight="medium")

ax.legend(
    loc="upper right",
    fontsize=10,
    frameon=True, 
    edgecolor="black", 
    facecolor="white", 
)

ax.grid(True, which="major", linestyle=":", alpha=0.6)

plt.tight_layout()
plt.savefig("plot_edo.png")
plt.show()
