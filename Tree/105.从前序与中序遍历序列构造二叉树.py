'''
根据一棵树的前序遍历与中序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

前序遍历 preorder =[3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        root = self.build(preorder, 0, len(preorder) - 1,
                          inorder, 0, len(inorder) - 1)
        return root

    def build(self, preorder, pre_start, pre_end,
              inorder, in_start, in_end):
        if pre_start > pre_end: return None
        root_val = preorder[pre_start]
        root_index = inorder.index(root_val)
        root = TreeNode(root_val)

        left_size = root_index - in_start
        root.left = self.build(preorder, pre_start + 1, pre_start + left_size,
                               inorder, in_start, root_index-1)
        root.right = self.build(preorder, pre_start + left_size + 1, pre_end,
                                inorder, root_index + 1, in_end)
        return root
