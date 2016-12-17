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
print np.shape(A) # 2,3
print('1.2')
print np.shape(B) # 2,2
print('1.3')
print np.shape(C) # 3,2
print('1.4')
print np.shape(D) # 2,3
print('1.5')
print np.shape(u) # 1,4
print('1.6')
print np.shape(w) # 4,1

#2 Vector Operations
alpha = 6
print('2.1')
print u + v  #[9 7 -4 9]
print('2.2')
print u - v  #[3 -3 -2 1]
print('2.3')
print alpha * u #[36 12 -18 30]
print('2.4')
print np.dot(u, v) #51
print('2.5')
print np.linalg.norm(u) # 8.602325

#3 Matrix Operations
print('3.1')
#print A + C wrong dimensions
print('3.2')
print A - np.transpose(C) # [[-4 -7 -3];[3 6 4]]
print('3.3')
print np.transpose(C) + 3*D #[[14 3 3];[2 7 9]]
print('3.4')
print B * A [[-1 -5 -1];[2 7 4]]
print('3.5')
# print B * np.transpose(A) wrong dimensions


