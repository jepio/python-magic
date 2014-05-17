# invariant_mass

A simple simulation I wrote for myself to check combinatorial background. This simulation lacks proper "physics" but it show the mathematical principles behind cuts and selection.

To run execute `python2.7 mass.py`. Two plots will be generated, a before and an after plot in png format. 

Four hundred decays into electron-positron pairs are simulated. Next all possible combinations are investigated and the ones that:

1. have momenta facing the same direction
2. have momentum of the sum is bigger than an arbitrary number

are rejected. The effect is a very similar distribution to the original one, with some background events.
