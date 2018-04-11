#
# [657] Judge Route Circle
#
# https://leetcode.com/problems/judge-route-circle/description/
#
# algorithms
# Easy (68.42%)
# Total Accepted:    70.9K
# Total Submissions: 103.7K
# Testcase Example:  '"UD"'
#
# 
# Initially, there is a Robot at position (0, 0). Given a sequence of its
# moves, judge if this robot makes a circle, which means it moves back to the
# original place. 
# 
# 
# 
# The move sequence is represented by a string. And each move is represent by a
# character. The valid robot moves are R (Right), L (Left), U (Up) and D
# (down). The output should be true or false representing whether the robot
# makes a circle.
# 
# 
# Example 1:
# 
# Input: "UD"
# Output: true
# 
# 
# 
# Example 2:
# 
# Input: "LL"
# Output: false
# 
# 
#
class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        vertical_pos = 0
        horizontal_pos = 0
        for move in moves:
            if move == 'U':
                vertical_pos += 1
            elif move == 'D':
                vertical_pos -= 1
            elif move == 'L':
                horizontal_pos -= 1
            else:
                horizontal_pos += 1
        return True if vertical_pos == 0 and horizontal_pos == 0 else False
