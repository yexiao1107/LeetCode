'''
定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre, cur, nxt = None, head, head
        while cur:
            nxt = cur.next
            cur.next = pre

            pre = cur
            cur = nxt
        return pre