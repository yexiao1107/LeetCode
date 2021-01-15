'''
输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7
 

限制：

0 <= 节点个数 <= 5000
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        '''
        前序：根左右
        中序：左根右
        根据前序的第一个元素就是根节点，中序找到根节点索引，分为左右子树
        :param preorder:
        :param inorder:
        :return:
        '''

        def recur(root, left, right):
            '''

            :param root: 前序根节点索引
            :param left: 中序左边界
            :param right: 中序右边界
            :return:
            '''
            if left > right: return
            node = TreeNode(preorder[root])
            i = index_dict[preorder[root]]
            node.left = recur(root + 1, left, i - 1)
            node.right = recur(i - left + root + 1, i + 1, right)
            return node

        index_dict = dict(zip(inorder, range(len(inorder))))
        return recur(0, 0, len(inorder) - 1)

if __name__ == "__main__":
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    solution = Solution()
    print(solution.buildTree(preorder, inorder))
