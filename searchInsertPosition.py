def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    low = 0
    high = len(nums) - 1
    while (low <= high):
        mid = (low + high) // 2
        if (nums[mid] == target):
            return mid
        elif (nums[mid] < target):
            low += 1
        else:
            high -= 1
    return low

if __name__ == "__main__":
    print(searchInsert([1,3,5,6], 7))
