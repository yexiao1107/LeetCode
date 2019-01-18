def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: void Do not return anything, modify nums1 in-place instead.
    """
    p, q = m - 1, n - 1
    while p >= 0 and q >= 0:
        if nums1[p] > nums2[q]:
            nums1[p + q + 1] = nums1[p]
            p = p - 1
        else:
            nums1[p + q + 1] = nums2[q]
            q = q - 1
    nums1[:q + 1] = nums2[:q + 1]
    return nums1


if __name__ == "__main__":
    print(merge([1,2,3,0,0,0], 3, [1, 2, 3], 3))