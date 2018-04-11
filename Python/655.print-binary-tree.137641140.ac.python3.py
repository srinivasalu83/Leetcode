#
# [655] Print Binary Tree
#
# https://leetcode.com/problems/print-binary-tree/description/
#
# algorithms
# Medium (49.23%)
# Total Accepted:    8.7K
# Total Submissions: 17.7K
# Testcase Example:  '[1,2]'
#
# Print a binary tree in an m*n 2D string array following these rules: 
# 
# 
# The row number m should be equal to the height of the given binary tree.
# The column number n should always be an odd number.
# The root node's value (in string format) should be put in the exactly middle
# of the first row it can be put. The column and the row where the root node
# belongs will separate the rest space into two parts (left-bottom part and
# right-bottom part). You should print the left subtree in the left-bottom part
# and print the right subtree in the right-bottom part. The left-bottom part
# and the right-bottom part should have the same size. Even if one subtree is
# none while the other is not, you don't need to print anything for the none
# subtree but still need to leave the space as large as that for the other
# subtree. However, if two subtrees are none, then you don't need to leave
# space for both of them. 
# Each unused space should contain an empty string "".
# Print the subtrees following the same rules.
# 
# 
# Example 1:
# 
# Input:
# ⁠    1
# ⁠   /
# ⁠  2
# Output:
# [["", "1", ""],
# ⁠["2", "", ""]]
# 
# 
# 
# 
# Example 2:
# 
# Input:
# ⁠    1
# ⁠   / \
# ⁠  2   3
# ⁠   \
# ⁠    4
# Output:
# [["", "", "", "1", "", "", ""],
# ⁠["", "2", "", "", "", "3", ""],
# ⁠["", "", "4", "", "", "", ""]]
# 
# 
# 
# Example 3:
# 
# Input:
# ⁠     1
# ⁠    / \
# ⁠   2   5
# ⁠  / 
# ⁠ 3 
# ⁠/ 
# 4 
# Output:
# 
# [["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""]
# ⁠["",  "",  "", "2", "", "", "", "",  "",  "",  "",  "5", "", "", ""]
# ⁠["",  "3", "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]
# ⁠["4", "",  "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]]
# 
# 
# 
# Note:
# The height of binary tree is in the range of [1, 10].
# 
#
class Solution:
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        if not root:
            return []
        record = [[root]]
        while True:
            level = []
            is_all_null = True
            for node in record[-1]:
                if node:
                    level.append(node.left)
                    level.append(node.right)
                    if node.right or node.left:
                        is_all_null = False
                else:
                    level.append(None)
                    level.append(None)
            if is_all_null:
                break
            else:
                record.append(level)
        print(record)
        height = len(record)
        width = len(record[-1]) * 2 - 1
        offset = (width + 1) // 2
        fill_inds = [(width - 1) // 2]
        res = [[''] * width for _ in range(height)]
        for h in range(height):
            for i in range(len(fill_inds)):
                if record[h][i]:
                    res[h][fill_inds[i]] = str(record[h][i].val)
            offset = offset // 2
            new_fill_inds = []
            for ind in fill_inds:
                new_fill_inds.append(ind - offset)
                new_fill_inds.append(ind + offset)
            fill_inds = new_fill_inds
            print(offset, res)
        return res
            
        
