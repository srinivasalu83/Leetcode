#
# [49] Group Anagrams
#
# https://leetcode.com/problems/group-anagrams/description/
#
# algorithms
# Medium (38.46%)
# Total Accepted:    194.1K
# Total Submissions: 504.7K
# Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
#
# Given an array of strings, group anagrams together.
# 
# 
# For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
# Return:
# 
# [
# ⁠ ["ate", "eat","tea"],
# ⁠ ["nat","tan"],
# ⁠ ["bat"]
# ]
# 
# Note: All inputs will be in lower-case.
#
class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ret = {}
        for s in strs:
            ret.setdefault(''.join(sorted(s)), []).append(s)
        return list(ret.values())
    
