"""
Goal: Create a python program that iteratively calculates and visualizes the motion
of an object in a constant gravitational field.
"""

import math as ma
from sys import argv

"""
Requirement: The iterative calculation may only deviate from the analytic trajectory by
1%. Inputs and outputs should be on one sheet, with calculations on other
sheet(s).
"""

script, g_const, v0_mag, v0_ang_degree, y0, ts = argv

v0_ang = float(v0_ang_degree) / 180.00 * ma.pi
v0x = float(v0_mag) * ma.cos(float(v0_ang))
v0y = float(v0_mag) * ma.sin(float(v0_ang))
ax = 0.0
ay = - (float(g_const))

flytime = (2.0 * v0y) / (-ay)
dis = flytime * v0x
th = v0y / - ay
max_y = ((v0y) ** 2.0 / (2.0 * -ay) + float(y0))

print v0x
print v0y
print ax
print ay

print flytime
print max_y
print dis
print flytime

