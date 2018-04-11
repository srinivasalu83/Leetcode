#
# [65] Valid Number
#
# https://leetcode.com/problems/valid-number/description/
#
# algorithms
# Hard (12.94%)
# Total Accepted:    84.1K
# Total Submissions: 650K
# Testcase Example:  '"0"'
#
# Validate if a given string is numeric.
# 
# Some examples:
# "0" => true
# " 0.1 " => true
# "abc" => false
# "1 a" => false
# "2e10" => true
# 
# Note: It is intended for the problem statement to be ambiguous. You should
# gather all requirements up front before implementing one.
# 
# Update (2015-02-10):
# The signature of the C++ function had been updated. If you still see your
# function signature accepts a const char * argument, please click the reload
# button to reset your code definition.
# 
#
class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #define a DFA
        state = [{}, 
                 {'blank': 1, 'sign': 2, 'digit':3, '.':4}, 
                 {'digit':3, '.':4},
                 {'digit':3, '.':5, 'e':6, 'blank':9},
                 {'digit':5},
                 {'digit':5, 'e':6, 'blank':9},
                 {'sign':7, 'digit':8},
                 {'digit':8},
                 {'digit':8, 'blank':9},
                 {'blank':9}]
        currentState = 1
        for c in s:
            if c >= '0' and c <= '9':
                c = 'digit'
            if c == ' ':
                c = 'blank'
            if c in ['+', '-']:
                c = 'sign'
            if c not in state[currentState].keys():
                return False
            currentState = state[currentState][c]
        if currentState not in [3,5,8,9]:
            return False
        return True
