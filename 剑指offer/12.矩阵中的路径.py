'''
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一格开始，每一步可以在矩阵中向左、右、上、下移动一格。
如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。
例如，在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字母用加粗标出）。

[["a","b","c","e"],
["s","f","c","s"],
["a","d","e","e"]]

但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个字符b占据了矩阵中的
第一行第二个格子之后，路径不能再次进入这个格子。


示例 1：

输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true
示例 2：

输入：board = [["a","b"],["c","d"]], word = "abcd"
输出：false

提示：

1 <= board.length <= 200
1 <= board[i].length <= 200
'''


class Solution:
    def exist(self, board, word: str) -> bool:
        def dfs(board, word, i, j, index):
            if i >= len(board) or i < 0 or j >= len(board[0]) or j < 0 or board[i][j] != word[index]:
                return False
            if index == len(word) - 1:
                return True
            board[i][j] = ""
            res = dfs(board, word, i + 1, j, index + 1) or dfs(board, word, i - 1, j, index + 1) or \
                  dfs(board, word, i, j + 1, index + 1) or dfs(board, word, i, j - 1, index + 1)
            board[i][j] = word[index]
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if (dfs(board, word, i, j, 0)):
                    return True
        return False

if __name__=="__main__":
    solution = Solution()
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    print(solution.exist(board,word))
