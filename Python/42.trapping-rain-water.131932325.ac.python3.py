#
# [42] Trapping Rain Water
#
# https://leetcode.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (37.53%)
# Total Accepted:    162.1K
# Total Submissions: 432K
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# Given n non-negative integers representing an elevation map where the width
# of each bar is 1, compute how much water it is able to trap after raining.
# 
# For example,
# Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
# 
# 
# 
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In
# this case, 6 units of rain water (blue section) are being trapped. Thanks
# Marcos for contributing this image!
# 
#
class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        acc, length = 0, len(height)
        bars = [[0, 0] for i in range(length)]
        lo, hi = 0, 0
        for i in range(length):
            lo = max(lo, height[i])
            hi = max(hi, height[length - 1 - i])
            bars[i][0], bars[length - 1 - i][1] = lo, hi
            
        for i in range(1, length - 1):
            bar = min(bars[i])
            if bar > height[i]:
                acc += bar - height[i]
        return acc
        
    def asdf():
        height = height + [0]
        self.height = height
        lastPeak = 0
        acc = 0
        for i in range(1, len(height) - 1):
            if height[i - 1] < height[i] and height[i] >= height[i + 1]:
                acc += self.calculate(lastPeak, i)
                lastPeak = i
        return acc
    
    def calculate(self, lo, hi):
        acc = 0
        hei = min(self.height[lo], self.height[hi])
        for i in range(lo + 1, hi):
            if hei > self.height[i]:
                acc += (hei - self.height[i])
        return acc
