from numpy import e, linspace, pi, vectorize
from math import sin
from EulerHeatFunctionBoundary import *
from matplotlib import animation, pyplot as plt
from time import time

 # Here we set some variables
x = linspace(-pi/2, pi/2, 10)
f = lambda x, t: e**(-t)*sin(x) + 2 # An "anonymous function".
fl = lambda t: f(x[0], t)
fr = lambda t: f(x[-1], t)
F = vectorize(f) # Makes a function work on a vector of values.
t0 = 0
dx = x[1] - x[0]
r = .49 # This can be as high as 0.5.
dt = r*(dx**2)
u0 = F(x, t0)
u = u0
time = t0
finaltime = 6.0

# Set up the figure
fig = plt.figure()
ax = plt.axes(xlim=(-pi/2, pi/2), ylim=(1,3))
ax.set_title('Euler Heat Equation Solver Demo', color = 'black')
ax.set_xlabel('X')
ax.set_ylabel('u(x,t) = Temperature')
line, = ax.plot([], [], lw=2) # Initialize the line and give it a thickness
time_label = ax.text(0.05, 0.90, '', transform=ax.transAxes, fontsize=14) # initialize the time label for the graph
#The use of transform=ax.transAxes throughout the code indicates that the
#coordinates are given relative to the axes bounding box, with 0,0 being 
#the lower left of the axes and 1,1 the upper right.

# Initialization function
def init():
    time_label.set_text('')
    line.set_data([], [])
    return line, time_label
    
# Animation function.  
def update(i):
	global u, time # Necessary. 
	nr_times = 1
	u, time = EulerHeatFunctionBC(u, x, fl, fr, dt, nr_times, time)
	time_label.set_text('time = %.3f' % time) # Display the current time to the accuracy of your liking.
	line.set_data(x, u) # Set the data in the line
	return line, time_label
    
# Start the animation
HeatAnimation = animation.FuncAnimation(fig, update, frames = int(finaltime/dt), interval = 100,  init_func=init, blit = False, repeat=False)

plt.show()

print max(abs(u - F(x, time))) #  Print out the error in the numerical method.
