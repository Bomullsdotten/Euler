from __future__ import absolute_import
import unittest


class MyTestCase(unittest.TestCase):
    def test_fibonacci_returns_fibonacci_number_x(self):
        from Even_fibonacci.fibonacci import fibonacci
        ten_first_fib = [1,1,2,3,5,8,13,21,34,55]
        result = fibonacci(1)
        self.assertEqual(result, ten_first_fib[0])
        result = fibonacci(2)
        self.assertEqual(result, ten_first_fib[1])
        result = fibonacci(5)
        self.assertEqual(result, ten_first_fib[4])

    def test_is_even(self):
        from Even_fibonacci.fibonacci import is_even
        result = is_even(14)
        self.assertTrue(result)
        result = is_even(13)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
