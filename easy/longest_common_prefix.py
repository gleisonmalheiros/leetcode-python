"""
#14
https://leetcode.com/problems/longest-common-prefix/description/

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
"""


class LongestCommonPrefix:
    @staticmethod
    def longest_common_prefix(strs: list[str]) -> str:
        res = ''

        if len(strs) > 0:
            res = strs[0] # first prefix is whole first word

            for i in range(1, len(strs)): # for each word after the first
                word = strs[i]

                if len(word) < len(res): # whichever smaller
                    res = res[0: len(word)]

                for j in range(len(res)):
                    if res[j] != word[j]:
                        if j == 0:
                            return ''
                        else:
                            res = res[0: j]
                            break

        return res
