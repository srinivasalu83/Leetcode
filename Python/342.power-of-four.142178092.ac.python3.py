#
# [342] Power of Four
#
# https://leetcode.com/problems/power-of-four/description/
#
# algorithms
# Easy (39.13%)
# Total Accepted:    83.7K
# Total Submissions: 213.8K
# Testcase Example:  '16'
#
# 
# Given an integer (signed 32 bits), write a function to check whether it is a
# power of 4.
# 
# Example:
# Given num = 16, return true.
# Given num = 5, return false.
# 
# 
# Follow up: Could you solve it without loops/recursion?
# 
# Credits:Special thanks to @yukuairoy  for adding this problem and creating
# all test cases.
#
class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num & (num - 1) == 0 and num & 1431655765 != 0
