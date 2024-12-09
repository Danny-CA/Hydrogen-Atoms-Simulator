## Hydrogen Atoms Simulator
This is the final project of the subject Modeling and Simulation of the [<ins>Escuela Nacional de Estudios Superiores UNAM campus Morelia </ins>](https://www.enesmorelia.unam.mx).
This project is carried out by students of the Bachelor's Degree in Technologies for Information in the Sciences.

## Members and Contact
* Erika Monserrat Correa Hernández | erikacorreahdezenes@gmail.com
* Daniel Camilo  | camilodani065@gmail.com
* Humberto Cortez | tejedordealas@gmail.com

## License
This project is licensed under the MIT License. Please refer to the LICENSE document for more details regarding referencing and usage of this project.

## Introduction
This project aims to simulate the behavior of hydrogen atoms when subjected to heat or cold, using Molecular Dynamics (MD) methods. To achieve accurate simulation, the transmission model will be initialized using Maxwell's distribution to correctly describe the interactions influencing the dynamics of atoms at the microscopic level. Additionally, the simulation environment will be configured in ECLive, where a gas model will be employed to efficiently represent thermal conditions.

The simulation will track the trajectory of the atoms under controlled temperature conditions, observing how they move and how interactions between them vary depending on temperature changes. This study will not only visualize atomic-level thermal motions but also infer relevant macroscopic properties from the observed behavior.

## Justification
The N-body problem is essential for understanding systems where multiple particles interact under mutual forces. Due to its complexity, it lacks general analytical solutions, requiring numerical methods to obtain approximate results. This project aims to simulate these interactions and visualize them intuitively, contributing to the practical understanding of these systems and their scientific

## General Objective
To simulate and analyze the behavior of hydrogen atoms under the influence of thermal variations, employing Molecular Dynamics and Maxwell's distribution in a computational simulation environment using ECLive.

## Particular Objetives
* Particle modeling: n-body problem. 
* Study atomic-level thermal motion: Analyze how heat and cold affect the displacement of hydrogen atoms during the simulation.
* Observe atomic interactions: Evaluate how atoms interact with each other and how these interactions are modified by temperature variations.
  
## Methodology
  ### 1.- Initialization
* Define the initial parameters of the simulation, including the number of hydrogen atoms, their initial positions, and velocities based on the Maxwell-Boltzmann distribution.
* Establish boundary conditions for the simulation environment.

  ### 2.- Simulation Algorithm
* Employ Molecular Dynamics (MD) to compute the time evolution of the system using numerical integration methods 

  ### 3.- Data Collection
* Record particle trajectories, velocities, and interactions at each simulation step.
* Generate data outputs compatible with visualization scripts, such as view2D.dat.

  ### 4.- Visualization and Analysis
* Use Python scripts (e.g., view2D.py) to visualize the trajectories and velocity distributions of hydrogen atoms.
* Analyze results to observe thermal motion patterns and validate them against theoretical Maxwell-Boltzmann distributions.

### N-body model:
* Represent each atom as a particle in 2D space.
* Consider interactions between particles based on different temperatures.

### Molecular Dynamics (MD) methods:
* Generate initial velocities based on the Maxwell-Boltzmann distribution.

## Software tools
* C++ 
* Python 3.11
* matplotlib version 3.9.2
* numpy version 2.1.1
  
## Results Simulated
<img width="876" alt="implementación" src="https://github.com/user-attachments/assets/e49ece34-c0e0-4afc-9a0f-c4525013be09">

## Simulation Video

[![Watch a video](https://img.youtube.com/vi/yqLzYJh7v50/maxresdefault.jpg)](https://youtu.be/yqLzYJh7v50?si=j0R-9n6avMizQ8j4)


## References
https://github.com/giccunam/transmission

https://en.wikipedia.org/wiki/Maxwell%E2%80%93Boltzmann_distribution

https://en.wikipedia.org/wiki/Maxwell%E2%80%93Boltzmann_distribution#/media/File:Simulation_of_gas_for_relaxation_demonstration.gif

