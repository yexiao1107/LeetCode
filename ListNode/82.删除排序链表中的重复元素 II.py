'''
存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除链表
中所有存在数字重复情况的节点，只保留原始链表中没有重复出现的数字。

返回同样按升序排列的结果链表。

示例 1：

输入：head = [1,2,3,3,4,4,5]
输出：[1,2,5]
示例 2：


输入：head = [1,1,1,2,3]
输出：[2,3]
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        dump = ListNode(0, head)
        cur = dump
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                x = cur.next.val
                while cur.next and cur.next.val == x:
                    cur.next = cur.next.next
            else:
                cur = cur.next
        return dump.next
