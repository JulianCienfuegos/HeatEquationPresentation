from numpy import e, linspace, pi, vectorize, sin
#from math import sin
from EulerHeatConstBC import *
from matplotlib import animation, pyplot as plt

 # Here we set some variables
x = linspace(-pi, pi, 20)
f = lambda x, t: e**(-t)*sin(x) + 2 # An "anonymous function".
#F = vectorize(f) # Makes a function work on a vector of values.
t0 = 0
dx = x[1] - x[0]
r = .49 # This can be as high as 0.5.
dt = r*(dx**2)
u0 = f(x, t0)
u = u0
time = t0
finaltime = 2.0

# Set up the figure
fig = plt.figure()
ax = plt.axes(xlim=(-pi, pi), ylim=(1,3))
ax.set_title('Euler Heat Equation Solver Demo', color = 'black')
ax.set_xlabel('X')
ax.set_ylabel('u(x,t) = Temperature')
line, = ax.plot([], [], lw=3) # initialize the line and give it a thickness
time_label = ax.text(0.05, 0.90, '', transform=ax.transAxes) # initialize the time label for the graph

# Initialization function
def init():
    time_label.set_text('')
    line.set_data([], [])
    return line, time_label
    
# Animation function.  
def update(i):
	global u, time # Necessary. 
	nr_times = 1
	u, time = EulerHeatConstBC(u, x, dt, nr_times, time)
	time_label.set_text('time = %.3f' % time) # Display the current time to the accuracy of your liking.
	line.set_data(x, u) # Set the data in the line
	return line, time_label
    
# Start the animation.
HeatAnimation = animation.FuncAnimation(fig, update, frames = int(finaltime/dt), interval = 10,  init_func=init, blit = True, repeat=False)
#anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

# Show the animation
plt.show()

# Let's see how we did!
print max(abs(u - f(x, time))) #  Print out the error in the numerical method.
