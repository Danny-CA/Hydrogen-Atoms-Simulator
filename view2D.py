import numpy as np
from scipy.stats import maxwell
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

try:
    with open("view2D.dat", "r") as f:
        data = f.readlines()

    # Extracción de parámetros del encabezado
    first_line = data[0][1:].strip().split("\t")  # Quitar el '#' y dividir por tabulación
    particles, T, frames, x_min, x_max, y_min, y_max, r_circle = map(float, first_line)  # Convertir a flotantes
    frames    = int(frames)
    particles = int(particles)

    positions = []
    velocities = []

    # Elimina líneas que estén vacías o contengan solo espacios en blanco.
    for line in data[1:]:
        if not line.strip():
            continue
        # Extracción de posiciones y velocidades
        parts = line.split("\t")
        pos = list(map(float, parts[0][1:-2].split(",")))  # Elimina el primer carácter ([) y los últimos dos caracteres (] )
        vel = list(map(float, parts[1][2:-2].split(",")))  # Elimina los dos primeros caracteres ([) y los dos últimos caracteres (] )
        positions.append(pos)
        velocities.append(vel)

    # Conversión a numpy arrays
    positions = np.array(positions).reshape(frames, particles, 2)  # (frames, particles, x/y)
    velocities = np.array(velocities).reshape(frames, particles, 2)  # (frames, particles, vx/vy)
    vel_magnitudes = np.linalg.norm(velocities, axis=2)

    fig = plt.figure(figsize=(12, 6))
    ax = fig.add_subplot(1, 2, 1)
    hist = fig.add_subplot(1, 2, 2)

    plt.subplots_adjust(bottom=0.2, left=0.1)
    
    # Configuración del eje de partículas
    ax.axis('equal')
    ax.set_xlim([x_min, x_max])
    ax.set_ylim([y_min, y_max])
    ax.set_title("Simulación de partículas")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")

    # Configuración del histograma
    hist.set_title("Distribución de Velocidades (Maxwell-Boltzmann)")
    hist.set_xlabel("Velocidad")
    hist.set_ylabel("Frecuencia")
    hist.grid(True)

    # Calcular la distribución teórica de Maxwell-Boltzmann
    k_B = 1.38e-23
    m_H = 1.67e-27
    v_range = np.linspace(0, np.max(vel_magnitudes), 500)
    v_mp = np.sqrt(2 * k_B * T / m_H)  # Velocidad más probable
    theoretical_curve = maxwell.pdf(v_range, scale=v_mp)

    # Partículas como círculos
    circles = [plt.Circle((positions[0, i, 0], positions[0, i, 1]), r_circle, color='steelblue', lw=1.5, zorder=20)
               for i in range(particles)]
    for circle in circles:
        ax.add_patch(circle)

    # Función de actualización para la animación
    def update(frame):
        # Actualizar posiciones de partículas
        for i, circle in enumerate(circles):
            circle.set_center((positions[frame, i, 0], positions[frame, i, 1]))

        # Actualizar histograma acumulativo
        hist.clear()
        hist.hist(vel_magnitudes[:frame+1].flatten(), bins=20, color='steelblue', alpha=0.7, density=True)
        hist.plot(v_range, theoretical_curve, 'r-', lw=2, label="Maxwell-Boltzmann")
        hist.legend()
        hist.set_title("Distribución de Velocidades (Maxwell-Boltzmann)")
        hist.set_xlabel("Velocidad")
        hist.set_ylabel("Frecuencia")
        hist.grid(True)

    # Crear la animación
    ani = FuncAnimation(fig, update, frames=frames, interval=50)

    plt.show()

except Exception as e:
    print(f"Error: {e}")