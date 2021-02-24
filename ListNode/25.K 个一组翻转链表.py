'''
给你一个链表，每k个节点一组进行翻转，请你返回翻转后的链表。

k是一个正整数，它的值小于或等于链表的长度。

如果节点总数不是k的整数倍，那么请将最后剩余的节点保持原有顺序。


示例：

给你这个链表：1->2->3->4->5

当k= 2 时，应当返回: 2->1->4->3->5

当k= 3 时，应当返回: 3->2->1->4->5

说明：

你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse(self, head1: ListNode, head2: ListNode):
        pre, cur, nxt = None, head1, head1
        while cur != head2:
            nxt = cur.next
            cur.next = pre

            pre = cur
            cur = nxt
        return pre

    def reverseKGroup(self, head: ListNode, k: int):
        if (head == None): return None
        a = b = head
        for i in range(k):
            if (b == None): return head
            b = b.next
        new_head = self.reverse(a, b)
        a.next = self.reverseKGroup(b, k)
        return new_head