#
# [171] Excel Sheet Column Number
#
# https://leetcode.com/problems/excel-sheet-column-number/description/
#
# algorithms
# Easy (48.51%)
# Total Accepted:    164.6K
# Total Submissions: 339.4K
# Testcase Example:  '"A"'
#
# Related to question Excel Sheet Column Title
# Given a column title as appear in an Excel sheet, return its corresponding
# column number.
# 
# For example:
# ⁠   A -> 1
# ⁠   B -> 2
# ⁠   C -> 3
# ⁠   ...
# ⁠   Z -> 26
# ⁠   AA -> 27
# ⁠   AB -> 28 
# 
# Credits:Special thanks to @ts for adding this problem and creating all test
# cases.
#
class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        base = ord('A') - 1
        for i, c in enumerate(s):
            res = res * 26 + ord(c) - base
            # print(ord(c) - base, res)
        return res
