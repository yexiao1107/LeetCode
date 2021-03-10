'''
给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的key对应的节点，
并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。

一般来说，删除节点可分为两个步骤：

首先找到需要删除的节点；
如果找到了，删除它。
说明： 要求算法时间复杂度为O(h)，h 为树的高度。

示例:

root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

给定需要删除的节点值是 3，所以我们首先找到 3 这个节点，然后删除它。

一个正确的答案是 [5,4,6,2,null,null,7], 如下图所示。

    5
   / \
  4   6
 /     \
2       7

另一个正确答案是 [5,2,6,null,4,null,7]。

    5
   / \
  2   6
   \   \
    4   7
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMin(self, tree: TreeNode):
        while (tree.left != None): tree = tree.left
        return tree

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root == None: return None
        if root.val == key:
            if root.left == None: return root.right
            if root.right == None: return root.left
            if root.left != None and root.right != None:
                min = self.getMin(root.right)
                root.val = min.val
                root.right = self.deleteNode(root.right, min.val)
        if root.val > key: root.left = self.deleteNode(root.left, key)
        if root.val < key: root.right = self.deleteNode(root.right, key)
        return root
