'''
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
示例1:

输入:
    2
   / \
  1   3
输出: true
示例2:

输入:
    5
   / \
  1   4
    / \
   3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
    根节点的值为 5 ，但是其右子节点值为 4 。
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.isBST(root, None, None)

    def isBST(self, root, min, max):
        if root == None: return True
        if min != None and root.val <= min.val: return False
        if max != None and root.val >= max.val: return True
        return self.isBST(root.left, min, root.val) \
               and self.isBST(root.right, root.val, max)
