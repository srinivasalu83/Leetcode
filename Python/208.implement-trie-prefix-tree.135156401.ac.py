#
# [208] Implement Trie (Prefix Tree)
#
# https://leetcode.com/problems/implement-trie-prefix-tree/description/
#
# algorithms
# Medium (30.91%)
# Total Accepted:    109.2K
# Total Submissions: 353.2K
# Testcase Example:  '["Trie","search"]\n[[],["a"]]'
#
# 
# Implement a trie with insert, search, and startsWith methods.
# 
# 
# 
# Note:
# You may assume that all inputs are consist of lowercase letters a-z.
# 
#
class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = [{}, True]
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        p = self.root
        for c in word:
            p = p[0].setdefault(c, [{}, False])
        p[1] = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        p = self.root
        for c in word:
            p = p[0].get(c, None)
            if p == None:
                return False
        return p[1]
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        p = self.root
        for c in prefix:
            p = p[0].get(c, None)
            if p == None:
                return False
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
