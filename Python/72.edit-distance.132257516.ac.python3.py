#
# [72] Edit Distance
#
# https://leetcode.com/problems/edit-distance/description/
#
# algorithms
# Hard (32.54%)
# Total Accepted:    114.4K
# Total Submissions: 351.6K
# Testcase Example:  '""\n""'
#
# 
# Given two words word1 and word2, find the minimum number of steps required to
# convert word1 to word2. (each operation is counted as 1 step.)
# 
# 
# 
# You have the following 3 operations permitted on a word:
# 
# 
# 
# a) Insert a character
# b) Delete a character
# c) Replace a character
# 
#
class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        mat = [[0 for j in range(n + 1)] for i in range(m + 1)]
        for i in range(1, m + 1):
            mat[i][0] = i
        for j in range(1, n + 1):
            mat[0][j] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    mat[i][j] = mat[i - 1][j - 1]
                else:
                    mat[i][j] = min(mat[i][j - 1], mat[i - 1][j], mat[i - 1][j - 1]) + 1
        print(mat)
        return mat[m][n]
