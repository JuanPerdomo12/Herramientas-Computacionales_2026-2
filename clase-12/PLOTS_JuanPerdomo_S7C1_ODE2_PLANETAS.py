import matplotlib.pyplot as plt
import numpy as np

#1 cuerpo

euler_05_1 = np.loadtxt("EDO2_planetas_1cuerpos_euler_0.5.txt")
t_euler_05_1 = euler_05_1[:,0]
x_euler_05_1 = euler_05_1[:,1]
y_euler_05_1 = euler_05_1[:,2]
vx_euler_05_1 = euler_05_1[:,3]
vy_euler_05_1 = euler_05_1[:,4]

euler_1_1 = np.loadtxt("EDO2_planetas_1cuerpos_euler_1.txt")
t_euler_1_1 = euler_1_1[:,0]
x_euler_1_1 = euler_1_1[:,1]
y_euler_1_1 = euler_1_1[:,2]
vx_euler_1_1 = euler_1_1[:,3]
vy_euler_1_1 = euler_1_1[:,4]

lf_05_1 = np.loadtxt("EDO2_planetas_1cuerpos_lf_0.5.txt")
t_lf_05_1 = lf_05_1[:,0]
x_lf_05_1 = lf_05_1[:,1]
y_lf_05_1 = lf_05_1[:,2]
vx_lf_05_1 = lf_05_1[:,3]
vy_lf_05_1 = lf_05_1[:,4]

lf_1_1 = np.loadtxt("EDO2_planetas_1cuerpos_lf_1.txt")
t_lf_1_1 = lf_1_1[:,0]
x_lf_1_1 = lf_1_1[:,1]
y_lf_1_1 = lf_1_1[:,2]
vx_lf_1_1 = lf_1_1[:,3]
vy_lf_1_1 = lf_1_1[:,4]

#2 cuerpos

euler_05_2 = np.loadtxt("EDO2_planetas_2cuerpos_euler_0.5.txt")
t_euler_05_2 = euler_05_2[:,0]
x_S_euler_05_2 = euler_05_2[:,1]
y_S_euler_05_2 = euler_05_2[:,2]
x_T_euler_05_2 = euler_05_2[:,3]
y_T_euler_05_2 = euler_05_2[:,4]
vx_S_euler_05_2 = euler_05_2[:,5]
vy_S_euler_05_2 = euler_05_2[:,6]
vx_T_euler_05_2 = euler_05_2[:,7]
vy_T_euler_05_2 = euler_05_2[:,8]

euler_1_2 = np.loadtxt("EDO2_planetas_2cuerpos_euler_1.txt")
t_euler_1_2 = euler_1_2[:,0]
x_S_euler_1_2 = euler_1_2[:,1]
y_S_euler_1_2 = euler_1_2[:,2]
x_T_euler_1_2 = euler_1_2[:,3]
y_T_euler_1_2 = euler_1_2[:,4]
vx_S_euler_1_2 = euler_1_2[:,5]
vy_S_euler_1_2 = euler_1_2[:,6]
vx_T_euler_1_2 = euler_1_2[:,7]
vy_T_euler_1_2 = euler_1_2[:,8]

lf_05_2 = np.loadtxt("EDO2_planetas_2cuerpos_lf_0.5.txt")
t_lf_05_2 = lf_05_2[:,0]
x_S_lf_05_2 = lf_05_2[:,1]
y_S_lf_05_2 = lf_05_2[:,2]
x_T_lf_05_2 = lf_05_2[:,3]
y_T_lf_05_2 = lf_05_2[:,4]
vx_S_lf_05_2 = lf_05_2[:,5]
vy_S_lf_05_2 = lf_05_2[:,6]
vx_T_lf_05_2 = lf_05_2[:,7]
vy_T_lf_05_2 = lf_05_2[:,8]

lf_1_2 = np.loadtxt("EDO2_planetas_2cuerpos_lf_1.txt")
t_lf_1_2 = lf_1_2[:,0]
x_S_lf_1_2 = lf_1_2[:,1]
y_S_lf_1_2 = lf_1_2[:,2]
x_T_lf_1_2 = lf_1_2[:,3]
y_T_lf_1_2 = lf_1_2[:,4]
vx_S_lf_1_2 = lf_1_2[:,5]
vy_S_lf_1_2 = lf_1_2[:,6]
vx_T_lf_1_2 = lf_1_2[:,7]
vy_T_lf_1_2 = lf_1_2[:,8]

#N cuerpos

euler_05_9 = np.loadtxt("EDO2_planetas_9cuerpos_euler_0.5.txt")

euler_1_9 = np.loadtxt("EDO2_planetas_9cuerpos_euler_1.txt")

lf_05_9 = np.loadtxt("EDO2_planetas_9cuerpos_lf_0.5.txt")

lf_1_9 = np.loadtxt("EDO2_planetas_9cuerpos_lf_1.txt")

#datos observacionales

a = 1.00000011
e = 0.01671022

theta = np.linspace(0, 2*np.pi, 1000)
r_obs = (a*(1-e**2))/(1+e*np.cos(theta))

x_obs = r_obs*np.cos(theta)
y_obs = r_obs*np.sin(theta)

t = np.linspace(0.0, 365.0, 1000)

fig, ax = plt.subplots(figsize=(8, 6), dpi=120)

ax.plot(
    x_obs,
    y_obs,
    label="Datos Observacionales (NASA)",
    color="black",
    linestyle="--", 
    linewidth=1,
    marker="s",
    markevery=1,
    markersize=3,
)

ax.plot(
    x_euler_05_1,
    y_euler_05_1,
    label="Metodo de Euler con h = 0.5",
    color="#1f77b4",
    linestyle="-",
    linewidth=1,
    marker="o",
    markevery=1,
    markersize=3,
)

ax.plot(
    x_euler_1_1,
    y_euler_1_1,
    label="Metodo de Euler con h = 1",
    color="#0b7e20",
    linestyle="-",
    linewidth=1,
    marker="^",
    markevery=1,
    markersize=3,
)

ax.plot(
    x_lf_05_1,
    y_lf_05_1,
    label="Metodo de Leap-Frog con h = 0.5",
    color="#d4db16",
    linestyle="-",
    linewidth=1,
    marker="<",
    markevery=1,
    markersize=3,
)

ax.plot(
    x_lf_1_1,
    y_lf_1_1,
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

fig, ax = plt.subplots(figsize=(8, 6), dpi=120)

ax.plot(
    x_obs,
    y_obs,
    label="Datos Observacionales (NASA)",
    color="black",
    linestyle="--", 
    linewidth=1,
    marker="s",
    markevery=1,
    markersize=3,
)

ax.plot(
    x_S_euler_05_2,
    y_S_euler_05_2,
    label="Metodo de Euler con h = 0.5 (Sol)",
    color="#1f77b4",
    linestyle="-",
    linewidth=1,
    marker="o",
    markevery=1,
    markersize=3,
)

ax.plot(
    x_S_euler_1_2,
    y_S_euler_1_2,
    label="Metodo de Euler con h = 1 (Sol)",
    color="#0b7e20",
    linestyle="-",
    linewidth=1,
    marker="^",
    markevery=1,
    markersize=3,
)

ax.plot(
    x_S_lf_05_2,
    y_S_lf_05_2,
    label="Metodo de Leap-Frog con h = 0.5 (Sol)",
    color="#d4db16",
    linestyle="-",
    linewidth=1,
    marker="<",
    markevery=1,
    markersize=3,
)

ax.plot(
    x_S_lf_1_2,
    y_S_lf_1_2,
    label="Metodo de Leap-Frog con h = 1 (Sol)",
    color="#ae00ff",
    linestyle="-",
    linewidth=1,
    marker=">",
    markevery=1,
    markersize=3,
)

ax.plot(
    x_T_euler_05_2,
    y_T_euler_05_2,
    label="Metodo de Euler con h = 0.5 (Tierra)",
    color="#ff7f0e",
    linestyle="-",
    linewidth=1,
    marker="o",
    markevery=1,
    markersize=3,
)

ax.plot(
    x_T_euler_1_2,
    y_T_euler_1_2,
    label="Metodo de Euler con h = 1 (Tierra)",
    color="#e377c2",
    linestyle="-",
    linewidth=1,
    marker="^",
    markevery=1,
    markersize=3,
)

ax.plot(
    x_T_lf_05_2,
    y_T_lf_05_2,
    label="Metodo de Leap-Frog con h = 0.5 (Tierra)",
    color="#17becf",
    linestyle="-",
    linewidth=1,
    marker="<",
    markevery=1,
    markersize=3,
)

ax.plot(
    x_T_lf_1_2,
    y_T_lf_1_2,
    label="Metodo de Leap-Frog con h = 1 (Tierra)",
    color="#bcbd22",
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

plt.title("Solucion Problema de Dos Cuerpos (Tierra y Sol)", fontsize=15, fontweight="medium")
plt.tight_layout()
plt.savefig("plot_edo2_planetas_2_cuerpos.png")
plt.show()


data_nasa = {
    "Mercurio": {"a": 0.387098, "e": 0.205630, "color": "gray"},
    "Venus":    {"a": 0.723332, "e": 0.006772, "color": "goldenrod"},
    "Tierra":   {"a": 1.000000, "e": 0.016710, "color": "black"},
    "Marte":    {"a": 1.523679, "e": 0.093401, "color": "red"},
    "Júpiter":  {"a": 5.204267, "e": 0.048498, "color": "orange"},
    "Saturno":  {"a": 9.537207, "e": 0.055550, "color": "khaki"},
    "Urano":    {"a": 19.19126, "e": 0.046296, "color": "lightskyblue"},
    "Neptuno":  {"a": 30.06896, "e": 0.008988, "color": "mediumblue"}
}

theta = np.linspace(0, 2 * np.pi, 1000)

orbitas_obs = {}
for name, planet in data_nasa.items():
    a = planet["a"]
    e = planet["e"]

    r_obs = (a * (1 - e**2)) / (1 + e * np.cos(theta))
    x_obs = r_obs * np.cos(theta)
    y_obs = r_obs * np.sin(theta)
    orbitas_obs[name] = (x_obs, y_obs)

fig, ax = plt.subplots(figsize=(8, 6), dpi=120)

for i, (name, (x_o, y_o)) in enumerate(orbitas_obs.items()):
    color_obs = data_nasa[name]["color"]

    lbl_obs = "Órbitas Observacionales (NASA)" if i == 0 else None
    ax.plot(
        x_o, y_o,
        label=lbl_obs,
        color=color_obs,
        linestyle="--",
        linewidth=1.2,
        alpha=0.8
    )

sims = [
    (euler_05_9, "Euler h = 0.5", "#1f77b4", "o"),
    (euler_1_9,  "Euler h = 1.0", "#0b7e20", "^"),
    (lf_05_9,    "Leap-Frog h = 0.5", "#db1616", "<"),
    (lf_1_9,     "Leap-Frog h = 1.0", "#ae00ff", ">")
]

for sim_data, method_label, color, marker in sims:
    for i in range(9):
        x_idx = 1+2*i
        y_idx = 2+2*i
        
        lbl = f"{method_label}" if i == 0 else None
        
        ax.plot(
            sim_data[:, x_idx],
            sim_data[:, y_idx],
            label=lbl,
            color=color,
            linestyle="-",
            linewidth=1,
            marker=marker,
            markevery=20,
            markersize=3
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

ax.set_xlabel("x [UA]", fontsize=13, fontweight="medium")
ax.set_ylabel("y [UA]", fontsize=13, fontweight="medium")

ax.legend(
    loc="upper right",
    fontsize=10,
    frameon=True, 
    edgecolor="black", 
    facecolor="white", 
)

ax.grid(True, which="major", linestyle=":", alpha=0.6)

plt.title("Orbitas del Sistema Solar (9 Cuerpos)", fontsize=15, fontweight="medium")
plt.tight_layout()
plt.savefig("plot_edo2_orbitas_9_planetas_.png")
plt.show()

import matplotlib.animation as animation

#animacion 1 cuerpo

x_tierra = x_lf_05_1
y_tierra = y_lf_05_1

step = 2
x_anim = x_tierra[::step]
y_anim = y_tierra[::step]

fig_anim1, ax_anim1 = plt.subplots(figsize=(7, 7), dpi=100)

ax_anim1.plot(0, 0, 'o', color='gold', markersize=12, label='Sol')

linea_trayectoria, = ax_anim1.plot([], [], '-', color='#1f77b4', lw=1.5, label='Órbita Tierra')
punto_tierra, = ax_anim1.plot([], [], 'o', color='#1f77b4', markersize=8)

ax_anim1.set_xlim(-1.2, 1.2)
ax_anim1.set_ylim(-1.2, 1.2)
ax_anim1.set_aspect('equal')
ax_anim1.set_xlabel("x [UA]", fontsize=12)
ax_anim1.set_ylabel("y [UA]", fontsize=12)
ax_anim1.set_title("Órbita de la Tierra (Sol Estático)", fontsize=13)
ax_anim1.grid(True, linestyle=":", alpha=0.6)
ax_anim1.legend(loc="upper right")

def init_anim1():
    linea_trayectoria.set_data([], [])
    punto_tierra.set_data([], [])
    return linea_trayectoria, punto_tierra

def update_anim1(frame):
    linea_trayectoria.set_data(x_anim[:frame], y_anim[:frame])
    punto_tierra.set_data([x_anim[frame]], [y_anim[frame]])
    return linea_trayectoria, punto_tierra

anim1 = animation.FuncAnimation(
    fig_anim1,
    update_anim1,
    frames=len(x_anim),
    init_func=init_anim1,
    interval=20,
    blit=True
)

anim1.save("orbita_Tierra_Sol_estatico.gif", writer="pillow", fps=30)
plt.show()

#animacion 2 cuerpos

x_S_anim = x_S_lf_05_2[::step]
y_S_anim = y_S_lf_05_2[::step]
x_T_anim = x_T_lf_05_2[::step]
y_T_anim = y_T_lf_05_2[::step]

fig_anim2, ax_anim2 = plt.subplots(figsize=(7, 7), dpi=100)

line_S, = ax_anim2.plot([], [], '-', color='orange', lw=1, alpha=0.7)
line_T, = ax_anim2.plot([], [], '-', color='blue', lw=1.5, label='Trayectoria Tierra')
point_S, = ax_anim2.plot([], [], 'o', color='gold', markersize=10, label='Sol')
point_T, = ax_anim2.plot([], [], 'o', color='dodgerblue', markersize=6, label='Tierra')

ax_anim2.set_xlim(-1.2, 1.2)
ax_anim2.set_ylim(-1.2, 1.2)
ax_anim2.set_aspect('equal')
ax_anim2.set_xlabel("x [UA]", fontsize=12)
ax_anim2.set_ylabel("y [UA]", fontsize=12)
ax_anim2.set_title("Problema de Dos Cuerpos (Sol y Tierra)", fontsize=13)
ax_anim2.grid(True, linestyle=":", alpha=0.6)
ax_anim2.legend(loc="upper right")

def init_anim2():
    line_S.set_data([], [])
    line_T.set_data([], [])
    point_S.set_data([], [])
    point_T.set_data([], [])
    return line_S, line_T, point_S, point_T

def update_anim2(frame):
    line_S.set_data(x_S_anim[:frame], y_S_anim[:frame])
    line_T.set_data(x_T_anim[:frame], y_T_anim[:frame])
    point_S.set_data([x_S_anim[frame]], [y_S_anim[frame]])
    point_T.set_data([x_T_anim[frame]], [y_T_anim[frame]])
    return line_S, line_T, point_S, point_T

anim2 = animation.FuncAnimation(
    fig_anim2,
    update_anim2,
    frames=len(x_T_anim),
    init_func=init_anim2,
    interval=20,
    blit=True
)

anim2.save("orbita_dos_cuerpos.gif", writer="pillow", fps=30)
plt.show()

#animacion 9 cuerpo

data_9 = lf_05_9
step_9 = 5
names = ["Sol", "Mercurio", "Venus", "Tierra", "Marte", "Júpiter", "Saturno", "Urano", "Neptuno"]

fig_anim9, ax_anim9 = plt.subplots(figsize=(8, 8), dpi=100)

colores_planetas = [
    'gold',
    'gray',
    'goldenrod',
    'dodgerblue',
    'red',
    'orange',
    'khaki',
    'lightskyblue',
    'mediumblue'
]

lineas_trayectoria = []
puntos_cuerpos = []

for i in range(9):
    linea, = ax_anim9.plot([], [], '-', color=colores_planetas[i], lw=0.8, alpha=0.6)
    punto, = ax_anim9.plot([], [], 'o', color=colores_planetas[i], markersize=6 if i > 0 else 10, label=names[i])
    lineas_trayectoria.append(linea)
    puntos_cuerpos.append(punto)

ax_anim9.set_xlim(-32, 32)
ax_anim9.set_ylim(-32, 32)
ax_anim9.set_aspect('equal')
ax_anim9.set_xlabel("x [UA]", fontsize=12)
ax_anim9.set_ylabel("y [UA]", fontsize=12)
ax_anim9.set_title("Simulación del Sistema Solar (9 Cuerpos)", fontsize=13)
ax_anim9.grid(True, linestyle=":", alpha=0.6)
ax_anim9.legend(loc="upper right", bbox_to_anchor=(1.25, 1.0))

def init_anim9():
    for linea, punto in zip(lineas_trayectoria, puntos_cuerpos):
        linea.set_data([], [])
        punto.set_data([], [])
    return lineas_trayectoria + puntos_cuerpos

def update_anim9(frame):
    f = frame * step_9
    for i in range(9):
        x_cuerpo = data_9[:f, 1 + 2 * i]
        y_cuerpo = data_9[:f, 2 + 2 * i]
        
        lineas_trayectoria[i].set_data(x_cuerpo, y_cuerpo)
        if f < len(data_9):
            puntos_cuerpos[i].set_data([data_9[f, 1 + 2 * i]], [data_9[f, 2 + 2 * i]])
            
    return lineas_trayectoria + puntos_cuerpos

n_frames = len(data_9) // step_9

anim9 = animation.FuncAnimation(
    fig_anim9,
    update_anim9,
    frames=n_frames,
    init_func=init_anim9,
    interval=20,
    blit=True
)

anim9.save("orbita_9_cuerpos_sistema_solar.gif", writer="pillow", fps=30)
plt.tight_layout()
plt.show()