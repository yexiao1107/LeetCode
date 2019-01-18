def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    maxPro = 0
    for i in range(1,len(prices)):
        if prices[i] > prices[i-1]:
            maxPro += prices[i] - prices[i-1]
    return maxPro

if __name__ == "__main__":
    print(maxProfit([7,1,5,3,6,4]))