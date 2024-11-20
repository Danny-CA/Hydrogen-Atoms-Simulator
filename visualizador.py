import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib
matplotlib.use("TkAgg")  # Fuerza el backend interactivo

# Leer datos de archivo
with open("simulation.dat") as f:
    data = f.readlines()

# Leer límites y radio de las partículas
x_min, x_max, y_min, y_max, r_circle = map(float, data[0][2:].split("\t"))

# Preparar listas de posiciones por frames
X, Y = [], []
frame_data = []

for line in data[1:]:
    if not line.strip():
        continue
    pos = line.split("\t")[4][1:-2].split(",")
    X.append(float(pos[0]))
    Y.append(float(pos[1]))

# Separar las posiciones por frames
n_particles = len(X) // 100  # Partículas por frame
frames = [slice(i * n_particles, (i + 1) * n_particles) for i in range(100)]

fig, ax = plt.subplots()
ax.set(xlabel='X', ylabel='Y', title='Simulación de Maxwell-Boltzmann')
plt.axis([x_min, x_max, y_min, y_max])

# Inicializar partículas
particles, = ax.plot([], [], 'o', color='blue', alpha=0.5)

# Función de actualización
def update(frame):
    start, end = frames[frame].start, frames[frame].stop
    particles.set_data(X[start:end], Y[start:end])
    return particles,

# Crear animación
ani = FuncAnimation(fig, update, frames=len(frames), interval=100, blit=True)
plt.show()
