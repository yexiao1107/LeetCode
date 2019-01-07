class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        h = head
        while h:
            if h.next and h.next.val == h.val:
                h.next = h.next.next
            else:
                h = h.next
        return head


if __name__ == "__main__":
    arr1 = [1, 1, 2, 3, 3]
    l1 = ListNode(arr1[0])
    p1 = l1
    for i in arr1[1:]:
        p1.next = ListNode(i)
        p1 = p1.next
    s = Solution()
    q = s.deleteDuplicates(l1)
    while q:
        print(q.val)
        q = q.next
