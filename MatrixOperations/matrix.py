import numpy as np
'''
Created on Jun 16, 2019

@author: adnan
'''

def matrixmultiplication(mat1, mat2):
    return np.dot(mat1, mat2)


print(matrixmultiplication(np.array([[7, 2, 9], [8, 3, 1], [5, 2, 8]]), np.array([[2, 9, 1], [3, 1, 5], [7, 2, 1]])))
print(matrixmultiplication(np.array([[1, 3], [2, 4], [0, 5]]), np.array([[1, 0], [2, 3]])))
u = np.array([[3],[-5],[4]])
v = np.array([[1],[2],[5]])
print(v)
print(u)
print(u.transpose() * v)
