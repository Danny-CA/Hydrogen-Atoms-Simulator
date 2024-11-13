<<<<<<< HEAD
<h1>Transmission</h1>

[<img src="https://img.youtube.com/vi/TpM7fpkYzZQ/hqdefault.jpg" width="100%">](https://youtu.be/TpM7fpkYzZQ)

<p>

2020/05/11

Author: Victor De la Luz

email: vdelaluz@enesmorelia.unam.mx

License: GNU/GPL

Languaje: C

Compile: make

Run: ./transm > view2D.dat

Create visualization:

./view2D.py

ffmpeg   -framerate 60   -pattern_type glob   -i 'animation/*.png'   -r 15   -vf scale=512:-1 ../transmission.mp4 ;
</p>
=======
## Hydrogen Atoms Simulator: Behavior Under Heat and Cold

## Members and Contact
* Erika Monserrat Correa Hernández | erikacorreahdezenes@gmail.com
* Daniel Camilo  | camilodani065@gmail.com
* Humberto Cortez | tejedordealas@gmail.com 
## License
GNU General Public License v3.0
## Affilation
Final project for the 2025-1 Modeling and Simulation class, designed and developed at the Universidad Nacional Autonoma de México(UNAM), at the Escuela Nacional de Estudios Superiores (ENES Morelia). This project is carried out by students of the Bachelor's Degree in Technologies for Information in the Sciences.
## Introduction

This project aims to simulate the behavior of hydrogen atoms when subjected to heat or cold, using Molecular Dynamics (MD) methods. To achieve accurate simulation, the transmission model will be initialized using Maxwell's equations to correctly describe the electromagnetic interactions influencing the dynamics of atoms at the microscopic level. Additionally, the simulation environment will be configured in ECLive, where a gas model will be employed to efficiently represent thermal conditions.

The simulation will track the trajectory of the atoms under controlled temperature conditions, observing how they move and how interactions between them vary depending on temperature changes. This study will not only visualize atomic-level thermal motions but also infer relevant macroscopic properties from the observed behavior.

## General Objective
To simulate and analyze the behavior of hydrogen atoms under the influence of thermal variations, employing Molecular Dynamics and Maxwell's equations in a computational simulation environment using ECLive.
## Particular Objetives

* Study atomic-level thermal motion: Analyze how heat and cold affect the vibration and displacement of hydrogen atoms during the simulation.

* Observe atomic interactions: Evaluate how atoms interact with each other and how these interactions are modified by temperature variations.

## Tools

* C++ 23 for compilation
* Python 3 for visualization


>>>>>>> b56e51560abc16baae65e0cb70b6afc446d3963a
