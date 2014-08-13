from scipy.sparse import spdiags
from numpy import array, dot, diag, zeros, ones, vstack

# Here are the important functions
def EulerHeatConstBCSparse(u0, x, dt, nr_times, t0):
	""" This function solves the heat equation :
			u_t = u_xx
	by using the Euler method. The function takes 
	an initial condition u0, a domain  x, 
	a time step dt, the number of times to run the loop, 
	and the initial time, t0, as input.
	"""
	# Important Constants, etc.
	time = t0
	dx = x[1] - x[0]
	numUnknowns = len(u0) - 2
	r = dt/(dx**2) # Exponents are done with a double asterisk in python
	mainDiagonal = -2*ones(numUnknowns)
	offDiagonal = ones(numUnknowns)
	T = MakeTridiagonalMatrix(mainDiagonal, offDiagonal) # We could consider a better place to make T to make the code faster.
	u = u0
	
	# Make the boundary condition vector
	BoundaryConditions = zeros(numUnknowns)
	BoundaryConditions[0] = u0[0]
	BoundaryConditions[-1] = u0[-1]
	
	# Loop to perform the calculations
	for step in range(nr_times):
		u[1:-1] = u[1:-1] + r*T*u[1:-1] + r*BoundaryConditions 
		time = time + dt # We could reconsider how to do this to minimze rounding errors.
	
	# Return what we want
	return u, time
	
def MakeTridiagonalMatrix(main, offset_one):
	"""This function will make a tridiagonal 2D matrix
	which has the main array on its main diagonal and the offset_one 
	array on its super and sub diagonals.
	"""
	size = len(main)
	offsets = [0,1,-1]
	data = vstack((main, offset_one, offset_one))
	A = spdiags(data, offsets, size, size)
	return A
