#
# [326] Power of Three
#
# https://leetcode.com/problems/power-of-three/description/
#
# algorithms
# Easy (40.73%)
# Total Accepted:    124K
# Total Submissions: 304.5K
# Testcase Example:  '27'
#
# 
# ⁠   Given an integer, write a function to determine if it is a power of
# three.
# 
# 
# ⁠   Follow up:
# ⁠   Could you do it without using any loop / recursion?
# 
# 
# Credits:Special thanks to @dietpepsi for adding this problem and creating all
# test cases.
#
class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and (1162261467 % n == 0)
