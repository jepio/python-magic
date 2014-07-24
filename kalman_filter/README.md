# kalman_filter

A 1D Kalman Filter for a linear system with constant velocity.

Run with `./kalman_filter number` to generate a plot showing the evolution of
the system and the estimate over *number* samples. Without a parameter *number*
will be equal 25. Additionally the final system variance estimate is printed.

This simple script uses numpy to generate random data and matplotlib to plot. 
The outcome can be seen below:

![kalman filter plot](./kalman.png)
