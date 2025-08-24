# importation dependencies
from matplotlib import pyplot
import numpy as np
# GOAL: to simaltaneously create a linear, quadratic, cubic, logarithmic, log linear, exponential graph

#creating global variables
Xaxis = np.linspace(0,5,100)
YLineValues = np.linspace(0,5,100)
"""
- linspace creates 100 values in between 0,5.
- the Xaxis variable is the x values that remain fixed.
- The YLineValues are used to create the baseline of y values, but will show linear, quadratic, cubic, logarithmic, log linear, exponential graph.
"""
# creating the different y values
quad_values = Xaxis * Xaxis
cubic_values = Xaxis * Xaxis * Xaxis
log_values = np.log(Xaxis)
natural_log_values = log_values * Xaxis
exponential_values = 2 ** Xaxis
# plotting the different values in one graph
pyplot.plot(Xaxis,quad_values, label = 'quadratic')
pyplot.plot(Xaxis,cubic_values, label = 'cubic')
pyplot.plot(Xaxis,log_values, label = 'logarithmic')
pyplot.plot(Xaxis,natural_log_values, label = 'nlogarithmic')
pyplot.plot(Xaxis,exponential_values, label = 'exponential')
# now setting up the graph

pyplot.legend()
# shows the lines that are drawn by label eg for the exponential y values
pyplot.title('Rates of growth')
pyplot.xlabel('x values')
pyplot.ylabel('y values')
pyplot.show()