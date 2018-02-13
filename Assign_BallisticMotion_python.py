"""
Goal: Create a python program that iteratively calculates and visualizes the motion
of an object in a constant gravitational field.
"""


import math as ma
from sys import argv
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

"""
Requirement: The iterative calculation may only deviate from the analytic trajectory by
1%. Inputs and outputs should be on one sheet, with calculations on other
sheet(s).
"""

script, g_const, v0_mag, v0_ang_degree, y0, ts = argv

#floating all numbers
g_const = float(g_const)
v0_mag = float(v0_mag)
v0_ang_degree = float(v0_ang_degree)
y0 = float(y0)
ts = float(ts)

#time indepedent calculations
v0_ang = (v0_ang_degree) / 180.00 * ma.pi
v0x = (v0_mag) * ma.cos((v0_ang))
v0y = (v0_mag) * ma.sin((v0_ang))
ax = 0.0
ay = - ((g_const))

flytime = (2.0 * v0y) / (-ay)
dis = flytime * v0x
th = v0y / - ay
max_y = ((v0y) ** 2.0 / (2.0 * -ay) + (y0))

print "Max height is"
print max_y, "meters"
print "Total distance traveled is"
print dis, "meters"
print "object is in the air for"
print flytime, "secs"

analytic_y_plot_list = []
analytic_x_plot_list = []
def gen_analytic_y_plot_list(y0, v0y, ay, ts, v0x):
	t = 0.0
	while t <= flytime + ts:
		analytic_y_plot_list.append(y0 + v0y * t + (1.0 / 2.0) * (ay) * t ** 2)
		analytic_x_plot_list.append(v0x * t)
		t = t + ts
	return analytic_x_plot_list, analytic_y_plot_list

gen_analytic_y_plot_list(y0, v0y, ay, ts, v0x)

y = np.asarray(analytic_y_plot_list)
x = np.asarray(analytic_x_plot_list)


plt.plot(x, y)
plt.xlim(0.0, dis)
plt.ylim(0.0, max_y)

plt.xlabel(r"$x-position$")
plt.ylabel(r"$y-position$")
plt.show()




