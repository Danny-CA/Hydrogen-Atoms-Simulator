#include "people.h"
#include <stdlib.h>
#include <time.h>
#include <math.h>  // Incluye las funciones matemáticas como exp()
#define M_PI 3.14159265358979323846

// Genera velocidades usando la distribución de Maxwell-Boltzmann
double maxwell_boltzmann_velocity(double T) {
    const double k_B = 1.38e-23; // Constante de Boltzmann (J/K)
    const double m_H = 1.67e-27; // Masa del átomo de hidrógeno (kg)

    // Generar una velocidad aleatoria con aceptación/rechazo
    double v, f, r;
    do {
        double v_mp = sqrt(2 * k_B * T / m_H); // Calcula la velocidad más probable
        v = ((double)rand() / RAND_MAX) * (4 * v_mp); // Escala el rango dinámicamente
        f = (m_H / (2 * M_PI * k_B * T)) * exp(-m_H * v * v / (2 * k_B * T));
        r = ((double)rand() / RAND_MAX) * f; // Aceptación/rechazo
    } while (r > f);
    return v; // magnitudes
}

// Inicializar una nueva partícula
People new_People(double x, double y, double T) {
    People person;

    // Inicializar posición
    person.position[0] = x;
    person.position[1] = y;
//  person.position[2] = 0.0; eje z

    // Generar velocidades
    person.velocity[0] = maxwell_boltzmann_velocity(T);
    person.velocity[1] = maxwell_boltzmann_velocity(T);
//  person.velocity[2] = maxwell_boltzmann_velocity(T); eje z

    person.status = 0; // Estado inicial (puedes cambiarlo)
    person.time_recovery = 0.0;

    return person;
}
