#
# [96] Unique Binary Search Trees
#
# https://leetcode.com/problems/unique-binary-search-trees/description/
#
# algorithms
# Medium (41.91%)
# Total Accepted:    147.7K
# Total Submissions: 352.3K
# Testcase Example:  '3'
#
# Given n, how many structurally unique BST's (binary search trees) that store
# values 1...n?
# 
# For example,
# Given n = 3, there are a total of 5 unique BST's.
# 
# 
# ⁠  1         3     3      2      1
# ⁠   \       /     /      / \      \
# ⁠    3     2     1      1   3      2
# ⁠   /     /       \                 \
# ⁠  2     1         2                 3
# 
# 
# 
# 
#
class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        total = [0 for i in range(n + 1)]
        total[0] = total[1] = 1
        for i in range(2, n + 1):
            for j in range(0, i):
                total[i] += total[j] * total[i - j - 1]
        print(total)
        return total[-1]
