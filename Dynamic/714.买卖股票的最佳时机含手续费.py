'''
给定一个整数数组prices，其中第i个元素代表了第i天的股票价格 ；非负整数fee 代表了交易股票的手续费用。

你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。

返回获得利润的最大值。

注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。

示例 1:

输入: prices = [1, 3, 2, 8, 4, 9], fee = 2
输出: 8
解释: 能够达到的最大利润:
在此处买入prices[0] = 1
在此处卖出 prices[3] = 8
在此处买入 prices[4] = 4
在此处卖出 prices[5] = 9
总利润:((8 - 1) - 2) + ((9 - 4) - 2) = 8.
'''


class Solution:
    def maxProfit(self, prices, fee: int) -> int:
        '''
        动态规划，状态转移矩阵
        1.今天不持有最大化收益：dp[i][0]=max(dp[i-1][0],dp[i-1][1]+prices[i]-free)
        今天不持有由两个状态转移而来，昨天不持有，昨天持有今天卖出
        2.今天持有最大化收益：dp[i][1]=max(dp[i-1][1],dp[i-1][0]-prices[i])
        今天持有由两个状态转移而来，昨天持有，昨天不持有今天买入

        空间还可以优化
        :param prices:
        :param fee:
        :return:
        '''
        size = len(prices)
        dp = [0, -prices[0]]
        for i in range(1, size):
            tmp = dp[0]
            dp[0] = max(tmp, dp[1] + prices[i] - fee)
            dp[1] = max(dp[1], tmp - prices[i])

        return dp[0]


if __name__ == "__main__":
    prices = [1, 3, 2, 8, 4, 9]
    fee = 2
    solution = Solution()
    print(solution.maxProfit(prices, fee))
