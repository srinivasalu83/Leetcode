#
# [122] Best Time to Buy and Sell Stock II
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
#
# algorithms
# Easy (47.73%)
# Total Accepted:    199.4K
# Total Submissions: 417.8K
# Testcase Example:  '[]'
#
# Say you have an array for which the ith element is the price of a given stock
# on day i.
# 
# Design an algorithm to find the maximum profit. You may complete as many
# transactions as you like (ie, buy one and sell one share of the stock
# multiple times). However, you may not engage in multiple transactions at the
# same time (ie, you must sell the stock before you buy again).
#
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profits = [0] * len(prices)
        for i in range(1, len(prices)):
            profits[i] = max(0, prices[i] - prices[i - 1])
        return sum(profits)
