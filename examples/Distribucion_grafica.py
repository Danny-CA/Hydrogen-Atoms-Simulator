import numpy as np
import matplotlib.pyplot as plt

def maxwell_boltzmann(v, T, m=1.67e-27):
    k_B = 1.38e-23  # Constante de Boltzmann
    factor = (m / (2 * np.pi * k_B * T)) ** (3 / 2)
    exponential = np.exp(-m * v**2 / (2 * k_B * T))
    return 4 * np.pi * v**2 * factor * exponential

# rango de velocidades
v = np.linspace(0, 3000, 500)

# Temperaturas para graficar
temperaturas = [300, 600, 900]
colores = ['orange', 'red', 'magenta']
labels = [f'T = {T} K' for T in temperaturas]


plt.figure(figsize=(10, 6))

#  distribución de Maxwell-Boltzmann para cada temperatura
for T, color, label in zip(temperaturas, colores, labels):
    plt.plot(v, maxwell_boltzmann(v, T), color=color, lw=2, label=label)


plt.title('Distribución de Maxwell-Boltzmann para un átomo de hidrógeno', fontsize=14)
plt.xlabel('Velocidad (m/s)', fontsize=12)
plt.ylabel('f(v)', fontsize=12)
plt.legend(fontsize=12)
plt.grid()


plt.show()
