#
# [190] Reverse Bits
#
# https://leetcode.com/problems/reverse-bits/description/
#
# algorithms
# Easy (29.37%)
# Total Accepted:    131.4K
# Total Submissions: 447.2K
# Testcase Example:  '           0 (00000000000000000000000000000000)'
#
# Reverse bits of a given 32 bits unsigned integer.
# 
# For example, given input 43261596 (represented in binary as
# 00000010100101000001111010011100), return 964176192 (represented in binary as
# 00111001011110000010100101000000).
# 
# 
# Follow up:
# If this function is called many times, how would you optimize it?
# 
# 
# Related problem: Reverse Integer
# 
# Credits:Special thanks to @ts for adding this problem and creating all test
# cases.
#
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        binn = bin(n)[2::]
        reversed_bin = '0' * (32 - len(binn)) + binn
        return int(reversed_bin[::-1], 2)
