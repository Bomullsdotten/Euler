from __future__ import absolute_import
import unittest


class MyTestCase(unittest.TestCase):
    def test_Eratoshenes_returns_primes_bellow_n(self):
        from primes import Eratosthenes
        n = 30
        result = Eratosthenes.primesTo(n)
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        self.assertListEqual(primes, result)



if __name__ == '__main__':
    unittest.main()
