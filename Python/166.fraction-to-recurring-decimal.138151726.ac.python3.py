#
# [166] Fraction to Recurring Decimal
#
# https://leetcode.com/problems/fraction-to-recurring-decimal/description/
#
# algorithms
# Medium (18.10%)
# Total Accepted:    63.6K
# Total Submissions: 351.6K
# Testcase Example:  '1\n2'
#
# Given two integers representing the numerator and denominator of a fraction,
# return the fraction in string format.
# 
# If the fractional part is repeating, enclose the repeating part in
# parentheses.
# 
# For example,
# 
# 
# Given numerator = 1, denominator = 2, return "0.5".
# Given numerator = 2, denominator = 1, return "2".
# Given numerator = 2, denominator = 3, return "0.(6)".
# 
# 
# 
# 
# Credits:
# Special thanks to @Shangrila for adding this problem and creating all test
# cases.
# 
#
class Solution:
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        res = []
        n, d = numerator, denominator
        if n * d < 0:
            res.append('-')
        n, d = abs(n), abs(d)
        if n < d:
            res.append('0')
        while n >= d:
            res.append(str(n // d))
            n = n % d
        if n == 0:
            return ''.join(res)
        res.append('.')
        n *= 10
        record = {}
        while n != 0:
            if n in record:
                res.insert(record[n], '(')
                res.append(')')
                return ''.join(res)
            record[n] = len(res)
            nn = n
            while nn < d:
                res.append('0')
                nn *= 10
                record[nn] = len(res)
            res.append(str(nn // d))
            n = nn % d * 10
        return ''.join(res)
