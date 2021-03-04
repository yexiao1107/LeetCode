'''
给定一个二叉搜索树的根节点 root ，和一个整数 k ，
请你设计一个算法查找其中第k个最小元素（从 1 开始计数）。

示例 1：

输入：root = [3,1,4,null,2], k = 1
输出：1
示例 2：

输入：root = [5,3,6,2,4,null,null,1], k = 3
输出：3

提示：

树中的节点数为 n 。
1 <= k <= n <= 104
0 <= Node.val <= 104
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.res = 0
        self.index = 1

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.traverse(root, k)
        return self.res

    def traverse(self, root, k):
        if root == None: return
        self.traverse(root.left, k)
        self.res = root.val
        self.index += 1
        if (self.index == k):
            self.res = root.val
            return
        self.traverse(root.right, k)
