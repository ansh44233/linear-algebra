"""
Linear algebra operations implemented from scratch in pure Python.
Written by Ansh.
"""

def add(A, B):
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] + B[i][j])
        result.append(row)
    return result


def sub(A, B):
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] - B[i][j])
        result.append(row)
    return result


def scaler_multiple(A, Number):
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] * Number)
        result.append(row)
    return result


# alias with standard spelling
def scalar_multiply(A, number):
    return scaler_multiple(A, number)


def multiplication(A, B):
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            total = 0
            for k in range(len(B)):
                total += A[i][k] * B[k][j]
            row.append(total)
        result.append(row)
    return result


def transpose(A):
    result = []
    for j in range(len(A[0])):
        row = []
        for i in range(len(A)):
            row.append(A[i][j])
        result.append(row)
    return result


def identity(n):
    result = []
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(1)
            else:
                row.append(0)
        result.append(row)
    return result


def determinant(A):
    # calculate determinant for 2x2 and 3x3 matrices
    n = len(A)
    if n == 1:
        return A[0][0]
    if n == 2:
        return (A[0][0] * A[1][1]) - (A[0][1] * A[1][0])
    
    det = 0
    for j in range(n):
        submatrix = [row[:j] + row[j+1:] for row in A[1:]]
        det += ((-1) ** j) * A[0][j] * determinant(submatrix)
    return det


def print_matrix(M, title=""):
    if title:
        print(f"[{title}]")
    for row in M:
        print(" ", row)
    print()
