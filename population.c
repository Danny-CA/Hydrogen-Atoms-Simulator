#include "population.h"
#include <stdlib.h>

Population new_Population(int size, double T) {
    Population population;
    population.people = (People *)malloc(size * sizeof(People));
    population.size = size;

    for (int i = 0; i < size; i++) {
        // Limitar posiciones iniciales dentro de [-50, 50]
        double x = ((double)rand() / RAND_MAX) * 100 - 50;
        double y = ((double)rand() / RAND_MAX) * 100 - 50;
        population.people[i] = new_People(x, y, T);

        // Escalar velocidades iniciales
        for (int j = 0; j < 3; j++) {
            population.people[i].velocity[j] *= 0.01; // Reducir magnitud de velocidad
        }
    }

    return population;
}

// Implementación de free_Population
void free_Population(Population *p) {
    free(p->people);
    p->people = NULL; // Evita referencias inválidas
    p->size = 0;      // Limpia el tamaño
}
