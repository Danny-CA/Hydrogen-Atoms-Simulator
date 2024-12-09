#include "population.h"
#include <stdlib.h>

Population new_Population(int particles, double T) {
    Population population;
    population.people = (People *)malloc(particles * sizeof(People));
    population.size = particles;

    for (int i = 0; i < particles; i++) {
        // Limitar posiciones iniciales dentro de [-50, 50]
        double x = ((double)rand() / RAND_MAX) * 100 - 50;
        double y = ((double)rand() / RAND_MAX) * 100 - 50;
        population.people[i] = new_People(x, y, T);
    }
    return population;
}

// Implementación de free_Population
void free_Population(Population *p) {
    free(p->people);
    p->people = NULL; // Evita referencias inválidas
    p->size = 0;      // Limpia el tamaño
}
