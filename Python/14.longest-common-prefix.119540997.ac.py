#
# [14] Longest Common Prefix
#
# https://leetcode.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (31.60%)
# Total Accepted:    264.1K
# Total Submissions: 835.9K
# Testcase Example:  '[]'
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
# 
#
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        commonlen = min([len(ss) for ss in strs])
        for ii in range(commonlen):
            standard = strs[0][ii]
            for jj in range(len(strs)):
                if (standard != strs[jj][ii]):
                    return strs[0][:ii]
        return strs[0][:commonlen]
