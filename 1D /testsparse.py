import scipy.sparse as sp
import numpy as np
from time import time

########################################################################
#
# Our matrix is going to be size x size. Our vector is going to be size x 1
#
########################################################################

size = 10

########################################################################
# 
# Try the multiplication with a numpy array and a scipy sparse matrix.
#
########################################################################

start = time()

data = np.arange(size)
data = np.vstack((data, data, data))
offsets = [0,1,-1]
A = sp.spdiags(data, offsets, size, size)
print A.todense()
B = np.arange(size)
C = A * B

elapsed = (time() - start)
print "Sparse Time: " + str(elapsed)

########################################################################
#
# Try the multiplication with two numpy arrays.A = spdiags(x, offsets, m, n)
#
########################################################################

def MakeTridiagonalMatrix(main, offset_one, offset_minus_one):
	"""This function will make a tridiagonal 2D array (NOT a matrix)
	which has the main array on its main diagonal and the offset_one 
	array on its super and sub diagonals.
	"""
	return np.diag(main) + np.diag(offset_minus_one, k = -1) + np.diag(offset_one, k = 1)

start2 = time()

data2 = np.arange(size)
A2 = MakeTridiagonalMatrix(data2, data2[1:], data2[:-1])
B2 = np.arange(size)
C2 = np.dot(A2, B2)

elapsed2 = (time() - start2)
print "Array Time: " + str(elapsed2)


########################################################################
#
# Are the two results equal?
#
########################################################################

print 'Are the products equal? ' + str(np.array_equal(C, C2))
