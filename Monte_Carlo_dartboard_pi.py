# -*- coding: utf-8 -*-
"""
Monte Carlo Dartboard Estimation of Pi

Determine an approximate value of pi using the Monte Carlo dartboard method.
Random x & y values are chosen within the area of a square of side length 2a.
a is the radius of the circle or 'dartboard' within the square. These x and y
coordinates correspond to the landing of a dart. To determine if the
dart hit the dartboard, the Pythagorean theorem is used:

                      R^2 = x^2 + y^2

Where R is the radius of the circle, and x and y are coordinates. If the
squares of the random x and y coordinates are less than the square of
the radius, the dart is within the radius of the circle. This is counted
as a hit. The ratio of darts within the circle to the total numer of darts
thrown is equal to pi/4, since:

                    Prob(circle)/Prob(square) = Circle Area/Square Area
                    
                    Circle Area/Square Area = pi*a^2 / 4*a^2 = pi / 4

Where a is the radius of the circle.
"""

import random as rm
import matplotlib.pyplot as plt

# Constants
square_prob = 1  # Probability of dart landing within square = 100%
a = 1            # Radius of circle - half width of square
N_darts = 10000  # Num of darts thrown
circle_count = 0 # Initial number of darts landed within circle
pi_list = []     # Initialise list for calculated pi values
rm.seed()        # Initialise random generator


def get_random_coordinate(range_min, range_max):
    """
    Calculate a random coordinate within a defined range
    
    ...
    
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
    return (range_max - range_min) * rm.random() - abs(range_min)

  
# Iterate from 0 - N_darts in inrements of 1:
for dart in range(1, N_darts, 1):
    # Generate random x value
    x = get_random_coordinate(-a, a)
    # Generate random y value
    y = get_random_coordinate(-a, a)
   
    # If x^2 + y^2 <= a^2, the dart is within the circle
    if x**2 + y**2 <= a**2:
        # Increment circle_count by 1
        circle_count += 1

    # Calculate probability of a dart landing within the circle
    circle_prob = (circle_count/dart) / square_prob
   
    # Calculate pi:
    # Prob(circle)/Prob(square) = Circle Area/Square Area = pi.a^2/4.a^2 = pi/4
    # Therefore pi = 4 * probability of a dart landing within the circle
    pi = 4 * circle_prob
    pi_list.append(pi)

# Pyplot graph:
plt.xlabel('Darts')      # Set x-axis label
plt.ylabel('Pi Value')   # Set y-axis label
plt.title('Dartboard Method to Calculate pi')    # Set graph title

plt.plot(pi_list) # Plot pi vs darts
plt.plot([0, N_darts], [pi, pi], 'r') # Plot a red line from 0 to N_darts on x-axis
                                      # and at final pi calculation on y-axis
