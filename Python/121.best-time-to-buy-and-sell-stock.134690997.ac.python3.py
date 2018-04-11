#
# [121] Best Time to Buy and Sell Stock
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
#
# algorithms
# Easy (42.91%)
# Total Accepted:    284.7K
# Total Submissions: 663.4K
# Testcase Example:  '[7,1,5,3,6,4]'
#
# Say you have an array for which the ith element is the price of a given stock
# on day i.
# 
# If you were only permitted to complete at most one transaction (ie, buy one
# and sell one share of the stock), design an algorithm to find the maximum
# profit.
# 
# Example 1:
# 
# Input: [7, 1, 5, 3, 6, 4]
# Output: 5
# 
# max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger
# than buying price)
# 
# 
# 
# Example 2:
# 
# Input: [7, 6, 4, 3, 1]
# Output: 0
# 
# In this case, no transaction is done, i.e. max profit = 0.
# 
# 
#
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return self.stat(prices, 0, len(prices) - 1)[2]
    
    def stat(self, prices, start, end):
        if start > end:
            return 2147283648, -1, 0
        if start == end:
            return prices[start], prices[end], 0
        mid = (start + end) // 2
        [min1, max1, pro1] = self.stat(prices, start, mid)
        [min2, max2, pro2] = self.stat(prices, mid + 1, end)
        res_min = min(min1, min2)
        res_max = max(max1, max2)
        res_pro = max(pro1, pro2, max2 - min1)
        return res_min, res_max, res_pro
