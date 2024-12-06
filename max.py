import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


file_path = "view2D.dat"

try:
    with open(file_path, "r") as f:
        data = f.readlines()
# lectura límites y radio de las partículas
    x_min, x_max, y_min, y_max, r_circle = map(float, data[0][2:].split("\t"))

    positions = []
    velocities = []

    for line in data[1:]:
        if not line.strip():
            continue
        # Extracción de posiciones y velocidades
        parts = line.split("\t")
        pos = list(map(float, parts[4][1:-2].split(",")))  # [x, y]
        vel = list(map(float, parts[5][1:-2].split(",")))  # [vx, vy]
        positions.append(pos)
        velocities.append(vel)

    n_particles = len(positions) // 100  
    frames = 100  

    # Converción a numpy arrays
    positions = np.array(positions).reshape(frames, n_particles, 2)  # (frames, particles, x/y)
    velocities = np.array(velocities).reshape(frames, n_particles, 2)  # (frames, particles, vx/vy)

   
    vel_magnitudes = np.linalg.norm(velocities, axis=2)

   
    fig = plt.figure(figsize=(12, 6))
    ax = fig.add_subplot(1, 2, 1)
    hist = fig.add_subplot(1, 2, 2)

    plt.subplots_adjust(bottom=0.2, left=0.1)

    
    ax.axis('equal')
    ax.set_xlim([x_min, x_max])
    ax.set_ylim([y_min, y_max])
    ax.set_title("Simulación de partículas")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")

    #  partículas como círculos
    circles = [plt.Circle((positions[0, i, 0], positions[0, i, 1]), r_circle, ec="black", lw=1.5, zorder=20)
               for i in range(n_particles)]
    for circle in circles:
        ax.add_patch(circle)

    # Histograma
    hist.set_title("Distribución de velocidades")
    hist.set_xlabel("Velocidad (m/s)")
    hist.set_ylabel("Densidad de frecuencia")

    # Función para actualizar la visualización
    def update(frame_idx):
        frame_idx = int(frame_idx)  

        # Actualizar posiciones de las partículas
        for i, circle in enumerate(circles):
            circle.center = positions[frame_idx, i, 0], positions[frame_idx, i, 1]

        # Actualizar histograma
        hist.clear()
        vel_mod = vel_magnitudes[frame_idx]

        # Validar que haya datos de velocidades
        if len(vel_mod) == 0:
            hist.set_title("Sin datos de velocidades")
            return

        counts, bins, _ = hist.hist(vel_mod, bins=30, density=True, alpha=0.6, label="Simulación")

        # Calculo de  la curva Maxwell-Boltzmann
        m = 1.67e-27  # Masa de un átomo de hidrógeno (kg)
        k = 1.38e-23  # Constante de Boltzmann (J/K)
        avg_energy = 0.5 * m * np.mean(vel_mod ** 2)  # Energía cinética promedio
        T = (2 / 3) * (avg_energy / k)  # Temperatura efectiva

        v = np.linspace(bins[0], bins[-1], 200)
        fv = (m / (2 * np.pi * k * T)) ** (3 / 2) * 4 * np.pi * v ** 2 * np.exp(-m * v ** 2 / (2 * k * T))

        # Verificar que fv y counts tengan valores significativos
        if np.max(fv) > 0 and np.max(counts) > 0:
            fv_scaled = fv / np.max(fv) * np.max(counts)  # Escalar la distribución
            hist.plot(v, fv_scaled, label=f"Maxwell-Boltzmann\nT={T:.2f} K", color="red")
        else:
            hist.set_title("Distribución Maxwell-Boltzmann (datos insuficientes)")

        hist.legend(loc="upper right")

    # Crear la animación automática
    anim = FuncAnimation(fig, update, frames=frames, interval=100, repeat=True)

    
    plt.show()

except FileNotFoundError:
    print("El archivo 'view2D.dat' no se encontró en el directorio actual.")
except Exception as e:
    print(f"Ocurrió un error: {e}")
