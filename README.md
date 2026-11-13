# Linear Algebra from Scratch (Pure Python)

A zero-dependency Python implementation of foundational linear algebra algorithms and matrix operations, written from first principles without relying on third-party numerical packages like NumPy.

I built this project during my college coursework to deeply understand how multidimensional array arithmetic, linear transformations, and recursive matrix algorithms operate under the hood using native data structures and explicit nested loops.

---

## Why from Scratch?

In modern Python development, it's common to run `import numpy as np` and invoke `np.dot()` or `np.linalg.det()` as black boxes. While highly optimized in C/BLAS for production, relying solely on high-level libraries hides the underlying algorithmic mechanics.

This project focuses on:
- **Algorithmic Clarity:** Understanding the step-by-step traversal, row-column dot products, and boundary conditions required for matrix operations.
- **Pure Python Execution:** Zero external C-bindings or package installations required; runs immediately on any standard Python 3 interpreter.
- **Foundational Computing:** Building mathematical intuition for graphics pipelines, game development maths, and machine learning primitives (forward-pass weights and bias additions).

---

## Supported Operations

| Operation | Function | Mathematical Definition | Time Complexity |
| :--- | :--- | :--- | :---: |
| **Matrix Addition** | `add(A, B)` | $C_{i,j} = A_{i,j} + B_{i,j}$ | $\mathcal{O}(m \cdot n)$ |
| **Matrix Subtraction** | `sub(A, B)` | $C_{i,j} = A_{i,j} - B_{i,j}$ | $\mathcal{O}(m \cdot n)$ |
| **Scalar Multiplication** | `scaler_multiple(A, k)` | $C_{i,j} = k \cdot A_{i,j}$ | $\mathcal{O}(m \cdot n)$ |
| **Matrix Multiplication** | `multiplication(A, B)` | $C_{i,j} = \sum_{k=1}^{p} A_{i,k} \cdot B_{k,j}$ | $\mathcal{O}(m \cdot p \cdot n)$ |
| **Transpose** | `transpose(A)` | $A^T_{j,i} = A_{i,j}$ | $\mathcal{O}(m \cdot n)$ |
| **Identity Matrix** | `identity(n)` | $I_{i,j} = 1 \text{ if } i = j \text{ else } 0$ | $\mathcal{O}(n^2)$ |
| **Determinant** | `determinant(A)` | $\det(A) = \sum_{j=1}^{n} (-1)^{1+j} a_{1,j} M_{1,j}$ | Recursive Laplace Expansion |

---

## Technical Implementation Details

### 1. Matrix Representation
Matrices are structured as standard 2D lists (lists of lists) in Python:
```python
# 2x2 Matrix
A = [
    [1, 2],
    [3, 4]
]
```

### 2. Matrix Multiplication
Implemented via the standard 3-nested-loop row-by-column inner product algorithm:
```python
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
```

### 3. Recursive Determinant (Laplace Expansion)
Computes the determinant for $2 \times 2$ matrices directly, and handles $n \times n$ matrices through recursive cofactor expansion along the first row:
```python
def determinant(A):
    n = len(A)
    if n == 1:
        return A[0][0]
    if n == 2:
        return (A[0][0] * A[1][1]) - (A[0][1] * A[1][0])
    
    det = 0
    for j in range(n):
        # Slice minor submatrix excluding row 0 and column j
        submatrix = [row[:j] + row[j+1:] for row in A[1:]]
        det += ((-1) ** j) * A[0][j] * determinant(submatrix)
    return det
```

---

## Getting Started

### Prerequisites
- Python 3.8 or higher (No third-party packages needed).

### Clone & Run

```bash
# Clone the repository
git clone https://github.com/ansh44233/linear-algebra.git
cd linear-algebra

# Run the test demonstration
python main.py
```

### Sample Output

```text
--- Matrix Operations ---
[Matrix A]
  [1, 2]
  [3, 4]

[Matrix B]
  [5, 6]
  [7, 8]

Addition (A + B):
  [6, 8]
  [10, 12]

Subtraction (A - B):
  [-4, -4]
  [-4, -4]

Scalar Multiply (A * 2):
  [2, 4]
  [6, 8]

Matrix Multiplication (A x B):
  [19, 22]
  [43, 50]

Transpose of A:
  [1, 3]
  [2, 4]

Identity Matrix (3x3):
  [1, 0, 0]
  [0, 1, 0]
  [0, 0, 1]

Determinant of A:
 det(A) = -2
```

---

## Project Structure

```
linear-algebra/
├── linear_algebra/
│   ├── __init__.py       # Package initializer
│   └── matrix.py         # Pure Python matrix operations & algorithms
├── main.py               # Demonstration script showing operations
├── LICENSE               # MIT License
└── README.md             # Project documentation & engineering notes
```

---

## Author

**Ansh**  
- GitHub: [@ansh44233](https://github.com/ansh44233)

## License

This project is licensed under the [MIT License](LICENSE).
