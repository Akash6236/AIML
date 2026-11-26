# Program 1(f): NumPy Matrix Operations

import numpy as np

A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

B = np.array([[9, 8, 7],
              [6, 5, 4],
              [3, 2, 1]])

print("Matrix A:\n", A)
print("Matrix B:\n", B)

print("\nAddition:\n", A + B)
print("\nSubtraction:\n", A - B)
print("\nMatrix Multiplication:\n", A @ B)
print("\nTranspose of A:\n", A.T)
print("\nDeterminant of A:", np.linalg.det(A))
