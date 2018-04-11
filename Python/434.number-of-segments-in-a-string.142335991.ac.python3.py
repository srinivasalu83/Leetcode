#
# [434] Number of Segments in a String
#
# https://leetcode.com/problems/number-of-segments-in-a-string/description/
#
# algorithms
# Easy (36.63%)
# Total Accepted:    37.4K
# Total Submissions: 102.1K
# Testcase Example:  '"Hello, my name is John"'
#
# Count the number of segments in a string, where a segment is defined to be a
# contiguous sequence of non-space characters.
# 
# Please note that the string does not contain any non-printable characters.
# 
# Example:
# 
# Input: "Hello, my name is John"
# Output: 5
# 
# 
#
class Solution:
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split())
        '''
        def is_valid_char(c):
            return c.isalnum() or c in ["'", "-"]
        
        s = ' ' + s.strip()
        count = 0
        for i in range(1, len(s)):
            if not is_valid_char(s[i - 1]) and is_valid_char(s[i]):
                count += 1
        return count
        '''
