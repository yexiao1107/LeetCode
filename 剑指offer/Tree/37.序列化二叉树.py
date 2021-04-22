'''
请实现两个函数，分别用来序列化和反序列化二叉树。

示例: 

你可以将以下二叉树：

    1
   / \
  2   3
     / \
    4   5

序列化为 "[1,2,3,null,null,4,5]"
'''


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root: return ""
        queue = []
        res = []
        queue.append(root)
        while queue:
            tmp = queue.pop(0)
            if tmp:
                res.append(tmp.val)
                queue.append(tmp.left)
                queue.append(tmp.right)
            else:
                res.append('None')
        return '[' + ','.join(res) + ']'

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data: return []
        data_list = data[1:-1].split(",")
        queue = []
        root = TreeNode(int(data_list[0]))
        queue.append(root)
        i = 1
        while queue:
            node = queue.pop(0)
            if data_list[i] != 'None':
                node.left = TreeNode(int(data_list[i]))
                queue.append(node.left)
            i += 1
            if data_list[i] != 'None':
                node.right = TreeNode(int(data_list[i]))
                queue.append(node.right)
            i += 1
        return root
