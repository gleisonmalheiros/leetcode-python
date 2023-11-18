import unittest
from two_sum import TwoSum


class TestTwoSum(unittest.TestCase):

    def test_case1(self):
        nums = [2, 7, 11, 13]
        target = 9
        actual = TwoSum.two_sum(nums, target)
        expected = [0, 1]
        self.assertEqual(expected, actual)

    def test_case2(self):
        nums = [3, 2, 4]
        target = 6
        actual = TwoSum.two_sum(nums, target)
        expected = [1, 2]
        self.assertEqual(expected, actual)

    def test_case3(self):
        nums = [3, 3]
        target = 6
        actual = TwoSum.two_sum(nums, target)
        expected = [0, 1]
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
