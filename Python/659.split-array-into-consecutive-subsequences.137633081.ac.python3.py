#
# [659] Split Array into Consecutive Subsequences
#
# https://leetcode.com/problems/split-array-into-consecutive-subsequences/description/
#
# algorithms
# Medium (36.96%)
# Total Accepted:    7.9K
# Total Submissions: 21.4K
# Testcase Example:  '[1,2,3,3,4,5]'
#
# You are given an integer array sorted in ascending order (may contain
# duplicates), you need to split them into several subsequences, where each
# subsequences consist of at least 3 consecutive integers. Return whether you
# can make such a split.
# 
# Example 1:
# 
# Input: [1,2,3,3,4,5]
# Output: True
# Explanation:
# You can split them into two consecutive subsequences : 
# 1, 2, 3
# 3, 4, 5
# 
# 
# 
# Example 2:
# 
# Input: [1,2,3,3,4,4,5,5]
# Output: True
# Explanation:
# You can split them into two consecutive subsequences : 
# 1, 2, 3, 4, 5
# 3, 4, 5
# 
# 
# 
# Example 3:
# 
# Input: [1,2,3,4,4,5]
# Output: False
# 
# 
# 
# Note:
# 
# The length of the input is in range of [1, 10000]
# 
# 
#
from collections import Counter, defaultdict

class Solution:
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        freq = Counter(nums)
        tails = defaultdict(int)
        for v in nums:
            if freq[v] <= 0:
                continue
            elif tails[v] > 0:
                tails[v] -= 1
                tails[v + 1] += 1
                freq[v] -= 1
            elif freq[v + 1] > 0 and freq[v + 2] > 0:
                tails[v + 3] += 1
                freq[v] -= 1
                freq[v + 1] -= 1
                freq[v + 2] -= 1
            else:
                return False
        return True
