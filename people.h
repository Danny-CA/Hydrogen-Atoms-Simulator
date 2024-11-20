#ifndef PEOPLE_H
#define PEOPLE_H

typedef struct {
    double position[3]; // Posición (x, y, z)
    double velocity[3]; // Velocidad (vx, vy, vz)
    int status;         // Estado
    double time_recovery;
} People;

People new_People(double x, double y, double T);

#endif
