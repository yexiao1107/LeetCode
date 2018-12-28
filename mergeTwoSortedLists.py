class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        result = ListNode(0)
        l = result
        while l1 and l2:
            if l1.val < l2.val:
                l.next = l1
                l1 = l1.next
            else:
                l.next = l2
                l2 = l2.next
            l = l.next

        l.next = l1 or l2

        return result.next


if __name__ == "__main__":
    arr1 = [1, 2, 5]
    arr2 = [1, 3, 7]
    l1 = ListNode(arr1[0])
    p1 = l1
    l2 = ListNode(arr2[0])
    p2 = l2
    for i in arr1[1:]:
        p1.next = ListNode(i)
        p1 = p1.next
    for i in arr2[1:]:
        p2.next = ListNode(i)
        p2 = p2.next
    s = Solution()
    # 融合两个链表
    q = s.mergeTwoLists(l1, l2)
    while q:
        print(q.val)
        q = q.next
