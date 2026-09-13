import numpy as np

A = np.array([[2, 3, 1],
              [1, 2, 4],
              [3, 1, 2]])

B = np.array([[4, 2, 1],
              [2, 3, 2],
              [1, 2, 5]])

# Inverse of A
A_inv = np.linalg.inv(A)
print("Inverse of A:")
print(A_inv)

# Determinant of B
det_B = np.linalg.det(B)
print("\nDeterminant of B:")
print(det_B)

# A × A^-1
result = np.dot(A, A_inv)
print("\nA × A^-1:")
print(result)