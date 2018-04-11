#
# [17] Letter Combinations of a Phone Number
#
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
#
# algorithms
# Medium (36.45%)
# Total Accepted:    229.2K
# Total Submissions: 628.8K
# Testcase Example:  '"23"'
#
# Given a digit string, return all possible letter combinations that the number
# could represent.
# 
# A mapping of digit to letters (just like on the telephone buttons) is given
# below.
# 
# 
# 
# 
# Input:Digit string "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# 
# 
# Note:
# Although the above answer is in lexicographical order, your answer could be
# in any order you want.
# 
#
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}
        res = []
        if not digits:
            return []
        for ii in mapping[digits[0]]:
            res.append(ii)
        for ii in digits[1:]:
            temp = []
            for jj in res:
                for kk in mapping[ii]:
                    temp.append(jj + kk)
            res = temp
        return res
