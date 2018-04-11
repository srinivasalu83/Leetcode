#
# [123] Best Time to Buy and Sell Stock III
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/
#
# algorithms
# Hard (30.36%)
# Total Accepted:    106.5K
# Total Submissions: 350.8K
# Testcase Example:  '[]'
#
# Say you have an array for which the ith element is the price of a given stock
# on day i.
# 
# Design an algorithm to find the maximum profit. You may complete at most two
# transactions.
# 
# Note:
# You may not engage in multiple transactions at the same time (ie, you must
# sell the stock before you buy again).
#
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        hold1 = hold2 = sell1 = sell2 = -float('inf')
        for p in prices:
            sell2 = max(sell2, hold2 + p)
            hold2 = max(hold2, sell1 - p)
            sell1 = max(sell1, hold1 + p)
            hold1 = max(hold1, -p)
        return max(0, sell1, sell2)
