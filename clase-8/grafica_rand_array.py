import matplotlib.pyplot as plt
import numpy as np

rand_array = np.genfromtxt("rand_array.txt", delimiter="\n")

plt.figure(figsize=(10, 4))
plt.plot(rand_array, marker='o', linestyle='-', color='b', markersize=3)
plt.xlabel("Índice")
plt.ylabel("Valor")
plt.grid(True)
plt.tight_layout()
plt.savefig("aleatorios.png")
plt.show()