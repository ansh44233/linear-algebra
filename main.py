from linear_algebra.matrix import (
    add,
    sub,
    scaler_multiple,
    multiplication,
    transpose,
    identity,
    determinant,
    print_matrix
)

# matrices to test operations
A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

print("--- Matrix Operations ---")

print_matrix(A, "Matrix A")
print_matrix(B, "Matrix B")

print("Addition (A + B):")
print_matrix(add(A, B))

print("Subtraction (A - B):")
print_matrix(sub(A, B))

print("Scalar Multiply (A * 2):")
print_matrix(scaler_multiple(A, 2))

print("Matrix Multiplication (A x B):")
print_matrix(multiplication(A, B))

print("Transpose of A:")
print_matrix(transpose(A))

print("Identity Matrix (3x3):")
print_matrix(identity(3))

print("Determinant of A:")
print(" det(A) =", determinant(A))
