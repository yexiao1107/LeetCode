'''
从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。

 

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回：

[3,9,20,15,7]
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode):
        if root == None: return []
        res = []
        queue = []
        queue.append(root)
        while queue:
            cur = queue.pop(0)
            res.append(cur.val)
            if cur.left: queue.append(cur.left)
            if cur.right: queue.append(cur.right)
        return res
