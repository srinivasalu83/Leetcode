#
# [37] Sudoku Solver
#
# https://leetcode.com/problems/sudoku-solver/description/
#
# algorithms
# Hard (32.09%)
# Total Accepted:    91.1K
# Total Submissions: 283.9K
# Testcase Example:  '[[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]'
#
# Write a program to solve a Sudoku puzzle by filling the empty cells.
# 
# Empty cells are indicated by the character '.'.
# 
# You may assume that there will be only one unique solution.
# 
# 
# 
# A sudoku puzzle...
# 
# 
# 
# 
# ...and its solution numbers marked in red.
# 
#
class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.val = self.PossibleVals()
        self.Solver()

    def PossibleVals(self):
        a = "123456789"
        d, val = {}, {}
        for i in range(9):
            for j in range(9):
                ele = self.board[i][j]
                if ele != ".":
                    d[("r", i)] = d.get(("r", i), []) + [ele]
                    d[("c", j)] = d.get(("c", j), []) + [ele]
                    d[(i//3, j//3)] = d.get((i//3, j//3), []) + [ele]
                else:
                    val[(i,j)] = []
        for (i,j) in val.keys():
            inval = d.get(("r",i),[])+d.get(("c",j),[])+d.get((i//3,j//3),[])
            val[(i,j)] = [n for n in a if n not in inval ]
        return val

    def Solver(self):
        if len(self.val)==0:
            return True
        # start from the position with least choices
        kee = min(self.val.keys(), key=lambda x: len(self.val[x]))
        nums = self.val[kee]
        for n in nums:
            # update: the candidates being removed
            update = {kee:self.val[kee]}
            if self.ValidOne(n, kee, update): # valid choice
                if self.Solver(): # keep solving
                    return True
            self.undo(kee, update) # invalid choice or didn't solve it => undo
        return False

    def ValidOne(self, n, kee, update):
        self.board[kee[0]][kee[1]] = n
        del self.val[kee]
        i, j = kee
        # update candidate values of other positons
        for ind in self.val.keys():
            if n in self.val[ind]:
                if ind[0]==i or ind[1]==j or (ind[0]//3,ind[1]//3)==(i//3,j//3):
                    update[ind] = n
                    self.val[ind].remove(n)
                    # if this positon have no candidate values 
                    if len(self.val[ind])==0:
                        return False
        return True

    def undo(self, kee, update):
        self.board[kee[0]][kee[1]]="."
        for k in update:            
            if k not in self.val:
                self.val[k]= update[k]
            else:
                self.val[k].append(update[k])
        return None
