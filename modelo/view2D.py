#!/usr/bin/env python3

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from time import sleep
from matplotlib.animation import FuncAnimation

#Se definen colores
# k #negro, r = rojo, g= verde
#ccolor = ['k', 'r', 'g']  # Data for plotting
ccolor = ['k', 'k', 'k']

#Abre el archivo .dat y leé linea por linea
with open("view2D.dat") as f:
    data = f.readlines()
# Se definen las iteraciones, el número de personas,limites de las coordenadas y el radio de los circulos
iterations, npeople, x_As, x_Bs, y_As, y_Bs, r_circle = data[0].split("\t")  # Splitea cada línea del data usando \t

#Convierte las coordenadas y el radio a flotantes
#Es la ventana en dónde se mostraran y los radios de cada particula para poder usarlos númericamente
x_A = float(x_As)
x_B = float(x_Bs)
y_A = float(y_As)
y_B = float(y_Bs)
r_circle = float(r_circle)

#Se elimina el primer caracter de iteraciones
iterations = iterations[1:]
#Se convierten  enteros
npeople = int(npeople)
iterations = int(iterations)

#Listas para almacenar datos, cada sublista tiene las coordenadas (x,y) y el estado c de cada persona a lo largo del tiempo

X = [[] for x in range(npeople)]
Y = [[] for x in range(npeople)]
C = [[] for x in range(npeople)]

# Crea las figuras y los ejes de la gráfica
fig, ax = plt.subplots()
iterator = 0 #Inicializa en 0 y se usqa para recorrer a las personas

#Sila linea comienza con # , significa que es info de la iteracion
for line in data[1:]:
    if "#" in line[0]:
        iteration, healty, sick, immune, dead = line.split("\t")
    #Se extraen datos especificos de cada perosna
    else:
        age, gender, status, time_recovery, position, velocity = line.split("\t")
        #limpia para quitar caracteres extra y se separan en x e y
        position = position[1:-2]
        x, y = position.split(",")
        #Convertimos los datos
        x = float(x)
        y = float(y)
        c = int(status)

        X[iterator].append(x)
        Y[iterator].append(y)
        C[iterator].append(c)

        if iterator == npeople - 1:
            iterator = 0
        else:
            iterator += 1

ax.set(xlabel='x', ylabel='y', title='view2D')
plt.axis([x_A, x_B, y_A, y_B])
ax.grid()

for b in range(len(X[0])):
    plt.cla()
    ax.set(xlabel='x', ylabel='y', title='TICS UNAM Transmission')
    plt.axis([x_A, x_B, y_A, y_B])
    ax.grid()

    for u, v, c in zip(X, Y, C):
        thecolor = c[b]
        circle = plt.Circle((u[b], v[b]), r_circle, color=ccolor[thecolor])
        ax.add_artist(circle)
    plt.draw()

    plt.pause(0.0001)

def update(i):
    ax.clear()
    ax.set(xlabel='x', ylabel='y', title='TICS UNAM Transmission')
    plt.axis([x_A, x_B, y_A, y_B])
    ax.grid()

    for u, v, c in zip(X, Y, C):
        thecolor = c[i]
        circle = plt.Circle((u[i], v[i]), r_circle, color=ccolor[thecolor])
        ax.add_artist(circle)

animation = FuncAnimation(fig, update, frames=len(X[0]), interval=10)
plt.show()
