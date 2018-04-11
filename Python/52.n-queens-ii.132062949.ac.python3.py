#
# [52] N-Queens II
#
# https://leetcode.com/problems/n-queens-ii/description/
#
# algorithms
# Hard (46.82%)
# Total Accepted:    74.5K
# Total Submissions: 159.2K
# Testcase Example:  '1'
#
# Follow up for N-Queens problem.
# 
# Now, instead outputting board configurations, return the total number of
# distinct solutions.
# 
# 
#
class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.indicator = [[True for i in range(n)] for j in range(n)]
        self.ret = 0
        self.update = {}
        self._search(0, n - 1)
        return self.ret

    def _search(self, i, end):
        indicator, update = self.indicator, self.update
        # print(i, end, indicator, update)
        current_row = indicator[i]
        if i == end:
            for j, bo in enumerate(current_row):
                if bo:
                    # print('found')
                    self.ret += 1
        else:
            for j, bo in enumerate(current_row):
                if bo:
                    for k in range(i + 1, end + 1):
                        update.setdefault(i, [])
                        if indicator[k][j]:
                            update[i].append((k, j))
                            indicator[k][j] = False
                        if j - k + i >= 0 and indicator[k][j - k + i]:
                            update[i].append((k, j - k + i))
                            indicator[k][j - k + i] = False
                        if j + k - i <= end and indicator[k][j + k - i]:
                            update[i].append((k, j + k - i))
                            indicator[k][j + k - i] = False
                    self._search(i + 1, end)
                    self._undo(i)

    def _undo(self, lnum):
        l = self.update[lnum]
        indicator = self.indicator
        for i, j in l:
            indicator[i][j] = True
        self.update[lnum] = []
        
