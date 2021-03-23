'''
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明:
1 ≤m≤n≤ 链表长度。

示例:

输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        def reverseN(head: ListNode, n: int) -> ListNode:
            if (n == 1):
                self.successor = head.next
                return head
            last = reverseN(head.next, n - 1)
            head.next.next = head
            head.next = self.successor
            return last

        if (m == 1): return reverseN(head, n)
        head.next = self.reverseBetween(head.next, m - 1, n - 1)
        return head

    # def reverse(self, head: ListNode) -> ListNode:
    #     if (head.next == None): return head
    #     last = self.reverse(head.next)
    #     head.next.next = head
    #     head.next = None
    #     return last
    def reverseBetween2(self, head: ListNode, left: int, right: int) -> ListNode:
        # 设置 dummyNode 是这一类问题的一般做法
        dummy_node = ListNode(-1)
        dummy_node.next = head
        pre = dummy_node
        for _ in range(left - 1):
            pre = pre.next

        cur = pre.next
        for _ in range(right - left):
            next = cur.next
            cur.next = next.next
            next.next = pre.next
            pre.next = next
        return dummy_node.next
