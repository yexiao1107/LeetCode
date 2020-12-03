'''
统计所有小于非负整数 n 的质数的数量。

 

示例 1：

输入：n = 10
输出：4
解释：小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
示例 2：

输入：n = 0
输出：0
示例 3：

输入：n = 1
输出：0

'''
from math import sqrt


class Solution:



    def countPrimes_OOT(self, n: int) -> int:
        '''
        该方案暴力解决，运算超时
        :param n:
        :return:
        '''
        def is_prime(n):
            if n == 1:
                return False
            for i in range(2, int(sqrt(n)) + 1):
                if n % i == 0:
                    return False
            return True
        count = 0
        for i in range(n):
            if is_prime(i):
                count += 1
        return count

    def countPrimes(self, n: int) -> int:
        '''
        埃式法，利用i的倍数全是合数，i*i开始是因为i之前的数据都已经有倍数算过
        :param n:
        :return:
        '''
        is_prime = [1] * n
        count = 0
        for i in range(2, n):
            if is_prime[i]:
                count += 1j
                for j in range(i * i, n, i):
                    is_prime[j] = 0
        return count
