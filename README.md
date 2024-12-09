## Hydrogen Atoms Simulator
This is the final project of the subject Modeling and Simulation of the [<ins>Escuela Nacional de Estudios Superiores UNAM campus Morelia </ins>](https://www.enesmorelia.unam.mx).
This project is carried out by students of the Bachelor's Degree in Technologies for Information in the Sciences.

## Members and Contact
* Erika Monserrat Correa Hernández | erikacorreahdezenes@gmail.com
* Daniel Camilo  | camilodani065@gmail.com
* Humberto Cortez | tejedordealas@gmail.com 
## License
This project is protected under the MIT Licence, please refer to the document in case of any doubt towards referencing and usage of this project.

## Introduction

This project aims to simulate the behavior of hydrogen atoms when subjected to heat or cold, using Molecular Dynamics (MD) methods. To achieve accurate simulation, the transmission model will be initialized using Maxwell's distribution to correctly describe the interactions influencing the dynamics of atoms at the microscopic level. Additionally, the simulation environment will be configured in ECLive, where a gas model will be employed to efficiently represent thermal conditions.

The simulation will track the trajectory of the atoms under controlled temperature conditions, observing how they move and how interactions between them vary depending on temperature changes. This study will not only visualize atomic-level thermal motions but also infer relevant macroscopic properties from the observed behavior.
## Justification
The basic idea of the N-body problem came in 1687 with Isaac Newton's work Principia. The capability of describing the interaction between different particles through Newton's second law of motion with equations brought a lot of attention and investigation to reach the solution of the problem. Later, the limitations of this problem were found by Henry Poincaré: something known as the non-integrability principle. Which would occur whenever there were three or more bodies in the problem.

Due to these issues, there aren't analytical solutions to the N-Body problem. Leading us to the use of numerical methods that are capable of tracking and moving the position of each particle in the system given some initial data. This results in numerical solutions whose accuracy tends to have really satisfactory results for long periods of time. Allowing us to give approximate solution to lots of problems of this nature.
## General Objective
To simulate and analyze the behavior of hydrogen atoms under the influence of thermal variations, employing Molecular Dynamics and Maxwell's distribution in a computational simulation environment using ECLive.
## Particular Objetives
* Particle modeling: n-body problem. 
* Study atomic-level thermal motion: Analyze how heat and cold affect the displacement of hydrogen atoms during the simulation.

* Observe atomic interactions: Evaluate how atoms interact with each other and how these interactions are modified by temperature variations.
## Methodology
# N-body model:

* Represent each atom as a particle in 2D space.

* Consider interactions between particles based on different temperatures.

# Molecular Dynamics (MD) methods:

* Generate initial velocities based on the Maxwell-Boltzmann distribution.

# Visualization:

* Plot the particle trajectories.
* Represent the histogram of velocities and frequencies. Compare it with the theoretical Maxwell-Boltzmann distribution.
## Software tools

* C++ 
* Python 3.11
* matplotlib version 3.9.2
* numpy version 2.1.1
  
## Results Simulated
<img width="876" alt="implementación" src="https://github.com/user-attachments/assets/e49ece34-c0e0-4afc-9a0f-c4525013be09">

## Results Final

[![Watch video](https://img.youtube.com/vi/yqLzYJh7v50/maxresdefault.jpg)](https://youtu.be/yqLzYJh7v50)


## References

https://en.wikipedia.org/wiki/Maxwell–Boltzmann_distribution


