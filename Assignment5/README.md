Assignment5
===========

### How to run

    python ising.py <dimension of array> <temperature>

### Output

Please see SolutionOutputs folder.

Meeting on Sunday, December 7th
--------------------------------

Goal: complete animation, equilibrium condition, entropy calculation

Present: everyone

Member        |     Role
------------- | -------------
Ben Israeli    | Zuckerberg
Chris Florencio-Aleman  | question asker
Kathleen Kennedy  | scribe
Sean Ballinger  | leader

- Sean worked on animations
- Ben worked on the order parameter
- Kathleen worked on the entropy calculation
- All discussed results

Comments on Animation Results
-----------------------------
For T = 10J it takes ~230,000 iterations to reach equilibrium

For T = 0.1J it takes ~270,000 iterations to reach eqiulibrium

This is as expected because the higher temperature makes it less likely for a spin to flip to an unfavorable value according to the Boltzmann probability which depends on the value of k*T.

Comments on Phase Transition/Order Parameter Results
--------------------------------------------------------


Entropy Calculation
-------------------
The entropy can be calculated from the Boltzmann relation S = k*ln(g) where k is Boltzmann's constant and g is the multiplicity of the macrostate. The macrostate of the system is determined by the number of up-spins vs down-spins at any given time, so g is calculated by finding how many different configurations of the system are possible with the same number of up-spins. 
