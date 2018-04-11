#
# [71] Simplify Path
#
# https://leetcode.com/problems/simplify-path/description/
#
# algorithms
# Medium (26.31%)
# Total Accepted:    111.3K
# Total Submissions: 423.3K
# Testcase Example:  '"/home/"'
#
# Given an absolute path for a file (Unix-style), simplify it.
# 
# For example,
# path = "/home/", => "/home"
# path = "/a/./b/../../c/", => "/c"
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
# Did you consider the case where path = "/../"?
# In this case, you should return "/".
# Another corner case is the path might contain multiple slashes '/' together,
# such as "/home//foo/".
# In this case, you should ignore redundant slashes and return "/home/foo".
# 
# 
#
class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        from collections import deque
        path = deque(path.split('/'))
        i = 0
        while i < len(path):
            # print(path, i)
            if path[i] == '.' or path[i] == '':
                del path[i]
            elif path[i] == '..':
                if i == 0:
                    del path[i]
                else:
                    del path[i], path[i - 1]
                    i -= 1
            else: 
                i += 1
        return '/' + '/'.join(path)
    
