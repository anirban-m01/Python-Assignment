import numpy as np

A = np.array([
    [2, 3],
    [4, 5]
])

# Constant matrix
B = np.array([8, 14])

solution = np.linalg.solve(A, B)

print("Value of x =", solution[0])
print("Value of y =", solution[1])


#car velocity


D = float(input("Enter distance between two points (km): "))

v1 = 3 * D / 4
v2 = D / 4

print("Velocity of Car 1 =", v1, "km/hr")
print("Velocity of Car 2 =", v2, "km/hr")




from scipy.linalg import matrix_rank

# Create 4x4 matrix
A = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [2, 4, 6, 8],
    [1, 3, 5, 7]
])

print("Original Matrix:")
print(A)

# Transpose
T = A.T

print("\nTranspose of Matrix:")
print(T)

# Rank
r = matrix_rank(A)

print("\nRank of Matrix:", r)



#iv.

from scipy.linalg import eig


A = np.array([
    [4, 1, 0, 0],
    [1, 4, 1, 0],
    [0, 1, 4, 1],
    [0, 0, 1, 4]
])

# Find eigenvalues and eigenvectors
eigenvalues, eigenvectors = eig(A)

print("Matrix:")
print(A)

print("\nEigenvalues:")
print(eigenvalues)

print("\nEigenvectors:")
print(eigenvectors)




#V. QR(), SVD() and LSTSQ()

from scipy.linalg import qr, svd

# Create a square matrix
A = np.array([
    [1, 2],
    [3, 4]
])

print("Original Matrix:")
print(A)

# 1. QR Decomposition
Q, R = qr(A)

print("\nQR Decomposition:")
print("Q =")
print(Q)

print("R =")
print(R)

# 2. SVD
U, S, Vt = svd(A)

print("\nSVD:")
print("U =")
print(U)

print("Singular Values =")
print(S)

print("Vt =")
print(Vt)

# 3. Least Square Solution
b = np.array([5, 11])

x, residuals, rank, s = np.linalg.lstsq(A, b, rcond=None)

print("\nLSTSQ Result:")
print("Solution =", x)
print("Residuals =", residuals)
print("Rank =", rank)