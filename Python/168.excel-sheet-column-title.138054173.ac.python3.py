#
# [168] Excel Sheet Column Title
#
# https://leetcode.com/problems/excel-sheet-column-title/description/
#
# algorithms
# Easy (27.30%)
# Total Accepted:    133.6K
# Total Submissions: 489.4K
# Testcase Example:  '1'
#
# Given a positive integer, return its corresponding column title as appear in
# an Excel sheet.
# 
# For example:
# 
# ⁠   1 -> A
# ⁠   2 -> B
# ⁠   3 -> C
# ⁠   ...
# ⁠   26 -> Z
# ⁠   27 -> AA
# ⁠   28 -> AB 
# 
# Credits:Special thanks to @ifanchu for adding this problem and creating all
# test cases.
#
from math import log

class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        cap_map = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        result = []
        while n > 0:
            result.append(cap_map[(n - 1) % 26])
            n = (n - 1) // 26
        return "".join(reversed(result))
