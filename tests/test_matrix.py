import unittest
from linear_algebra import (
    add,
    sub,
    scalar_multiply,
    multiply,
    transpose,
    identity,
    determinant,
    trace,
)


class TestLinearAlgebra(unittest.TestCase):
    def setUp(self):
        self.A = [
            [1, 2],
            [3, 4]
        ]
        self.B = [
            [5, 6],
            [7, 8]
        ]

    def test_addition(self):
        result = add(self.A, self.B)
        self.assertEqual(result, [[6, 8], [10, 12]])

    def test_subtraction(self):
        result = sub(self.A, self.B)
        self.assertEqual(result, [[-4, -4], [-4, -4]])

    def test_scalar_multiply(self):
        result = scalar_multiply(self.A, 3)
        self.assertEqual(result, [[3, 6], [9, 12]])

    def test_matrix_multiply(self):
        # [1*5 + 2*7, 1*6 + 2*8] = [19, 22]
        # [3*5 + 4*7, 3*6 + 4*8] = [43, 50]
        result = multiply(self.A, self.B)
        self.assertEqual(result, [[19, 22], [43, 50]])

    def test_transpose(self):
        result = transpose(self.A)
        self.assertEqual(result, [[1, 3], [2, 4]])

    def test_identity(self):
        result = identity(2)
        self.assertEqual(result, [[1, 0], [0, 1]])

    def test_determinant_2x2(self):
        # 1*4 - 2*3 = -2
        self.assertEqual(determinant(self.A), -2)

    def test_determinant_3x3(self):
        C = [
            [6, 1, 1],
            [4, -2, 5],
            [2, 8, 7]
        ]
        # det = 6*(-14 - 40) - 1*(28 - 10) + 1*(32 - (-4))
        #     = 6*(-54) - 18 + 36 = -324 - 18 + 36 = -306
        self.assertEqual(determinant(C), -306)

    def test_trace(self):
        self.assertEqual(trace(self.A), 5)


if __name__ == "__main__":
    unittest.main()
