#
# [68] Text Justification
#
# https://leetcode.com/problems/text-justification/description/
#
# algorithms
# Hard (20.00%)
# Total Accepted:    69.6K
# Total Submissions: 348.2K
# Testcase Example:  '["This", "is", "an", "example", "of", "text", "justification."]\n16'
#
# Given an array of words and a length L, format the text such that each line
# has exactly L characters and is fully (left and right) justified.
# 
# You should pack your words in a greedy approach; that is, pack as many words
# as you can in each line. Pad extra spaces ' ' when necessary so that each
# line has exactly L characters.
# 
# Extra spaces between words should be distributed as evenly as possible. If
# the number of spaces on a line do not divide evenly between words, the empty
# slots on the left will be assigned more spaces than the slots on the right.
# 
# For the last line of text, it should be left justified and no extra space is
# inserted between words.
# 
# For example,
# words: ["This", "is", "an", "example", "of", "text", "justification."]
# L: 16.
# 
# Return the formatted lines as:
# 
# 
# [
# ⁠  "This    is    an",
# ⁠  "example  of text",
# ⁠  "justification.  "
# ]
# 
# 
# 
# 
# Note: Each word is guaranteed not to exceed L in length.
# 
# click to show corner cases.
# 
# Corner Cases:
# 
# 
# 
# 
# 
# 
# A line other than the last line might contain only one word. What should you
# do in this case?
# In this case, that line should be left-justified.
# 
# 
#
class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        ret = [[]]
        currentWidth = 0
        for s in words:
            if currentWidth + len(s) > maxWidth:
                ret[-1].pop()
                ret.append([])
                currentWidth = 0
            ret[-1].append(s)
            currentWidth += len(s) + 1
            ret[-1].append("")
        ret[-1].pop()
        if not ret:
            ret.pop()
        print(ret)
        for i, row in enumerate(ret):
            spaceTotalLen = maxWidth - sum([len(s) for s in row])
            if i == len(ret) - 1:
                for j in range(1, len(row), 2):
                    row[j] = " "
                    spaceTotalLen -= 1
                row.append(" " * spaceTotalLen)
            else:
                spaceNum = (len(row) - 1) // 2
                if spaceNum == 0:
                    row.append(" " * spaceTotalLen)
                    continue
                spaceAverage = spaceTotalLen // spaceNum
                spaceLeft = spaceTotalLen - spaceNum * spaceAverage
                for j in range(1, len(row), 2):
                    if (spaceLeft > 0):
                        row[j] = " " * (spaceAverage + 1)
                        spaceLeft -= 1
                    else:
                        row[j] = " " * spaceAverage
        print(ret)
        return ["".join(row) for row in ret]
    
