#
# [165] Compare Version Numbers
#
# https://leetcode.com/problems/compare-version-numbers/description/
#
# algorithms
# Medium (20.82%)
# Total Accepted:    99K
# Total Submissions: 475.2K
# Testcase Example:  '"0.1"\n"1.1"'
#
# Compare two version numbers version1 and version2.
# If version1 > version2 return 1, if version1 < version2 return -1, otherwise
# return 0.
# 
# You may assume that the version strings are non-empty and contain only digits
# and the . character.
# The . character does not represent a decimal point and is used to separate
# number sequences.
# For instance, 2.5 is not "two and a half" or "half way to version three", it
# is the fifth second-level revision of the second first-level revision.
# 
# Here is an example of version numbers ordering:
# 
# 
# 0.1 < 1.1 < 1.2 < 13.37
# 
# Credits:
# Special thanks to @ts for adding this problem and creating all test cases.
# 
#
class Solution:
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))
        min_len = min(len(v1), len(v2))
        for i in range(min_len):
            if v1[i] > v2[i]:
                return 1
            elif v1[i] < v2[i]:
                return -1
        if len(v1) > len(v2):
            return 1 if any(v > 0 for v in v1[min_len:]) else 0
        elif len(v2) > len(v1):
            return -1 if any(v > 0 for v in v2[min_len:]) else 0
        else:
            return 0
