def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 0:
        return 0
    j = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[j]:
            nums[j + 1] = nums[i]
            j += 1
    return j + 1


if __name__ == "__main__":
    print(removeDuplicates([0, 1, 1, 1, 2, 3]))
