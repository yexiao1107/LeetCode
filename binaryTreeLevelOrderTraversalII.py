class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        queue = [(root, 0)]
        while len(queue) > 0:
            node, depth = queue.pop()
            if node:
                if len(res) <= depth:
                    res.insert(0, [])
                res[-(depth + 1)].append(node.val)
                queue.insert(0, (node.left, depth + 1))
                queue.insert(0, (node.right, depth + 1))
        return res
