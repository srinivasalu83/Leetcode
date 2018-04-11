#
# [733] Flood Fill
#
# https://leetcode.com/problems/flood-fill/description/
#
# algorithms
# Easy (47.97%)
# Total Accepted:    12.3K
# Total Submissions: 25.6K
# Testcase Example:  '[[1,1,1],[1,1,0],[1,0,1]]\n1\n1\n2'
#
# 
# An image is represented by a 2-D array of integers, each integer representing
# the pixel value of the image (from 0 to 65535).
# 
# Given a coordinate (sr, sc) representing the starting pixel (row and column)
# of the flood fill, and a pixel value newColor, "flood fill" the image.
# 
# To perform a "flood fill", consider the starting pixel, plus any pixels
# connected 4-directionally to the starting pixel of the same color as the
# starting pixel, plus any pixels connected 4-directionally to those pixels
# (also with the same color as the starting pixel), and so on.  Replace the
# color of all of the aforementioned pixels with the newColor.
# 
# At the end, return the modified image.
# 
# Example 1:
# 
# Input: 
# image = [[1,1,1],[1,1,0],[1,0,1]]
# sr = 1, sc = 1, newColor = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]
# Explanation: 
# From the center of the image (with position (sr, sc) = (1, 1)), all pixels
# connected 
# by a path of the same color as the starting pixel are colored with the new
# color.
# Note the bottom corner is not colored 2, because it is not 4-directionally
# connected
# to the starting pixel.
# 
# 
# 
# Note:
# The length of image and image[0] will be in the range [1, 50].
# The given starting pixel will satisfy 0  and 0 .
# The value of each color in image[i][j] and newColor will be an integer in [0,
# 65535].
# 
#
class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        if not image or not image[0] or image[sr][sc] == newColor:
            return image
        self._floodFill(image, sr, sc, len(image), len(image[0]), image[sr][sc], newColor)
        return image
    
    def _floodFill(self, image, i, j, m, n, oldc, newc):
        if 0 <= i < m and 0 <= j < n and image[i][j] == oldc:
            image[i][j] = newc
            self._floodFill(image, i - 1, j, m, n, oldc, newc)
            self._floodFill(image, i + 1, j, m, n, oldc, newc)
            self._floodFill(image, i, j - 1, m, n, oldc, newc)
            self._floodFill(image, i, j + 1, m, n, oldc, newc)
