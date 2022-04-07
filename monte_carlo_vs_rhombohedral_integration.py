# -*- coding: utf-8 -*-
"""
Rhombohedral Integration vs Monte Carlo Integration

Integration is a branch of calculus used to determine the area under a curve.
Integration can be used to calculate quantities such as volume or area. There
are several integration techniques. The rhombohedral integration method
involves dividing the area under the curve into sections, calculating the area
of these smaller sections individually, and aggregating the results. To define
these sections, 2 points on the x-axis are picked (x1 and x2). The
corresponding y-values are determined as a function of x:
    
                                f(x) = y
                                
Therefore:

                                f(x1) = y1
                                f(x2) = y2

The area of the section can be determined using:
    
                                Area = (y2 + y1)/2 * delta_x
                            
Where delta_x is the difference between x1 and x2:
    
                                delta_x = x2 - x1

This is repeated across a defined range of x values. The rhombohedral method 
approximates the shape of the section and does not take curved edges into
account. It is for this reason it is less accurate than other integration
methods.

The Monte Carlo method is similar to the rhombohedral method in that it divides
the area under the curve into sections, calculates the area of these smaller
sections using the same formula as above, and aggregates the results. Where
this method differs is it is not performed linearly across the range of
x-values. A random x value is generated across the x range where:
                    
                                x1 = randomly generated x
                                
                                x2 = x1 + delta_x
                                
The corresponding y1 and y2 values can be calculated as a function of x as
specified earlier. This is repeated for a set number of iterations and the
areas aggregated.

This programme will compare both methods to each other and to the expected
outcome. The function used will be sine:
    
                                f(x) = sin(x) = y

The expected result for integrating the sine function across the x-range 0 to
pi is 2. The results and errors will be graphed using matplotlib.
"""

# Import libraries/modules
import numpy as np
import random as rm
from matplotlib import pyplot as plt

# Variables:
fn = np.sin               # Specify function
pi = np.pi                # Assign pi to variable
xi = 0                    # Initial x value
xf = pi                   # Final x value
steps = range(1, 1000, 1) # List of steps from 1 to 1000 in increments of 1
rhombo_perc_errors = []   # List to store rhombohedral integration errors
mc_perc_errors = []       # List to store Monte Carlo integration errors
correct_val = 2           # Correct integration result

# Initialise random number generator
rm.seed()

# Functions:
# Rhombohedral integration method
def rhombo(fn, x_steps, xi, xf):
    """
    Integrate over a defined range using the rhombohedral method
    
    ...
    
    Parameters
    ----------
    fn : TYPE - Function
        DESCRIPTION - Function to be used in calculation
    x_steps : TYPE - Int
        DESCRIPTION - Number of steps across x-range
    xi : TYPE - Float
        DESCRIPTION - Initial x value
    xf : TYPE - Float
        DESCRIPTION - Final x value
    Returns
    -------
    area : TYPE - Float
        DESCRIPTION - Area under the curve
    """
    # Create list of x values from xi to xf with x_steps number of increments
    x_vals = np.linspace(xi, xf, x_steps)
    # Calculate delta x
    dx = (xf-xi)/x_steps
    # Initial area is 0
    area = 0
    # Iterate through each x value
    for x in x_vals:
        # Calculate area of section and add to total area
        # area = (y2+y1)/2 * delta x
        area += (fn(x+dx) + fn(x))/2 * dx
    # Return final area value
    return area

# Monte Carlo integration method
def monte_carlo_integrate(fn, x_steps, xi, xf):
    """
    Integrate over a defined range using Monte Carlo integration
    
    ...
    
    Parameters
    ----------
    fn : TYPE - Function
        DESCRIPTION - Function to be used in calculation
    x_steps : TYPE - Int
        DESCRIPTION - Number of steps across x-range
    xi : TYPE - Float
        DESCRIPTION - First x value
    xf : TYPE - Float
        DESCRIPTION - Final x value
    Returns
    -------
    area : TYPE - Float
        DESCRIPTION - Area under the curve
    """
    # Create list of x values from xi to xf with x_steps number of increments
    x_vals = np.linspace(xi, xf, x_steps)
    # Calculate delta x
    dx = (xf-xi)/x_steps
    # Initial area is 0
    area = 0
    # Iterate through each x value
    for x in x_vals:
        # Generate random variable between 0 and 1
        rand = rm.random()
        # Scale random variable with range = min + value * (max - min)
        rand_x = x_vals[0] + rand * (x_vals[-1] - dx - x_vals[0])
        # Calculate area of section and add to total area
        # area = (y2-y1)/2 * delta x
        area += (fn(rand_x+dx) + fn(rand_x))/2 * dx
    # Return final area value
    return area

# Calculate area & % error for each method over a range of step numbers:
# Iterate through steps list
for step in steps:
    # Integrate using the rhombohedral method
    rhombo_area = rhombo(fn, step, xi, xf)
    # Calculate % error of rhombohedral integration compared to correct value
    rhombo_perc_error = (rhombo_area - correct_val)/correct_val * 100
    # Append the rhombohedral % error to list
    rhombo_perc_errors.append(rhombo_perc_error)
    
    # Integrate using the Monte Carlo method
    mc_area = monte_carlo_integrate(fn, step, xi, xf)
    # Calculate % error of Monte Carlo integration compared to correct value
    mc_perc_error = (mc_area - correct_val)/correct_val * 100
    # Append the Monte Carlo % error to list
    mc_perc_errors.append(mc_perc_error)

# Plot pyplot graph:
# Set title
plt.title('Rhombohedral vs. Monte Carlo Integration')
# Set x-label
plt.xlabel('Steps')
# Set y-label
plt.ylabel('% Error')
# Plot rhombo % error vs number of steps
plt.plot(steps, rhombo_perc_errors, 'r--', label='Rhombohedral', zorder=2)
# Plot Monte Carlo % error vs number of steps
plt.plot(steps, mc_perc_errors, 'b', label='Monte Carlo', zorder=1)
# Display legend
plt.legend(loc='best')
