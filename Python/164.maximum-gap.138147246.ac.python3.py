#
# [164] Maximum Gap
#
# https://leetcode.com/problems/maximum-gap/description/
#
# algorithms
# Hard (30.05%)
# Total Accepted:    55.3K
# Total Submissions: 184.2K
# Testcase Example:  '[]'
#
# Given an unsorted array, find the maximum difference between the successive
# elements in its sorted form.
# 
# Try to solve it in linear time/space.
# 
# Return 0 if the array contains less than 2 elements.
# 
# You may assume all elements in the array are non-negative integers and fit in
# the 32-bit signed integer range.
# 
# Credits:Special thanks to @porker2008 for adding this problem and creating
# all test cases.
#
class Solution:
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums))
        if len(nums) < 2:
            return 0
        minn, maxx = min(nums), max(nums)
        size = (maxx - minn) // (len(nums) - 1)
        # n buckets, only record min and max in each bucket
        buckets = [None] * ((maxx - minn) // size + 3)
        for v in nums:
            ind = (v - minn) // size
            if buckets[ind] == None:
                buckets[ind] = [v, v]
            else:
                buckets[ind][0] = min(buckets[ind][0], v)
                buckets[ind][1] = max(buckets[ind][1], v)
        i = 0
        max_gap = -float('inf')
        while i < len(buckets) - 1:
            if buckets[i] != None:
                for j in range(i + 1, len(buckets)):
                    if buckets[j] != None:
                        max_gap = max(max_gap, buckets[j][0] - buckets[i][1])
                        i = j - 1
                        break
            i += 1
        return max_gap
