#!/usr/bin/env python3

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from time import sleep
#import matplotlib.animation as FuncAnimation
import matplotlib.patches as patches
import os

# Crear el directorio 'animation3/' si no existe
output_dir = "animation3"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

ccolor = ['k', 'r', 'g']  # Data for plotting

with open("view2D.dat") as f:
    data = f.readlines()

iterations, npeople, x_As, x_Bs, y_As, y_Bs, r_circle = data[0].split("\t")
x_A = float(x_As)
x_B = float(x_Bs)
y_A = float(y_As)
y_B = float(y_Bs)
r_circle = float(r_circle)

iterations = iterations[1:]
npeople = int(npeople)
iterations = int(iterations)

X = [[] for x in range(npeople)]
Y = [[] for x in range(npeople)]
C = [[] for x in range(npeople)]

fig, ax = plt.subplots()
iterator = 0

for line in data[1:]:
    if "#" in line[0]:
        iteration, healty, sick, immune, dead = line.split("\t")
        iteration = int(iteration[1:])
        plt.cla()
        ax.set(xlabel='x', ylabel='y', title='TICS UNAM Transmission')
        plt.axis([x_A, x_B, y_A, y_B])
        ax.grid()
        iterator = 0
    else:
        age, gender, status, time_recovery, position, velocity = line.split("\t")
        position = position[1:-2]
        x, y = position.split(",")
        x = float(x)
        y = float(y)
        c = int(status)
        circle = plt.Circle((x, y), r_circle, color=ccolor[c])
        ax.add_artist(circle)
        iterator += 1

    if iterator == npeople:
        rect = patches.Rectangle((-47, -42), 24, 24, color='k', alpha=0.2, fill=True)
        ax.add_patch(rect)
        plt.text(-45, -25, "Healty: " + healty, fontsize=12)
        plt.text(-45, -30, "Sick: " + sick, fontsize=12, color='r')
        plt.text(-45, -35, "Immune: " + immune, fontsize=12, color='g')
        plt.text(-45, -45, "Dead: " + dead, color='b', fontsize=12)

        # Muestra la figura actual en pantalla y pausa para que sea visible
        plt.pause(0.1)  # Pausa breve para visualizar en tiempo real
        fig.savefig(f"{output_dir}/{iteration:04d}-view2D.png")

# Muestra la figura final y completa el flujo de visualización
plt.show()
#!/usr/bin/env python3

# Importación de librerías necesarias para graficar y manejar animaciones
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from time import sleep
#import matplotlib.animation as FuncAnimation  # Comentado porque no se usa en este código
import matplotlib.patches as patches  # Para añadir formas a las gráficas, como rectángulos
import os  # Para manipular el sistema de archivos

# Crear el directorio 'animation3/' si no existe para guardar las imágenes
output_dir = "animation3"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Definición de colores para los estados: negro (sano), rojo (enfermo), verde (inmune)
ccolor = ['k', 'r', 'g']  # Data for plotting

# Leer el archivo de datos "view2D.dat" y almacenar cada línea en una lista
with open("view2D.dat") as f:
    data = f.readlines()

# Extraer los parámetros iniciales de la primera línea del archivo
iterations, npeople, x_As, x_Bs, y_As, y_Bs, r_circle = data[0].split("\t")
x_A = float(x_As)  # Límite inferior del eje x
x_B = float(x_Bs)  # Límite superior del eje x
y_A = float(y_As)  # Límite inferior del eje y
y_B = float(y_Bs)  # Límite superior del eje y
r_circle = float(r_circle)  # Radio de los círculos que representan a cada persona

# Procesar el número de iteraciones y el número de personas en el sistema
iterations = iterations[1:]  # Elimina el primer carácter de iterations (ej., si es un "#")
npeople = int(npeople)  # Convertir el número de personas a entero
iterations = int(iterations)  # Convertir el número de iteraciones a entero

# Inicialización de listas para almacenar las posiciones y estados de cada persona
X = [[] for x in range(npeople)]
Y = [[] for x in range(npeople)]
C = [[] for x in range(npeople)]

# Crear la figura y los ejes para la gráfica
fig, ax = plt.subplots()
iterator = 0  # Contador para recorrer cada persona

# Procesamiento de cada línea de datos en el archivo (excluyendo la primera línea)
for line in data[1:]:
    # Si la línea comienza con "#", indica información de una nueva iteración
    if "#" in line[0]:
        iteration, healty, sick, immune, dead = line.split("\t")
        iteration = int(iteration[1:])  # Convertir el número de iteración a entero
        plt.cla()  # Limpia la gráfica para actualizarla
        ax.set(xlabel='x', ylabel='y', title='TICS UNAM Transmission')  # Configura las etiquetas y título
        plt.axis([x_A, x_B, y_A, y_B])  # Configura los límites de los ejes
        ax.grid()  # Añadir cuadrícula para mejor visualización
        iterator = 0  # Reiniciar el iterador al comenzar una nueva iteración

    # Si la línea no comienza con "#", contiene datos de una persona específica
    else:
        # Dividir la línea en variables de datos: edad, género, estado, etc.
        age, gender, status, time_recovery, position, velocity = line.split("\t")
        position = position[1:-2]  # Elimina caracteres innecesarios en posición
        x, y = position.split(",")  # Separar la posición en coordenadas x e y
        x = float(x)  # Convertir x a flotante
        y = float(y)  # Convertir y a flotante
        c = int(status)  # Convertir estado a entero para usar en la asignación de color

        # Crear un círculo en la posición (x, y) con el color correspondiente al estado
        circle = plt.Circle((x, y), r_circle, color=ccolor[c])
        ax.add_artist(circle)  # Añadir el círculo a la gráfica
        iterator += 1  # Incrementar el contador de personas en esta iteración

    # Si hemos alcanzado el número de personas en la iteración, se actualiza la leyenda y se guarda la imagen
    if iterator == npeople:
        # Añadir un rectángulo semitransparente para la leyenda
        rect = patches.Rectangle((-47, -42), 24, 24, color='k', alpha=0.2, fill=True)
        ax.add_patch(rect)

        # Añadir textos de leyenda con el conteo de cada estado
        plt.text(-45, -25, "Healty: " + healty, fontsize=12)
        plt.text(-45, -30, "Sick: " + sick, fontsize=12, color='r')
        plt.text(-45, -35, "Immune: " + immune, fontsize=12, color='g')
        plt.text(-45, -45, "Dead: " + dead, color='b', fontsize=12)

        # Mostrar la gráfica actualizada en pantalla y hacer una pausa breve
        plt.pause(0.1)  # Pausa para visualizar en tiempo real
        # Guardar la gráfica actual en una imagen PNG en el directorio animation3/
        fig.savefig(f"{output_dir}/{iteration:04d}-view2D.png")

# Mostrar la gráfica final y completar el flujo de visualización
plt.show()
