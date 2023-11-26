"""
#20
https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.
- Every close bracket has a corresponding open bracket of the same type.
"""

from collections import deque


class ValidParentheses:
    @staticmethod
    def isValid(s: str) -> bool:
        llist = deque()

        for i in range(0, len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                llist.appendleft(s[i])
            elif len(llist) == 0:
                return False
            elif s[i] == ')':
                if llist.popleft() != '(':
                    return False
            elif s[i] == '}':
                if llist.popleft() != '{':
                    return False
            elif s[i] == ']':
                if llist.popleft() != '[':
                    return False
            else:
                return False

        return len(llist) == 0
