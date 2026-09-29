import numpy as np

A = np.array([[2, 3, 4],
              [5, 7, 6],
              [8, 9, 10]])

B = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

print("\nMatrix A")
print(A)

print("\nMatrix B")
print(B)

print("\nAddition")
print(A + B)

print("\nSubtraction")
print(A - B)

print("\nMultiplication")
print(A @ B)

print("\nTranspose")
print(A.T)

print("\nDeterminant")
print(np.linalg.det(A))
