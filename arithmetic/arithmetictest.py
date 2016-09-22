from unittest import TestCase
from arithmetic import arith_geo

class ArithmeticProgressionTest(TestCase):

    """docstring for ArithmeticProgressionTest"""

    def test_empty_list(self):
        self.assertEqual(0, arith_geo([]),
                         msg='should return 0 for an empty array')

    def test_is_positive_arithematic_progression_one(self):
        self.assertEqual(
            'Arithmetic', arith_geo([2, 4, 6, 8, 10]),
            msg='should return `Arithmetic` for [2, 4, 6, 8, 10]')

    def test_is_positive_arithematic_progression_two(self):
        self.assertEqual(
            'Arithmetic',
            arith_geo([5, 11, 17, 23, 29, 35, 41]),
            msg='should return `Arithmetic` for [5, 11, 17, 23, 29, 35, 41]'
        )

    def test_is_negative_arithematic_progression(self):
        self.assertEqual(
            'Arithmetic',
            arith_geo([15, 10, 5, 0, -5, -10]),
            msg='should return `Arithmetic` for [15, 10, 5, 0, -5, -10]'
        )


class GeometricProgressionTest(TestCase):

    """docstring for GeometricProgressionTest"""

    def test_is_positive_geometric_progression_one(self):
        self.assertEqual(
            'Geometric',
            arith_geo([2, 6, 18, 54, 162]),
            msg='should return `Geometric` for [2, 6, 18, 54, 162]'
        )

    def test_is_positive_geometric_progression_two(self):
        self.assertEqual(
            'Geometric',
            arith_geo([0.5, 3.5, 24.5, 171.5]),
            msg='should return `Geometric` for [0.5, 3.5, 24.5, 171.5]'
        )

    def test_is_negative_geometric_progression_two(self):
        self.assertEqual(
            'Geometric',
            arith_geo([-128, 64, -32, 16, -8]),
            msg='should return `Geometric` for [-128, 64, -32, 16, -8]'
        )


class SimpleProgressionTest(TestCase):

    """docstring for GeometricProgressionTest"""

    def test_is_positive_ordinary_progression_one(self):
        self.assertEqual(-1,
                         arith_geo([1, 2, 3, 5, 8]),
                         msg='should return -1 for [1, 2, 3, 5, 8]'
                         )

    def test_is_positive_ordinary_progression_two(self):
        self.assertEqual(-1,
                         arith_geo([1, 3, 6, 10, 15]),
                         msg='should return -1 for [1, 3, 6, 10, 15]'
                         )

    def test_is_negative_ordinary_progression(self):
        self.assertEqual(
            -1,
            arith_geo([-1, -8, -27, -64, -125]),
            msg='should return -1 for [-1, -8, -27, -64, -125]'
        )

