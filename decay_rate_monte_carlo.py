# -*- coding: utf-8 -*-
"""
The Monte Carlo Method - Radioactive Decay

Radioactive decay occurs when unstable nuclei spontaneously breakdown into more
stable nuclei in a process that releases energy and matter from the nucleus.
The radioactive decay rate describes the average number of decays that occur
per unit time. The formula for the decay rate is as follows:

                                dN/dt = -λ * N

Where:
    
dN/dt - The first order differential of the number of nuclei with respect to time
λ - The decay constant
N - The number of nuclei

Radioactive decay is a random process. This means it cannot be predicted accurately
for a single particle, but can be described statistically through averages and 
probabilities.

The Monte Carlo method is a method to simulate random processes. Although there
are several forms of the method, the basic methodology consists of; definining
a range of possible inputs, generating random input variables distributed across
this range, performing a deterministic computation (reproducable output) on these
inputs, and combining the results.

This programme will use a Monte Carlo simulation to predict the decay rate. The
decay constant is a probability that a decay will occur, and will have a value
between 0 and 1. A random number generator will generate a value across this range.
If the random variable is less than the decay constant, the particle has decayed.
This will be repeated for all nuclei over a specified time period. The result
will be graphed using matplotlib. To test the accuracy of the Monte Carlo method,
a differential calculation will also be performed using the above equation in
combination with solve_ivp. This will also be graphed using matplotlib.
"""

# Import libraries/modules
import random as rm
from scipy.integrate import solve_ivp
from matplotlib import pyplot as plt
import numpy as np

# Variables:
lmbda = 0.01                # Decay constant (lambda)
Ni = 10000                  # Initial number of nuclei
N_list = [Ni]               # List of non-decayed nuclei amounts
ti = 0                      # Start time
tf = 1000                   # End time
t = np.arange(ti, tf, 1)    # List of time values from ti to tf in steps of 1

rm.seed()                   # Initialise the random number generator

# Functions:
def slope(t, N, lmbda):
    """
    Calculate the slope for the radioactive decay equation
    
    ...
    
    Parameters
    ----------
    t : TYPE - Int
        DESCRIPTION - Current time value
    N : TYPE - List
        DESCRIPTION - List of non-decayed nuclei amounts
    lmbda : TYPE - Float
        DESCRIPTION - Decay constant

    Returns
    -------
    dN_dt : TYPE - Float
        DESCRIPTION - First order derivative of N with respect to t
    """
    # Calculate the slope
    dN_dt = -lmbda * N
    # Return the slope
    return dN_dt

def monte_carlo(t, N_list, lmbda):
    """
    Differentiate using a Monte Carlo method
    
    ...
    
    Parameters
    ----------
    t : TYPE - Int
        DESCRIPTION - Time variable
    N_list : TYPE - List
        DESCRIPTION - List of number of nuclei values
    lmbda : TYPE - Float
        DESCRIPTION - Decay constant

    Returns
    -------
    N_list : TYPE - List
        DESCRIPTION - List of number of nuclei values
    """
    # Iterate from 0 to final t value
    for i in range(t[-1]):
        # Set N to the last value in the N list
        N = N_list[-1]
        # Iterate through every non-decayed atom
        for atom in range(N):
            # Generate random variable between 0 and 1
            rand = rm.random()
            # If random variable is less than decay constant, the atom has decayed
            if rand < lmbda:
                # Remove the atom from total number of non-decayed atoms
                N -= 1
        # Append new N value to N_list
        N_list.append(N)
    # Return list of N values
    return N_list

""" Main Logic: """
# Monte Carlo method
monte_carlo_res = monte_carlo(t, N_list, lmbda)

# Differential method using solve_ivp
sol = solve_ivp(slope,               # Slope function
                [ti, tf],            # x range - time
                [Ni],                # Initial y value - number of nuclei
                args=(lmbda,),       # Constants - decay constant
                t_eval=t,            # Specify t points
                method='LSODA')      # Integration method set to LSODA (ODEINT method)

""" Plot """
# Set x-axis label
plt.xlabel('Time')
# Set y-axis label
plt.ylabel('N')
# Set graph title
plt.title('Radioactive Decay - Monte Carlo Simulation')
# Plot N vs t - Monte Carlo method
plt.plot(t, monte_carlo_res, color='g', label='Monte Carlo Method')
# Plot N vs t - Differential method
plt.plot(sol.t, sol.y[0], 'r--', label='Differential Method')
# Display legend
plt.legend(loc='best')
