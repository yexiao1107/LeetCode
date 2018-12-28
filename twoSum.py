def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    dict = {}
    for i in range(len(nums)):
        x = nums[i]
        if target - x in dict:
            return dict[target - x], i
        dict[x] = i


if __name__ == '__main__':
    print(twoSum([2, 7, 11, 15], 9))
