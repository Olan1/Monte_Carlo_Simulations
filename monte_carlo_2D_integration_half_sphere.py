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

def calculate_x_y_z(R):
    # Randomly generate and scale x
    x = 2 * R * rm.random() - R
    # Calculate max possible y values within the circle at x
    y_max = np.sqrt(R**2 - x**2)
    # Generate and scale random y value within the range: -y_max <= y <= +y_max
    y = 2 * y_max * rm.random() - y_max
    # Calculate z value at x and y
    z = np.sqrt(R**2 - x**2 - y**2)
    # Place x, y, and z in list
    xyz = [x, y, z]
    # Return x, y and z
    return xyz

# Variable to store volume for cuboid method
cuboid_method_vol = 0
# Variable to store volume for cylinder method
cylinder_method_vol = 0
# Loop through number of quadrants
for i in range(quadrants):
    # Method 1: Cuboid method - Volumes may protrude from sphere
    # Calculate and unpack x, y, and z components using radius R
    x, y, z = calculate_x_y_z(R)
    # Calculate and add the quadrant volume to total volume
    cuboid_method_vol += dA * z
    
    # Method 2: Cylinder method - Volumes may not protrude from sphere
    # Calculate and unpack x, y, and z components using radius R_mod
    x, y, z = calculate_x_y_z(R_mod)
    # Calculate and add the quadrant volume to total volume
    cylinder_method_vol += dA * z

# Print total volume of half sphere
print(f'Cuboid method - {cuboid_method_vol}')
# Print total volume of half sphere
print(f'Cylinder method - {cylinder_method_vol}')
# Print calculated volume of half sphere
print(f'Calculated value - {half_sphere_vol}')
