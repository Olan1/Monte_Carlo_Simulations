# -*- coding: utf-8 -*-
"""
Monte Carlo 2D Integration

This programme will use 2D Monte Carlo integration of the function:
                                ∬ sin(x).sin(y).dx.dy
across the range 0 to pi on the x and y-axis. The area of the shapes base will
be calculated using:
                                area = pi^2
The area of the base will be divided into quadrants of area dA:
                                dA = area/quadrants
A random x and y coordinate will be generated between the range 0 and pi. This
will be done using:
                                x = (xf - xi) * rand - xi
                                y = (yf - yi) * rand - yi
Where:
x - The x coordinate
xf - The highest value in the x-range (pi)
xi - The lowest value in the x-range (0)
y - The y coordinate
yf - The highest value in the y-range (pi)
yi - The lowest value in the y-range (0)
rand - A randomly generated number between 0 and 1
At the x & y coordinates, the height (z) of the shape will be calculated using:
                                z = sin(x) * sin(y)
The volume of the quadrant will be calculated using:
                                volume = dA * z
This will be repeated over a specified number of quadrants and the results
aggregated.
This calculation will be repeated as a function of steps over a range of 1 to 
N steps, where the current number of quadrants is equal to the current N value.
The calculated volume at each step value will be calculated and graphed using
matplotlib.
"""
# Import libraries/modules
import numpy as np
import random as rm
from matplotlib import pyplot as plt

# Steps to perform calculation over
N_steps = range(1, 1001)
# Assign pi to variable
pi = np.pi
# Expected integral value
expected_vol = 4
# Initial x value
xi = 0
# Final x value
xf = pi
# Initial y value
yi = 0
# Final y value
yf = pi
# Area of base
base_area = (xf - xi) * (yf - yi)
# List to store volume values
vol_list = []
# Initialise random number generator
rm.seed()

# Function to generate and scale random variable between specifified range
def calculate_random_coordinate(range_min, range_max):
    """
    Parameters
    ----------
    range_min : TYPE - Float
        DESCRIPTION - Initial range value
    range_max : TYPE - Float
        DESCRIPTION - Final range value
    Returns
    -------
    TYPE - Float
        DESCRIPTION - A random coordinate between range_min and range_max
    """
    # Calculate and return random coordinate between specifified range
    return (range_max - range_min) * rm.random() - range_min

# Calculate height at coordinates x, y
def calculate_height(x, y):
    """
    Parameters
    ----------
    x : TYPE - Float
        DESCRIPTION - x coordinate
    y : TYPE - Float
        DESCRIPTION - y coordinate
    Returns
    -------
    TYPE - Float
        DESCRIPTION - Height at x, y position
    """
    # Calculate and return height
    return np.sin(x) * np.sin(y)

# Calculate total volume
def calculate_vol(base_area, quadrants, xi, xf, yi, yf):
    """
    Parameters
    ----------
    base_area : TYPE - Float
        DESCRIPTION - Area of the shapes base
    quadrants : TYPE - Integar
        DESCRIPTION - Number of sections to divide shape into
    xi : TYPE - Float
        DESCRIPTION - Initial x value
    xf : TYPE - Float
        DESCRIPTION - Final x value
    yi : TYPE - Float
        DESCRIPTION - Initial y value
    yf : TYPE - Float
        DESCRIPTION - Final y value
    Returns
    -------
    vol : TYPE - Float
        DESCRIPTION - Total calculated volume of shape
    """
    # Initial volume set to zero
    vol = 0
    # Area of quadrant base
    dA = base_area/quadrants
    # Iterate through each quadrant
    for quadrant in range(quadrants):
        # Get random x-coordinate
        x = calculate_random_coordinate(xi, xf)
        # Get random y-coordinate
        y = calculate_random_coordinate(yi, yf)
        # Get z at x, y position
        z = calculate_height(x, y)
        # Calculate and add the quadrant volume to total volume
        vol += dA * z
    # Return total volume
    return vol

# Iterate through specified number of steps
for N in N_steps:
    # Calculate the volume as a function of the the current number of steps
    volume = calculate_vol(base_area, N, xi, xf, yi, yf)
    # Append volume calculation to the volume list
    vol_list.append(volume)

# Pyplot graph
# Set title
plt.suptitle('Monte Carlo 2D Integration as a Function of Steps:', size='x-large')
# Set subtitle
plt.title('∬ sin(x).sin(y).dx.dy, limits: 0 and π', size='large')
# Set x-label
plt.xlabel('Steps')
# Set y-label
plt.ylabel('Volume')
# Plot volume as function of N steps
plt.plot(N_steps,
         vol_list,
         color = 'c',
         label = 'Monte Carlo Integration Volume',
         zorder = 1)
# Plot a red line across the expected value
plt.plot([N_steps[0], N_steps[-1]],
         [expected_vol, expected_vol],
         color = 'r',
         label = 'Expected Volume',
         zorder = 2)
# Display legend
plt.legend(loc='best')
