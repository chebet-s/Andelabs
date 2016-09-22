from unittest import TestCase
from primechecker import PrimeChecker

class PrimeNumberTest(TestCase):
    """docstring for PrimeNumberTest"""

    def test_object_type(self):
        obj = PrimeChecker()
        self.assertEqual(True, type(obj) is PrimeChecker,
                         msg='should be of type `PrimeChecker`')

    def test_obj_instance(self):
        obj = PrimeChecker()
        self.assertIsInstance(obj,
                              PrimeChecker,
                              msg='should be an instance of `PrimeChecker`')

    def test_is_prime_one(self):
        prime = PrimeChecker('41')
        self.assertEqual(True,
                         prime.is_prime(),
                         msg='should return true for 41')

    def test_is_prime_two(self):
        prime = PrimeChecker('101')
        self.assertEqual(True,
                         prime.is_prime(),
                         msg='should return true for 101')

    def test_is_prime_three(self):
        prime = PrimeChecker('67')
        self.assertEqual(True,
                         prime.is_prime(),
                         msg='should return false for 68')

    def test_is_prime_four(self):
        prime = PrimeChecker('3')
        self.assertEqual(True,
                         prime.is_prime(),
                         msg='should return true for 41')

    def test_is_prime_five(self):
        prime = PrimeChecker('')
        self.assertEqual(False,
                         prime.is_prime(),
                         msg='should return false for ""')