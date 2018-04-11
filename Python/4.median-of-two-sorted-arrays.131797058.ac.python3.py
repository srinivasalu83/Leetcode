#
# [4] Median of Two Sorted Arrays
#
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (23.05%)
# Total Accepted:    250.3K
# Total Submissions: 1.1M
# Testcase Example:  '[1,3]\n[2]'
#
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# 
# Find the median of the two sorted arrays. The overall run time complexity
# should be O(log (m+n)).
# 
# Example 1:
# 
# nums1 = [1, 3]
# nums2 = [2]
# 
# The median is 2.0
# 
# 
# 
# Example 2:
# 
# nums1 = [1, 2]
# nums2 = [3, 4]
# 
# The median is (2 + 3)/2 = 2.5
# 
# 
#
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """ 
        totalLen = len(nums1) + len(nums2)
        if totalLen % 2 == 1:
            return self.kInd(nums1, nums2, totalLen // 2)
        else:
            return (self.kInd(nums1, nums2, totalLen // 2 - 1) + self.kInd(nums1, nums2, totalLen // 2)) / 2
        
    def kInd(self, A, B, k):
        if not A:
            return B[k]
        if not B:
            return A[k]
        midA, midB = len(A) // 2, len(B) // 2
        if k <= midA + midB:
            if A[midA] > B[midB]:
                return self.kInd(A[:midA], B, k)
            else:
                return self.kInd(A, B[:midB], k)
        else:
            if A[midA] > B[midB]:
                return self.kInd(A, B[midB + 1:], k - midB - 1)
            else:
                return self.kInd(A[midA + 1:], B, k - midA - 1)
            
