from numpy import *

def Euler2DFuncBC(U0, dx, dt, nr_times, num_unknowns,t0, f, x, y):
	"""	This function solves 
	                u_t = u_xx + u_yy
	using the Forward Euler Method. The function takes
	an initial condition U0, a vector x, a time step dt, 
	the number of times to loop nr_times, and an initial
	time t0.
	"""
	N = len(U0[0])
	T = MakeDirichletMatrix(num_unknowns)
	u = MakeEulerVector(U0, N)
	r = dt/(dx**2)
	t = t0
	U = U0
	bc = MakeBCVector(N, f, x, y, t)
	for step in range(nr_times):
		u = u + r*(dot(T,u) + bc)
		t  = t + dt
		bc = MakeBCVector(N, f, x, y, t)
		# Make this into a function
		UpdateBoundary(U, N, f, x, y, t)
	U = MakeUpdatedEulerMatrix(U, u, N)
	return U, t

def UpdateBoundary(U, N, f, x, y, t):
	for i in range(N-2):
		U[0][i+1] = f(x[0], y[i+1], t)
		U[N-1][i+1] = f(x[N-1], y[i+1], t)
	for i in range(N-2):
		U[i+1][0] = f(x[i+1], y[0], t)
	for i in range(N-2):
		U[i+1][N-1] = f(x[i+1], y[N-1], t)
	U[N-1][N-1] = f(x[N-1], y[N-1], t)
	U[0][0] = f(x[0],y[0], t)
	U[0][N-1] = f(x[0], y[N-1], t)
	U[N-1][0] = f(x[N-1], y[0], t)

def MakeBCVector(N, f, x, y, t):
	"""This function make the boundary condition vector for the solver.
	"""
	bc = zeros((N-2)*(N-2))
	for i in range(N-2):
		bc[i*(N - 2)] = bc[i*(N - 2)] + f(x[0], y[i+1], t)
		bc[i*(N-2) + N-3] = bc[i*(N-2) + N-3] + f(x[N-1], y[i+1], t)
	for i in range(N-2): # Set the left boundary
		bc[i] = bc[i] + f(x[i+1], y[0], t) #U[i+1][0]
	for i in range(N-2): # Set the right boundary
		bc[(N-2)*(N-3) + i] =  bc[(N-2)*(N-3) + i] + f(x[i+1], y[N-1], t) 
	return bc

def MakeDirichletMatrix(N):
	"""This function makes the dirichlet matrix for the 2D 
	Forward Euler Method.
	"""
	main = -2*ones(N)
	offset_one = ones(N-1)
	A = MakeTridiagonalMatrix(main, offset_one)
	B = eye(N) # is a sparse matrix
	T = kron(A,B)+kron(B,A)
	return T
	
def MakeTridiagonalMatrix(main, offset_one):
	"""This function will make a tridiagonal 2D array (NOT a matrix)
	which has the main array on its main diagonal and the offset_one 
	array on its super and sub diagonals.
	"""
	return diag(main) + diag(offset_one, k = -1) + diag(offset_one, k = 1)
	
def MakeEulerVector(U, N):
	"""	This function takes the interior elements
	from a 2D numpy array and returns an array made 
	of these elements.
	"""
	u = []
	for i in range(N-2):
		u = concatenate((u, U[i+1][1:N-1]))
	return u

def MakeUpdatedEulerMatrix(U0, u, N):
	""" This function takes a vector of elements and 
	returns them to their position inside the original 
	meshgrid.
	"""
	U = U0
	for i in range(N-2):
		U[i+1][1:N-1] = u[i*(N-2):(i+1)*(N-2)] # Verify this
	return U
