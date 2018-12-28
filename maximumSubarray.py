def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    sum = 0
    maxsum = -10000
    for i in range(len(nums)):
        if sum < 0:
            sum = 0
        sum += nums[i]
        maxsum = max(sum,maxsum)
    return maxsum

if __name__ == "__main__":
    print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
