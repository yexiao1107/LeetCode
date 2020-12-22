'''
给定一个二叉树，返回其节点值的锯齿形层序遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回锯齿形层序遍历如下：

[
  [3],
  [20,9],
  [15,7]
]
'''


# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
        if not root: return []
        res = []
        que = [root]
        level = 0
        while que:
            arr = []
            for _ in range(len(que)):
                cur = que.pop(0)
                arr.append(cur.val)
                if cur.left: que.append(cur.left)
                if cur.right: que.append(cur.right)
            if level % 2: arr.reverse()
            res.append(arr)
            level += 1
        return res
