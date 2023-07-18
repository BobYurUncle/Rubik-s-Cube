"""
RotationMatrices

- A helper module used to create a rotation matrix relative to either the x, y, or z axes based on an angle given in radians
- References:
    Rotation matrices - https://journals.iucr.org/d/issues/2001/10/00/ba5006/#:~:text=The%20rows%20of%20a%20rotation%20matrix%20are%20orthogonal%20unit%20vectors&text=3.2%2C%20since%20the%20inverse%20(transposed,in%20exactly%20the%20opposite%20direction. 

"""

# **** UNITS FOR ANGLES ARE RADIANS ****
from math import sin, cos

def rotate_x_matrix(angle):
    return [[1, 0, 0], [0, int(cos(angle)), int(sin(angle))],[0, -1 * int(sin(angle)), int(cos(angle))]]

def rotate_y_matrix(angle):
    return [[int(cos(angle)), 0, -1 * int(sin(angle))], [0, 1, 0], [int(sin(angle)), 0, int(cos(angle))]]

def rotate_z_matrix(angle):
    return [[int(cos(angle)), int(sin(angle)), 0], [-1 * int(sin(angle)), int(cos(angle)), 0], [0, 0, 1]]
