'''
给定一个整数数组prices ，它的第 i 个元素prices[i] 是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。


示例 1：

输入：k = 2, prices = [2,4,1]
输出：2
解释：在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
示例 2：

输入：k = 2, prices = [3,2,6,5,0,3]
输出：7
解释：在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
     随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。


提示：

0 <= k <= 109
0 <= prices.length <= 1000
0 <= prices[i] <= 1000
'''


class Solution:
    def maxProfit(self, k: int, prices) -> int:
        '''
        buy[i][j]=max(buy[i-1][j],sell[i-1][j-1]-price[i])
        sell[i][j]=max(sell[i-1][j],buy[i-1][j]+price[i])
        :param k:
        :param prices:
        :return:
        '''
        if len(prices) == 0 or k == 0: return 0
        buy = [[-1 << 31] * k for _ in range(len(prices))]
        sell = [[-1 << 31] * k for _ in range(len(prices))]
        buy[0][0] = -prices[0]
        res = -1 << 31
        for i in range(1, len(prices)):
            for j in range(k):
                buy[i][j] = max(buy[i - 1][j], (sell[i - 1][j - 1] - prices[i]) if j >= 1 else (-prices[i]))
                sell[i][j] = max(sell[i - 1][j], buy[i - 1][j] + prices[i])
                res = max(res, sell[i][j])
        return max(0, res)


if __name__ == "__main__":
    k = 2
    prices = [3, 2, 6, 5, 0, 3]
    solution = Solution()
    print(solution.maxProfit(k, prices))
