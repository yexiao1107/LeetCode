'''
给你一个字符串s，以及该字符串中的一些「索引对」数组pairs，
其中pairs[i] =[a, b]表示字符串中的两个索引（编号从 0 开始）。

你可以 任意多次交换 在pairs中任意一对索引处的字符。

返回在经过若干次交换后，s可以变成的按字典序最小的字符串。

示例 1:

输入：s = "dcab", pairs = [[0,3],[1,2]]
输出："bacd"
解释：
交换 s[0] 和 s[3], s = "bcad"
交换 s[1] 和 s[2], s = "bacd"
示例 2：

输入：s = "dcab", pairs = [[0,3],[1,2],[0,2]]
输出："abcd"
解释：
交换 s[0] 和 s[3], s = "bcad"
交换 s[0] 和 s[2], s = "acbd"
交换 s[1] 和 s[2], s = "abcd"
示例 3：

输入：s = "cba", pairs = [[0,1],[1,2]]
输出："abc"
解释：
交换 s[0] 和 s[1], s = "bca"
交换 s[1] 和 s[2], s = "bac"
交换 s[0] 和 s[1], s = "abc"

提示：

1 <= s.length <= 10^5
0 <= pairs.length <= 10^5
0 <= pairs[i][0], pairs[i][1] <s.length
s中只含有小写英文字母

'''

##graph
import collections


class DisjointSetUnion:
    def __init__(self, n: int):
        self.n = n
        self.rank = [1] * n
        self.f = list(range(n))

    def find(self, x: int) -> int:
        if self.f[x] == x:
            return x
        self.f[x] = self.find(self.f[x])
        return self.f[x]

    def unionSet(self, x: int, y: int):
        fx, fy = self.find(x), self.find(y)
        if fx == fy:
            return
        if self.rank[fx] < self.rank[fy]:
            fx, fy = fy, fx
        self.rank[fx] += self.rank[fy]
        self.f[fy] = fx

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs) -> str:
        dsu = DisjointSetUnion(len(s))
        for x, y in pairs:
            dsu.unionSet(x, y)

        mp = collections.defaultdict(list)
        for i, ch in enumerate(s):
            mp[dsu.find(i)].append(ch)

        for vec in mp.values():
            vec.sort(reverse=True)

        ans = list()
        for i in range(len(s)):
            x = dsu.find(i)
            ans.append(mp[x][-1])
            mp[x].pop()

        return "".join(ans)

if __name__=="__main__":
    s = "dcab"
    pairs = [[0, 3], [1, 2], [0, 2]]
    solution = Solution()
    print(solution.smallestStringWithSwaps(s, pairs))