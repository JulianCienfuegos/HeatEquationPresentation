from numpy import e, linspace, pi, vectorize, sin
from EulerHeatConstBC import *
from matplotlib import animation, pyplot as plt

 # Here we set some variables
x = linspace(0, pi, 10)
f = lambda x, t: e**(-t)*sin(x) + 2
#F = vectorize(f)
t0 = 0
dx = x[1] - x[0]
r = .49
dt = r*(dx**2)
u0 = f(x, t0)
u = u0
time = t0

# Set up the figure
fig = plt.figure()
ax = plt.axes(xlim=(0, pi), ylim=(2,3))
ax.set_title('2D Test', color = 'black')
ax.set_axis_bgcolor('yellow')
ax.set_xlabel('X')
ax.set_ylabel('u(x,t) = Temperature')
line, = ax.plot([], [], lw=1)
for i in range(100): 
	nr_times = 1
	u, time = EulerHeatConstBC(u, x, dt, nr_times, time)
	line.set_data(x, u)
	plt.savefig(str("{0:03}".format(i))+'.png')

