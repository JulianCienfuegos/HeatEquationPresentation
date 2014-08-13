from Euler2DFuncBC import *
from numpy import *
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt

set_printoptions(precision=3, suppress = True) # This is how to adjust the print options  for ndarrays in numpy.
number = 11
x = linspace(-pi/2, pi/2, number)
dx = x[1] - x[0]
num_unknowns = len(x) - 2
y = linspace(-pi/2, pi/2,  number) 
X, Y = meshgrid(x, y)
t0 = 0
f = lambda x, y, t: 10*e**(-2*t)*(sin(y)*sin(x)) + 2
U0 = f(X, Y, t0) # Our initial condition
U = U0
t = t0
dt = 0.1*(2*dx**2)
finaltime = 5
nr_times = int(finaltime/dt)

for i in range(nr_times):
	U, t = Euler2DFuncBC(U, dx, dt, 1, num_unknowns, t, f, x, y)


# Plot the figure
fig = plt.figure()

ax = fig.gca(projection='3d', xlim=(-pi/2,pi/2), ylim=(-pi/2,pi/2), zlim=(0, 10))
ax.plot_surface(X, Y, U, rstride=1, cstride=1, cmap=cm.coolwarm,
        linewidth=0, antialiased=False)      
plt.show()

#Let's see how good we did.
print amax(absolute(subtract(U, f(X,Y, t))))
