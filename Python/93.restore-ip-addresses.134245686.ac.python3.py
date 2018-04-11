#
# [93] Restore IP Addresses
#
# https://leetcode.com/problems/restore-ip-addresses/description/
#
# algorithms
# Medium (28.45%)
# Total Accepted:    102.3K
# Total Submissions: 359.5K
# Testcase Example:  '"25525511135"'
#
# Given a string containing only digits, restore it by returning all possible
# valid IP address combinations.
# 
# For example:
# Given "25525511135",
# 
# return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
# 
#
class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 4:
            return []
        ret = []
        self._restore(s, 4, ret, [])
        return ret
    
    def _restore(self, s, num, ret, cur):
        # print(s, num, ret, cur)
        if num == 1:
            if len(s) > 0 and 0 <= int(s) <= 255 and str(int(s)) == s:
                ret.append('.'.join(cur + [s]))
        else:
            for i in range(1, 4):
                if len(s) > i and 0 <= int(s[:i]) <= 255 and str(int(s[:i])) == s[:i]:
                    cur.append(s[:i])
                    self._restore(s[i:], num - 1, ret, cur)
                    cur.pop()
                    
