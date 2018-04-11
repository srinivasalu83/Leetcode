#
# [647] Palindromic Substrings
#
# https://leetcode.com/problems/palindromic-substrings/description/
#
# algorithms
# Medium (54.76%)
# Total Accepted:    37.2K
# Total Submissions: 68K
# Testcase Example:  '"abc"'
#
# 
# Given a string, your task is to count how many palindromic substrings in this
# string.
# 
# 
# 
# The substrings with different start indexes or end indexes are counted as
# different substrings even they consist of same characters. 
# 
# 
# Example 1:
# 
# Input: "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
# 
# 
# 
# Example 2:
# 
# Input: "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
# 
# 
# 
# Note:
# 
# The input string length won't exceed 1000.
# 
# 
#
class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        def manachers(S):
            A = '@#' + '#'.join(S) + '#$'
            Z = [0] * len(A)
            center = right = 0
            for i in range(1, len(A) - 1):
                if i < right:
                    Z[i] = min(right - i, Z[2 * center - i])
                while A[i + Z[i] + 1] == A[i - Z[i] - 1]:
                    Z[i] += 1
                if i + Z[i] > right:
                    center, right = i, i + Z[i]
            return Z

        return sum((v+1)//2 for v in manachers(s))
    
    
    '''
    def countSubstrings(self, S):
    N = len(S)
    ans = 0
    for center in xrange(2*N - 1):
        left = center / 2
        right = left + center % 2
        while left >= 0 and right < N and S[left] == S[right]:
            ans += 1
            left -= 1
            right += 1
    return ans
    '''
