#include <stdio.h>
#include "population.h"

int main() {
    int particles = 50;     // Número de partículas
    double T = 300.0;        // Temperatura en Kelvin
    int steps = 100;         // Número de pasos de simulación
    double dt = 0.001;       // Intervalo de tiempo reducido

    Population population = new_Population(particles, T);

    // Guardar datos en un archivo para visualización
    FILE *file = fopen("view2D.dat", "w");
    fprintf(file, "#%d\t%f\t%d\t%f\t%f\t%f\t%f\t%f\n", particles, T, steps, -50.0, 50.0, -50.0, 50.0, 1.0); // Parámetros

    for (int step = 0; step < steps; step++) {
        for (int i = 0; i < particles; i++) {
            // Actualizar posiciones usando velocidades y dt
            population.people[i].position[0] += population.people[i].velocity[0] * dt;
            population.people[i].position[1] += population.people[i].velocity[1] * dt;

            // Rebote en los límites
            if (population.people[i].position[0] > 50 || population.people[i].position[0] < -50) {
                population.people[i].velocity[0] *= -1;
            }
            if (population.people[i].position[1] > 50 || population.people[i].position[1] < -50) {
                population.people[i].velocity[1] *= -1;
            }

            // Guardar en archivo: posición, velocidad y temperatura
            fprintf(file, "[%f,%f]\t[%f,%f]\n", 
                    population.people[i].position[0], 
                    population.people[i].position[1],
                    population.people[i].velocity[0], 
                    population.people[i].velocity[1]);
        }
    }

    fclose(file);
    free_Population(&population);

    printf("Simulación completada. Archivo generado: view2D.dat\n");
    return 0;
}
