'''
请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true
进阶：
你能否用O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    ##后序遍历，O(n)做法
    def traverse(self, right: ListNode):
        if (right == None): return True
        res = self.traverse(right.next)
        res = res and (self.left.val == right.val)
        self.left = self.left.next
        return res

    def isPalindromeOn(self, head: ListNode) -> bool:
        self.left = head
        return self.traverse(head)

    def reverse(self, head: ListNode) -> ListNode:
        pre, cur, nxt = None, head, head
        while cur != None:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

    def isPalindrome(self, head: ListNode) -> bool:
        slow, fast = head, head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        if (fast != None):
            slow = slow.next
        left = head
        right = self.reverse(slow)
        while (right != None):
            if (left.val != right.val):
                return False
            left = left.next
            right = right.next
        return True
