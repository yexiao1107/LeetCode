'''
给定一棵二叉树，返回所有重复的子树。对于同一类的重复子树，
你只需要返回其中任意一棵的根结点即可。
两棵树重复是指它们具有相同的结构以及相同的结点值。

示例 1：

        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4
下面是两个重复的子树：

      2
     /
    4
和

    4
因此，你需要以列表的形式返回上述重复子树的根结点。
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.map = {}
        self.res = set()

    def findDuplicateSubtrees(self, root: TreeNode):
        self.traverse(root)
        return list(self.res)

    def traverse(self, root):
        if root == None: return "#"
        left = self.traverse(root.left)
        right = self.traverse(root.right)
        strSub = str(left) + "," + str(right) + "," + str(root.val)
        num = self.map.get(strSub, default=0)
        if num == 1:
            self.res.add(root)
        self.map[strSub] = num + 1
        return strSub
