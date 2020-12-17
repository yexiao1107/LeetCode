'''
给你一个按升序排序的整数数组 num（可能包含重复数字），请你将它们分割成一个或多个子序列，
其中每个子序列都由连续整数组成且长度至少为 3 。

如果可以完成上述分割，则返回 true ；否则，返回 false 。

示例 1：

输入: [1,2,3,3,4,5]
输出: True
解释:
你可以分割出这样两个连续子序列 :
1, 2, 3
3, 4, 5不会


示例 2：

输入: [1,2,3,3,4,4,5,5]
输出: True
解释:
你可以分割出这样两个连续子序列 :
1, 2, 3, 4, 5
3, 4, 5
 

示例 3：

输入: [1,2,3,4,4,5]
输出: False
 

提示：

输入的数组长度范围为 [1, 10000]
'''
import collections
import heapq
from collections import defaultdict


class Solution:
    def isPossible(self, nums) -> bool:
        '''
        贪心算法，[1,2,3]=>[[3],[1,2,3]]=>[[3,4],[1,2,3]]=>[[3,4],[1,2,3,4]]
        :param nums:
        :return:
        '''
        res = []
        for u in nums:
            for v in res:
                if u == v[-1] + 1:
                    v.append(u)
                    break
            else:
                res.insert(0, [u])
        return all([len(v) >= 3 for v in res])

    def isPossible_heapd(self, nums):
        '''
        哈希表+最小堆，哈希表key为子序列最后一个数字，值为最小堆，最小堆的堆顶是子序列的最小长度
        :param nums:
        :return:
        '''
        chains = defaultdict(list)

        for i in nums:
            if not chains[i - 1]:
                heapq.heappush(chains[i], 1)
            else:
                min_len = heapq.heappop(chains[i - 1])
                heapq.heappush(chains[i], min_len + 1)
            # print(chains)

        for _, chain in chains.items():
            if chain and chain[0] < 3:
                return False
        return True

if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3, 3, 4, 4, 5]
    print(solution.isPossible_heapd(nums))
