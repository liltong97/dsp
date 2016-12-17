# Matrix Algebra
import numpy as np

A = np.matrix([[1, 2, 3], [2, 7, 4]])
B = np.matrix([[1, -1], [0, 1]])
C = np.matrix([[5, -1], [9, 1], [6, 0]])
D = np.matrix([[3, -2, -1], [1, 2, 3]])
u = np.array([6, 2, -3, 5])
v = np.array([3, 5, -1, 4])
w = np.matrix([[1], [8], [0], [5]])

# 1. Matrix Dimensions
print('1.1')
print np.shape(A)
print('1.2')
print np.shape(B)
print('1.3')
print np.shape(C)
print('1.4')
print np.shape(D)
print('1.5')
print np.shape(u)
print('1.6')
print np.shape(w)

#2 Vector Operations
alpha = 6
print('2.1')
print u + v
print('2.2')
print u - v
print('2.3')
print alpha * u
print('2.4')
print np.dot(u, v)
print('2.5')
print np.linalg.norm(u)

#3 Matrix Operations
print('3.1')
#print A + C wrong dimensions
print('3.2')
print A - np.transpose(C)
print('3.3')
print np.transpose(C) + 3*D
print('3.4')
print B * A
print('3.5')
# print B * np.transpose(A) wrong dimensions


