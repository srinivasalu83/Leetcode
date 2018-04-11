#
# [150] Evaluate Reverse Polish Notation
#
# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
#
# algorithms
# Medium (28.44%)
# Total Accepted:    114K
# Total Submissions: 400.9K
# Testcase Example:  '["2","1","+","3","*"]'
#
# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
# 
# Valid operators are +, -, *, /. Each operand may be an integer or another
# expression.
# 
# Some examples:
# 
# 
# ⁠ ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
# ⁠ ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
# 
# 
# 
# 
#
class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        op_stack = []
        exp_stack = []
        for token in tokens:
            if token == '+':
                r = exp_stack.pop()
                l = exp_stack.pop()
                exp_stack.append(int(l + r))
            elif token == '-':
                r = exp_stack.pop()
                l = exp_stack.pop()
                exp_stack.append(int(l - r))
            elif token == '*':
                r = exp_stack.pop()
                l = exp_stack.pop()
                exp_stack.append(int(l * r))
            elif token == '/':
                r = exp_stack.pop()
                l = exp_stack.pop()
                exp_stack.append(int(l / r))
            else:
                exp_stack.append(int(token))
        return exp_stack[-1]
