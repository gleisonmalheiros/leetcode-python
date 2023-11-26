from unittest import TestCase
from easy.longest_common_prefix import LongestCommonPrefix


class TestLongestCommonPrefix(TestCase):

    def test_longest_common_prefix1(self):
        words = ["flower", "flow", "flight"]
        self.assertEqual('fl', LongestCommonPrefix.longest_common_prefix(words))

    def test_longest_common_prefix2(self):
        words = ["dog", "racecar", "car"]
        self.assertEqual('', LongestCommonPrefix.longest_common_prefix(words))

    def test_longest_common_prefix3(self):
        words = ["undercook", "underestimate", "underwear", "underdog", "under"]
        self.assertEqual('under', LongestCommonPrefix.longest_common_prefix(words))
