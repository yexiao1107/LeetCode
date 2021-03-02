'''
根据一棵树的中序遍历与后序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

中序遍历 inorder =[9,3,15,20,7]
后序遍历 postorder = [9,15,7,20,3]
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
    def buildTree(self, inorder, postorder) -> TreeNode:
        root = self.build(inorder, 0, len(inorder) - 1,
                          postorder, 0, len(postorder) - 1)
        return root

    def build(self, inorder, in_start, in_end,
              postorder, post_start, post_end):
        if post_start > post_end: return None
        root_value = postorder[post_end]
        root_index = inorder.index(root_value)
        root = TreeNode(root_value)
        left_size = root_index - in_start
        root.left = self.build(inorder, in_start, root_index-1,
                               postorder, post_start, post_start + left_size-1)
        root.right = self.build(inorder, root_index + 1, in_end,
                                postorder, post_start + left_size, post_end - 1)
        return root