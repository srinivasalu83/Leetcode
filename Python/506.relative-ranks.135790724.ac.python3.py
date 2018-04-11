#
# [506] Relative Ranks
#
# https://leetcode.com/problems/relative-ranks/description/
#
# algorithms
# Easy (46.87%)
# Total Accepted:    29.2K
# Total Submissions: 62.3K
# Testcase Example:  '[5,4,3,2,1]'
#
# 
# Given scores of N athletes, find their relative ranks and the people with the
# top three highest scores, who will be awarded medals: "Gold Medal", "Silver
# Medal" and "Bronze Medal".
# 
# Example 1:
# 
# Input: [5, 4, 3, 2, 1]
# Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
# Explanation: The first three athletes got the top three highest scores, so
# they got "Gold Medal", "Silver Medal" and "Bronze Medal". For the left two
# athletes, you just need to output their relative ranks according to their
# scores.
# 
# 
# 
# Note:
# 
# N is a positive integer and won't exceed 10,000.
# All the scores of athletes are guaranteed to be unique.
# 
# 
# 
#
class Solution:
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        record = []
        for ind, score in enumerate(nums):
            record.append([score, ind])
        record.sort(reverse=True)
        for rank in range(len(nums)):
            score, ind = record[rank]
            if rank >= 3:
                nums[ind] = str(rank + 1)
            elif rank == 0:
                nums[ind] = "Gold Medal"
            elif rank == 1:
                nums[ind] = "Silver Medal"
            else:
                nums[ind] = "Bronze Medal"
        return nums
