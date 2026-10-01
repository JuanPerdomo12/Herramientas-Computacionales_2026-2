import matplotlib.pyplot as plt
import numpy as np

euler_05 = np.loadtxt("EDO2_planetas_euler_0.5.txt")
t_euler_05 = euler_05[:,0]
x_euler_05 = euler_05[:,1]
y_euler_05 = euler_05[:,2]
vx_euler_05 = euler_05[:,3]
vy_euler_05 = euler_05[:,4]

euler_1 = np.loadtxt("EDO2_planetas_euler_1.txt")
t_euler_1 = euler_1[:,0]
x_euler_1 = euler_1[:,1]
y_euler_1 = euler_1[:,2]
vx_euler_1 = euler_1[:,3]
vy_euler_1 = euler_1[:,4]

lf_05 = np.loadtxt("EDO2_planetas_lf_0.5.txt")
t_lf_05 = lf_05[:,0]
x_lf_05 = lf_05[:,1]
y_lf_05 = lf_05[:,2]
vx_lf_05 = lf_05[:,3]
vy_lf_05 = lf_05[:,4]

lf_1 = np.loadtxt("EDO2_planetas_lf_1.txt")
t_lf_1 = lf_1[:,0]
x_lf_1 = lf_1[:,1]
y_lf_1 = lf_1[:,2]
vx_lf_1 = lf_1[:,3]
vy_lf_1 = lf_1[:,4]

t = np.linspace(0.0, 365.0, 1000)

fig, ax = plt.subplots(figsize=(8, 6), dpi=120)
"""
ax.plot(
    t,
    0.1*np.cos(np.sqrt(50.0/0.2)*t),
    label="Curva Analitica",
    color="#030303",
    linestyle="-",
    linewidth=1,
    marker="*",
    markevery=5,
    markersize=4,
)
"""
ax.plot(
    x_euler_05,
    y_euler_05,
    label="Metodo de Euler con h = 0.5",
    color="#1f77b4",
    linestyle="-",
    linewidth=1,
    marker="o",
    markevery=1,
    markersize=3,
)

ax.plot(
    x_euler_1,
    y_euler_1,
    label="Metodo de Euler con h = 1",
    color="#0b7e20",
    linestyle="-",
    linewidth=1,
    marker="^",
    markevery=1,
    markersize=3,
)

ax.plot(
    x_lf_05,
    y_lf_05,
    label="Metodo de Leap-Frog con h = 0.5",
    color="#d4db16",
    linestyle="-",
    linewidth=1,
    marker="<",
    markevery=1,
    markersize=3,
)

ax.plot(
    x_lf_1,
    y_lf_1,
    label="Metodo de Leap-Frog con h = 1",
    color="#ae00ff",
    linestyle="-",
    linewidth=1,
    marker=">",
    markevery=1,
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

ax.set_xlabel("x", fontsize=13, fontweight="medium")
ax.set_ylabel("y", fontsize=13, fontweight="medium")

ax.legend(
    loc="upper right",
    fontsize=10,
    frameon=True, 
    edgecolor="black", 
    facecolor="white", 
)

ax.grid(True, which="major", linestyle=":", alpha=0.6)

plt.title("Orbita de la Tierra con el Sol Estatico", fontsize=15, fontweight="medium")
plt.tight_layout()
plt.savefig("plot_edo2_planetas_sol_estatico.png")
plt.show()
