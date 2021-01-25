'''
给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），
每段绳子的长度记为 k[0],k[1]...k[m-1] 。请问 k[0]*k[1]*...*k[m-1]
可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，
此时得到的最大乘积是18。

示例 1：

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1
示例2:

输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 ×3 ×4 = 36
提示：

2 <= n <= 58
'''


class Solution:

    def cuttingRope(self, n: int) -> int:
        '''
        动态规划，dp[i],2种情况最大，剪和不剪
        j处剪一下，后边不剪dp[i] = j*(i-j)
        后边还剪dp[i] = dp[i-j]*j
        :param n:
        :return:
        '''
        dp = [0 for _ in range(n + 1)]
        dp[2] = 1
        for i in range(3, n + 1):
            for j in range(i):
                dp[i] = max(dp[i], max(j * (i - j), dp[i - j] * j))
        return dp[n]


if __name__ == "__main__":
    solution = Solution()
    print(solution.cuttingRope(10))
