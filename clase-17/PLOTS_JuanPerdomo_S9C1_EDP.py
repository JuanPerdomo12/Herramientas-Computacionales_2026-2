import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

#difusion 2D

difusion_2d = np.loadtxt("EDP_difusion_2D_1.txt")

t = difusion_2d[:, 0]
T = difusion_2d[:, 1:]

L = 1.0
N = int(np.sqrt(T.shape[1]))
x = np.linspace(0, L, N)
y = np.linspace(0, L, N)
X, Y = np.meshgrid(x, y)

t_target = [0.0, 100.0, 300.0, 500.0]

fig, axes = plt.subplots(2, 2, figsize=(10, 8), dpi=120)
axes = axes.flatten()

for i, target in enumerate(t_target):
    idx = np.argmin(np.abs(t - target))
    time = t[idx]
    
    T_grid = T[idx, :].reshape((N, N))
    
    ax = axes[i]
    im = ax.imshow(
        T_grid.T, 
        origin="lower", 
        extent=[0, L, 0, L], 
        cmap="hot", 
        vmin=50, 
        vmax=100,
        interpolation="bicubic"
    )

    im.format_cursor_data = lambda data: ""

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
    ax.set_ylabel("Posicion $y$ [m]", fontsize=13, fontweight="medium")
    ax.set_title(f"t = {time:.1f} s", fontsize=12, fontweight="medium")
    fig.colorbar(im, ax=ax, label="Temperatura $T$ [°C]")

plt.suptitle("Difusión de Temperatura en 2D para 4 Tiempos", fontsize=14, fontweight="medium")
plt.tight_layout()
plt.savefig("plot_edp_difusion_2D_4tiempos.png")
plt.show()

fig, ax = plt.subplots(figsize=(7, 6), dpi=120)

T_init = T[0, :].reshape((N, N))
im = ax.imshow(
    T_init.T, 
    origin="lower", 
    extent=[0, L, 0, L], 
    cmap="hot", 
    vmin=50, 
    vmax=100,
    interpolation="bicubic"
)

im.format_cursor_data = lambda data: ""

cbar = fig.colorbar(im, ax=ax)
cbar.set_label("Temperatura $T$ [°C]", fontsize=11)

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
ax.set_ylabel("Posición $y$ [m]", fontsize=13, fontweight="medium")

time_text = ax.text(
    0.05,
    0.92,
    "",
    transform=ax.transAxes,
    fontsize=12,
    color="white",
    bbox=dict(boxstyle="round,pad=0.3", facecolor="black", edgecolor="white", alpha=0.8),
)

plt.title("Evolución Temporal de la Difusión de Temperatura 2D", fontsize=13, fontweight="medium")

def init():
    im.set_array(T_init.T)
    time_text.set_text("")
    return im, time_text

def update(frame):
    T_grid = T[frame, :].reshape((N, N))
    im.set_array(T_grid.T)
    time_text.set_text(f"Tiempo t = {t[frame]:.1f} s")
    return im, time_text

num_frames = len(t)
anim = FuncAnimation(
    fig, update, frames=num_frames, init_func=init, blit=True, interval=50
)

anim.save("animacion_difusion_2D.gif", writer="pillow", fps=20)
plt.tight_layout()
plt.show()