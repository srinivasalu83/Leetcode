#
# [88] Merge Sorted Array
#
# https://leetcode.com/problems/merge-sorted-array/description/
#
# algorithms
# Easy (32.13%)
# Total Accepted:    229.5K
# Total Submissions: 714.4K
# Testcase Example:  '[1]\n1\n[]\n0'
#
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as
# one sorted array.
# 
# 
# Note:
# You may assume that nums1 has enough space (size that is greater or equal to
# m + n) to hold additional elements from nums2. The number of elements
# initialized in nums1 and nums2 are m and n respectively.
#
class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i, j = m - 1, n - 1
        k = m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        while i >= 0:
            nums1[k] = nums1[i]
            i -= 1
            k -= 1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
        return
    
