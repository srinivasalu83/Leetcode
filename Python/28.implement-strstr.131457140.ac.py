#
# [28] Implement strStr()
#
# https://leetcode.com/problems/implement-strstr/description/
#
# algorithms
# Easy (28.95%)
# Total Accepted:    264K
# Total Submissions: 912K
# Testcase Example:  '"hello"\n"ll"'
#
# 
# Implement strStr().
# 
# 
# 
# Return the index of the first occurrence of needle in haystack, or -1 if
# needle is not part of haystack.
# 
# 
# Example 1:
# 
# Input: haystack = "hello", needle = "ll"
# Output: 2
# 
# 
# 
# Example 2:
# 
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
# 
# 
#
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return self.search(haystack, needle)
        
    def partial(self, pattern):
        """ Calculate partial match table: String -> [Int]"""
        ret = [0]
        
        for i in range(1, len(pattern)):
            j = ret[i - 1]
            while j > 0 and pattern[j] != pattern[i]:
                j = ret[j - 1]
            ret.append(j + 1 if pattern[j] == pattern[i] else j)
        return ret
        
    def search(self, T, P):
        """ 
        KMP search main algorithm: String -> String -> [Int] 
        Return all the matching position of pattern string P in S
        """
        if P == "":
            return 0
        
        partial, j = self.partial(P), 0
        
        for i in range(len(T)):
            while j > 0 and T[i] != P[j]:
                j = partial[j - 1]
            if T[i] == P[j]: j += 1
            if j == len(P): 
                return i - (j - 1)
            
        return -1
