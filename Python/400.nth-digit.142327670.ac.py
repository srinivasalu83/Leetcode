#
# [400] Nth Digit
#
# https://leetcode.com/problems/nth-digit/description/
#
# algorithms
# Easy (30.16%)
# Total Accepted:    33.9K
# Total Submissions: 112.3K
# Testcase Example:  '3'
#
# Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8,
# 9, 10, 11, ... 
# 
# Note:
# n is positive and will fit within the range of a 32-bit signed integer (n <
# 231).
# 
# 
# Example 1:
# 
# Input:
# 3
# 
# Output:
# 3
# 
# 
# 
# Example 2:
# 
# Input:
# 11
# 
# Output:
# 0
# 
# Explanation:
# The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0,
# which is part of the number 10.
# 
# 
#
class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 0
        num = 0
        while True:
            nine = 9 * (10 ** i)
            nextt = n - nine * (i + 1)
            if nextt > 0:
                n = nextt
                num += nine
                i += 1
            else:
                digit_ind = n % (i + 1)
                num += (n - 1) // (i + 1) + 1
                print(n, i, num, digit_ind)
                return int(list(str(num))[digit_ind - 1])
