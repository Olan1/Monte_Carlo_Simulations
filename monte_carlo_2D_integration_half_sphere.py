# -*- coding: utf-8 -*-
"""
Monte Carlo 2D Integration of a Half-Sphere

This programme will use 2 different methods of Monte Carlo integration to
calculate the volume of a half-sphere. Method 1 will divide the area of the
half-spheres base circle into quadrants of area dA. A random point will be
picked on the x-axis. To do this, a random number between 0 and 1 will be
generated. This number will be scaled to a range of ± the radius of the base
circle using the following formula:
                            x = 2 * R * rand - R
Where:
R - The radius of the base circle
rand - A random number between 0 and 1
The max possible y value at this x-coordinate will then be calculated. Since:
                            R^2 = x^2 + y^2
Since R and x are known values:
                            y_max = sqrt(R^2 - x^2)
Where:
R - Radius of base circle
x - x coordinate
y_max - The maximum possible value of the y coordinate
The y coordinate can then be calculated using:
                            y = 2 * y_max * rand - y_max
Finally, the z coordinate will be the height of the half-sphere at the chosen
x and y coordinates. Since:
                            R^2 = x^2 + y^2 + z^2
Rearranged:
                            z = sqrt(R^2 - x^2 - y^2)
From these calculated x, y, and z coordinates, the volume of the quadrant can
be calculated using:
                            V = dA * z
Where:
V - Volume
dA - Area of the base
z - Height
These calculations will be performed repeatedly in a loop for the number of
quadrants specified. The volumes of each quadrant will be aggregated.
For method 1, the x and y points can be chosen anywhere on the x-y plane.
Because of this, some points may be picked on the edge of the circle. This
means that some of the calculated volume will protrude from the half-sphere.
This will also occur on the z-axis for all calculations, as the volume formula
does not take into account the curved surface area of the half-sphere.

Method 2 is identical to method 1 except it will not use volumes that protrude
from the sphere in its calculations. To do this, the quadrant radius (r) of
area dA will be calculated using:
                            dA = pi * r^2
Rearranged:
                            r = sqrt(dA/pi)
Where:
dA - Area of the quadrant
pi - pi
r - Radius of the quadrant
This calculated r value will be deducted from the half-spheres base radius (R):
                            R_mod = R - r
Where:
R_mod - Modified radius of circle
R - Original radius of circle
r - Radius of quadrant
The x and y calculations specified in method 1 will be performed using the
modified radius value (R_mod). The z calculation will be performed using the
unmodified radiusvalue  (R). This will ensure that no shape will protrude on
the x-y plane as the max possible protrusion for a quadrant is the radius of
its base.
"""
# Import libraries/modules
import random as rm
import numpy as np

# Variables:
# Radius of half-sphere
R = 1.0
# Assign pi to variable
pi = np.pi
# Calculated volume of half-sphere
half_sphere_vol = 2/3 * pi * R**3
# Area of circle base
base_area = pi * R**2
# Number of quadrants to divide circle into
quadrants = 1000
# Area of each quadrant
dA = base_area/quadrants
# Radius of quadrant
r = np.sqrt(dA/pi)
# Modified radius to ensure volume calculations do not protrude from circle
R_mod = R - r
# Number of times volume calculations will be repeated
iterations = 100
# List to store method 1 volumes (protruding volume)
protruding_vol_list = []
# List to store method 2 volumes (non-protruding volume)
non_protruding_vol_list = []
# Initialise random number generator
rm.seed()

# Iterate through number of specified iterations
for i in range(iterations):
    # Variable to store volume for method 1 (protruding volume)
    protruding_vol = 0
    # Variable to store volume for method 2 (non-protruding volume)
    non_protruding_vol = 0
    # Iterate through specified number of quadrants
    for quadrant in range(quadrants):
        # Method 1: Volumes may protrude from sphere
        # Randomly generate & scale x coordinate in the range: -R <= x <= +R
        x = 2 * R * rm.random() - R
        # Calculate max possible y value at x coordinate
        y_max = np.sqrt(R**2 - x**2)
        # Generate & scale random y coordinate in the range: -y_max <= y <= +y_max
        y = 2 * y_max * rm.random() - y_max
        # Calculate z value at x and y coordinates, i.e. height of half-sphere
        z = np.sqrt(R**2 - x**2 - y**2)
        # Calculate and add the quadrant volume to total volume
        protruding_vol += dA * z

        # Method 2: Volumes may not protrude from sphere
        # Randomly generate & scale x coordinate in the range: -R_mod <= x <= +R_mod
        x = 2 * R_mod * rm.random() - R_mod
        # Calculate max possible y value at x coordinate
        y_max = np.sqrt(R_mod**2 - x**2)
        # Generate & scale random y coordinate in the range: -y_max <= y <= +y_max
        y = 2 * y_max * rm.random() - y_max
        # Calculate z value at x and y coordinates, i.e. height of half-sphere
        z = np.sqrt(R**2 - x**2 - y**2)
        # Calculate and add the quadrant volume to total volume
        non_protruding_vol += dA * z

    # Append the method 1 volume calculation to list
    protruding_vol_list.append(protruding_vol)
    # Append the method 2 volume calculation to list
    non_protruding_vol_list.append(non_protruding_vol)

# Calculate the average volume for method 1 (protruding volume)
protruding_vol_avg = np.mean(protruding_vol_list)
# Calculate the standard deviation for method 1 (protruding volume)
protruding_vol_std = np.std(protruding_vol_list)
# Calculate the average volume for method 2 (non-protruding volume)
non_protruding_vol_avg = np.mean(non_protruding_vol_list)
# Calculate the standard deviation for method 2 (non-protruding volume)
non_protruding_vol_std = np.std(non_protruding_vol_list)

# Print the average volume and standard deviation for method 1 to the console
print(f'Method 1 avg vol (protruding) - {protruding_vol_avg}')
print(f'Standard deviation: {protruding_vol_std}\n')
# Print the average volume and standard deviation for method 2 to the console
print(f'Method 2 avg vol (non-protruding) - {non_protruding_vol_avg}')
print(f'Standard deviation: {non_protruding_vol_std}\n')
# Print the calculated volume of the half sphere to the console
print(f'Calculated Volume - {half_sphere_vol}')
