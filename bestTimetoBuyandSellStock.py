def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if len(prices) == 0 :
        return 0
    low = prices[0]
    maxPro = 0
    for i in range(len(prices)):
        if prices[i] < low:
            low = prices[i]
        maxPro = max(maxPro,prices[i] - low)
    return maxPro
if __name__ == "__main__":
    print(maxProfit([7, 1, 4, 3, 6]))
