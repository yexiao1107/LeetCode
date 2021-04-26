'''
请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3

 

示例 1：

输入：root = [1,2,2,3,4,4,3]
输出：true
示例 2：

输入：root = [1,2,2,null,3,null,3]
输出：false
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isEqual(self, p: TreeNode, q: TreeNode):
        if p == None and q == None: return True
        if p and q and p.val == q.val:
            return self.isEqual(p.left, q.right) and self.isEqual(p.right, q.left)
        return False

    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isEqual(root.left, root.right)
