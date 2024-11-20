import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")  # Fuerza el backend interactivo

# Leer datos de archivo
with open("view2D.dat") as f:
    data = f.readlines()

# Extraer velocidades (vx, vy) del archivo
velocities = []
for line in data[1:]:
    if not line.strip():
        continue
    vel = line.split("\t")[5][1:-2].split(",")  # Columna de velocidades
    vx, vy = float(vel[0]), float(vel[1])
    velocity_magnitude = np.sqrt(vx**2 + vy**2)  # Magnitud de velocidad
    velocities.append(velocity_magnitude)

# Graficar histograma de velocidades
plt.figure(figsize=(10, 6))
plt.hist(velocities, bins=30, density=True, alpha=0.6, color='blue', label='Simulated')

# Función teórica de Maxwell-Boltzmann
def maxwell_boltzmann(v, T, m=1.67e-27):
    k_B = 1.38e-23  # Constante de Boltzmann
    factor = (m / (2 * np.pi * k_B * T)) ** (3 / 2)
    exponential = np.exp(-m * v**2 / (2 * k_B * T))
    return 4 * np.pi * v**2 * factor * exponential

# Graficar la curva teórica
T = 300  # Ajusta la temperatura según la simulación
v = np.linspace(0, max(velocities), 100)
plt.plot(v, maxwell_boltzmann(v, T) * len(velocities) * (v[1] - v[0]),
         color='red', lw=2, label='Maxwell-Boltzmann')

# Configurar la gráfica
plt.title('Distribución de velocidades - Maxwell-Boltzmann', fontsize=14)
plt.xlabel('Velocidad (m/s)', fontsize=12)
plt.ylabel('Densidad de Probabilidad', fontsize=12)
plt.legend(fontsize=12)
plt.grid()
plt.show()
