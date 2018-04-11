#
# [6] ZigZag Conversion
#
# https://leetcode.com/problems/zigzag-conversion/description/
#
# algorithms
# Medium (27.29%)
# Total Accepted:    204.8K
# Total Submissions: 750.5K
# Testcase Example:  '"PAYPALISHIRING"\n3'
#
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
# of rows like this: (you may want to display this pattern in a fixed font for
# better legibility)
# 
# 
# P   A   H   N
# A P L S I I G
# Y   I   R
# 
# 
# And then read line by line: "PAHNAPLSIIGYIR"
# 
# 
# 
# Write the code that will take a string and make this conversion given a
# number of rows:
# 
# 
# string convert(string text, int nRows);
# 
# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
# 
# 
# 
#
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        result = ''
        clicklen = numRows * 2 - 2
        s = s + (clicklen - (len(s) % clicklen - 1)) * '*'
        for jj in range(numRows):
            for ii in range(0, len(s), clicklen):
                if ii - jj >= 0:
                    result = result + s[ii - jj]
                if ii + jj < len(s) and jj != 0 and jj != numRows - 1:
                    result =  result + s[ii + jj]
        return result.replace('*', '')
