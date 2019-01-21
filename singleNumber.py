def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ans = nums[0]
    for i in range(1, len(nums)):
        ans = ans ^ nums[i]
    return ans

if __name__ == "__main__":
    print(singleNumber([2,2,1]))