'''
给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。

返回删除后的链表的头节点。

注意：此题对比原题有改动

示例 1:

输入: head = [4,5,1,9], val = 5
输出: [4,1,9]
解释: 给定你链表中值为5的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.
示例 2:

输入: head = [4,5,1,9], val = 1
输出: [4,5,9]
解释: 给定你链表中值为1的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.

'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        '''
        遍历到节点i的前一个节点，然后将指针指向i的下一个节点
        :param head:
        :param val:
        :return:
        '''
        if head.val == val:  return head.next
        pre, cur = head, head.next
        while cur.val != val and cur != None:
            pre, cur = cur, cur.next
        if (cur != None):
            pre.next = cur.next
        return head
