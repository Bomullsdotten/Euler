
from __future__ import absolute_import
import unittest


class MyTestCase(unittest.TestCase):
    def test_9_is_multiple_of_3(self):
        from Multiples_of_x.multiple_of_x import multiple_of_x

        result = multiple_of_x(9, 3)
        self.assertTrue(result)

    def test_5_is_not_a_denominator_of_3(self):
        from Multiples_of_x.multiple_of_x import multiple_of_x
        result = multiple_of_x(5,4)
        self.assertFalse(result)

    def test_numbers_multiples_of_3_in_range_10(self):
        from Multiples_of_x.multiple_of_x import multiples_in_range

        result = multiples_in_range(10, 3)
        answer = [3,6,9]
        self.assertListEqual(result, answer)

    def test_numbers_multiples_of_4_in_range_12(self):
        from Multiples_of_x.multiple_of_x import multiples_in_range

        result = multiples_in_range(12, 4)
        answer = [4,8]
        self.assertListEqual(result, answer)

    def test_number_multiples_of_xy_in_range_z(self):
        from Multiples_of_x.multiple_of_x import multiples_in_range

        result = multiples_in_range(10, 3, 5)
        answer = [3,5,6,9]
        self.assertListEqual(result, answer)

    def test_multiples_in_range_returns_unique_list(self):
        from Multiples_of_x.multiple_of_x import multiples_in_range

        result = multiples_in_range(4, 1,2)
        answer = [1, 2, 3]
        self.assertEqual(result, answer)


    def test_sum_multiples_of_xy_in_range_z(self):
        from Multiples_of_x.multiple_of_x import sum_multiples_in_range

        result = sum_multiples_in_range(10, 3, 5)
        answer = 23
        self.assertEqual(result, answer)


if __name__ == '__main__':
    unittest.main()
