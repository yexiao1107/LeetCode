'''
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

 

示例：

s = "leetcode"
返回 0

s = "loveleetcode"
返回 2
'''


class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict = {}
        for item in s:
            dict[item] = dict.get(item, 0) + 1

        for i, item in enumerate(s):
            if dict[item] == 1:
                return i
        return -1


if __name__ == "__main__":
    s = "leetcode"
    solution = Solution()
    print(solution.firstUniqChar(s))
