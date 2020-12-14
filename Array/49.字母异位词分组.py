'''
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:

输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
说明：

所有输入均为小写字母。
不考虑答案输出的顺序。

'''


class Solution:
    def groupAnagrams(self, strs):
        '''
        dict的key必须为不可变元素，利用dict的默认减少ifelse
        :param strs:
        :return:
        '''
        dict = {}
        for s in strs:
            key = tuple(sorted(s))
            dict[key] = dict.get(key, []) + [s]
        return list(dict.values())

if __name__ == "__main__":
    input = ["eat", "tea", "tan", "ate", "nat", "bat"]
    solution = Solution()
    print(solution.groupAnagrams(input))
