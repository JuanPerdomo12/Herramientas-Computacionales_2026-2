import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

#cuerda estremos fijos

cuerda_fija_05 = np.loadtxt("EDP_cuerda_extremos_fijos_0.5.txt")

t_05 = cuerda_fija_05[:, 0]
u_05 = cuerda_fija_05[:, 1:]

x = np.linspace(0, 2, u_05.shape[1])
i_05_6_times = np.linspace(0, len(t_05) - 1, 6, dtype=int)
i_05_100_times = np.linspace(0, len(t_05) - 1, 100, dtype=int)

cuerda_fija_3 = np.loadtxt("EDP_cuerda_extremos_fijos_3.txt")

t_3 = cuerda_fija_3[:, 0]
u_3 = cuerda_fija_3[:, 1:]

i_3_6_times = np.linspace(0, len(t_3) - 1, 6, dtype=int)

cuerda_forzada_05 = np.loadtxt("EDP_cuerda_forzada_0.5.txt")

t_forzada_05 = cuerda_forzada_05[:, 0]
u_forzada_05 = cuerda_forzada_05[:, 1:]

i_forzada_05_6_times = np.linspace(0, len(t_forzada_05) - 1, 6, dtype=int)

fig, ax = plt.subplots(figsize=(9, 6), dpi=120)

colors = ["#e11212", "#f08c09", "#ebeb0e", "#0eed12", "#0dd5e7", "#1223df","#900bea"]

for i, idx in enumerate(i_05_6_times):
    time = t_05[idx]
    ax.plot(
        x,
        u_05[idx, :],
        label=f"t = {time:.4f} s",
        color=colors[i],
        linewidth=1.8
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

ax.set_xlabel("Posicion $x$ [m]", fontsize=13, fontweight="medium")
ax.set_ylabel("Desplazamiento $u(x,t)$ [m]", fontsize=13, fontweight="medium")

ax.legend(
    loc="upper right",
    fontsize=10,
    frameon=True, 
    edgecolor="black", 
    facecolor="white", 
)

ax.grid(True, which="major", linestyle=":", alpha=0.6)

plt.title("Evolucion de una Cuerda con Extremos Fijos en 6 Tiempos Diferentes ($dt = 0.5dx/c$)", fontsize=15, fontweight="medium")
plt.tight_layout()
plt.savefig("plot_edp_cuerda_extremos_fijos_6tiempos.png")
plt.show()

fig, ax = plt.subplots(figsize=(9, 6), dpi=120)

for i, idx in enumerate(i_05_100_times):
    time = t_05[idx]
    ax.plot(
        x,
        u_05[idx, :],
        color=colors[i % len(colors)],
        linewidth=1.8
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

ax.set_xlabel("Posicion $x$ [m]", fontsize=13, fontweight="medium")
ax.set_ylabel("Desplazamiento $u(x,t)$ [m]", fontsize=13, fontweight="medium")

ax.grid(True, which="major", linestyle=":", alpha=0.6)

plt.title("Evolucion de una Cuerda con Extremos Fijos en 100 Tiempos Diferentes ($dt = 0.5dx/c$)", fontsize=15, fontweight="medium")
plt.tight_layout()
plt.savefig("plot_edp_cuerda_extremos_fijos_100tiempos.png")
plt.show()

fig, ax= plt.subplots(figsize=(9, 6), dpi=120)

for i, idx in enumerate(i_3_6_times):
    time = t_3[idx]
    ax.plot(
        x,
        u_3[idx, :], 
        label=f"t = {time:.4f} s",
        color=colors[i % len(colors)],
        linewidth=1.8,
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

ax.set_xlabel("Posicion $x$ [m]", fontsize=13, fontweight="medium")
ax.set_ylabel("Desplazamiento $u(x,t)$ [m]", fontsize=13, fontweight="medium")

ax.legend(
    loc="upper right",
    fontsize=10,
    frameon=True, 
    edgecolor="black", 
    facecolor="white", 
)

ax.grid(True, which="major", linestyle=":", alpha=0.6)

plt.title("Evolucion de una Cuerda con Extremos Fijos en 6 Tiempos Diferentes ($dt = 3.0dx/c$)", fontsize=14)
plt.tight_layout()
plt.savefig("plot_edp_cuerda_extremos_fijos_inestable.png")
plt.show()

fig, ax = plt.subplots(figsize=(9, 6), dpi=120)

for i, idx in enumerate(i_forzada_05_6_times):
    time = t_forzada_05[idx]
    ax.plot(
        x,
        u_forzada_05[idx, :],
        label=f"t = {time:.4f} s",
        color=colors[i % len(colors)],
        linewidth=1.8
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

ax.set_xlabel("Posicion $x$ [m]", fontsize=13, fontweight="medium")
ax.set_ylabel("Desplazamiento $u(x,t)$ [m]", fontsize=13, fontweight="medium")

ax.legend(
    loc="upper right",
    fontsize=10,
    frameon=True, 
    edgecolor="black", 
    facecolor="white", 
)

ax.grid(True, which="major", linestyle=":", alpha=0.6)

plt.title("Evolucion de una Cuerda con Extremo Forzado en 6 Tiempos Diferentes ($dt = 0.5dx/c$)", fontsize=15, fontweight="medium")
plt.tight_layout()
plt.savefig("plot_edp_cuerda_forzada_6tiempos.png")
plt.show()

fig, ax = plt.subplots(figsize=(9, 6), dpi=120)

(line,) = ax.plot([], [], color="#1223df", linewidth=2.0, label="Cuerda")

ax.set_xlim(0, 2)

ax.set_ylim(np.min(u_forzada_05) * 1.2, np.max(u_forzada_05) * 1.2)

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

ax.set_xlabel("Posición $x$ [m]", fontsize=13, fontweight="medium")
ax.set_ylabel("Desplazamiento $u(x,t)$ [m]", fontsize=13, fontweight="medium")
ax.grid(True, which="major", linestyle=":", alpha=0.6)

time_text = ax.text(
    0.02,
    0.95,
    "",
    transform=ax.transAxes,
    fontsize=12,
    bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor="black", alpha=0.8),
)

plt.title("Evolución Temporal de la Cuerda Forzada ($dt = 0.5dx/c$)", fontsize=14, fontweight="medium")

def init():
    line.set_data([], [])
    time_text.set_text("")
    return line, time_text

def update(frame):
    idx = frame
    line.set_data(x, u_forzada_05[idx, :])
    time_text.set_text(f"Tiempo t = {t_forzada_05[idx]:.5f} s")
    return line, time_text

num_frames = len(t_forzada_05)
anim = FuncAnimation(
    fig, update, frames=num_frames, init_func=init, blit=True, interval=30
)

anim.save("animacion_cuerda_forzada.gif", writer="pillow", fps=30)
plt.tight_layout()
plt.show()