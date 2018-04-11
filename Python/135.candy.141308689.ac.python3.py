#
# [135] Candy
#
# https://leetcode.com/problems/candy/description/
#
# algorithms
# Hard (25.27%)
# Total Accepted:    77.7K
# Total Submissions: 307.6K
# Testcase Example:  '[0]'
#
# 
# There are N children standing in a line. Each child is assigned a rating
# value. 
# 
# 
# You are giving candies to these children subjected to the following
# requirements:
# 
# 
# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# 
# 
# What is the minimum candies you must give?
# 
#
class Solution:
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        if n <= 1:
            return n
        # initial state: each kid gets one candy    
        nums = [1] * n
        # kids on upwards curve get candies
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                nums[i] = nums[i-1] + 1
        # kids on downwards curve get candies
        # if a kid on both up/down curves, i.e. a peak or a valley
        # kid gets the maximum candies among the two.
        for i in range(n-1, 0, -1):
            if ratings[i-1] > ratings[i]:
                nums[i-1] = max(nums[i]+1, nums[i-1])
        return sum(nums)
