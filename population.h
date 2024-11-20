#ifndef POPULATION_H
#define POPULATION_H

#include "people.h"

typedef struct {
    People *people;
    int size;
} Population;

Population new_Population(int size, double T);
void free_Population(Population *p); // Declaración de la función

#endif
