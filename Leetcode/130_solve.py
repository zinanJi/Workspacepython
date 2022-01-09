import collections


class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        row, col = len(board), len(board[0])

        def bfs(i, j):
            q = collections.deque()
            q.appendleft((i, j))
            while q:
                i, j = q.pop()
                if 0 <= i < row and 0 <= j < col and board[i][j] == "O":
                    board[i][j] = "A"
                    for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        q.appendleft((i + x, j + y))

        for j in range(col):
            if board[0][j] == "O":
                bfs(0, j)
            if board[row - 1][j] == "O":
                bfs(row - 1, j)

        for i in range(row):
            if board[i][0] == "O":
                bfs(i, 0)
            if board[i][col - 1] == "O":
                bfs(i, col - 1)

        for i in range(row):
            for j in range(col):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "A":
                    board[i][j] = "O"
