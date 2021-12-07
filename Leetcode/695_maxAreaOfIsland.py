class Solution(object):
    # 函数的调用实现深度优先遍历
    # 另一种方式是通过栈存放接下来想要遍历的土地
    # 还有一种方式是使用队列实现广度优先遍历
    def dfs(self, grid, cur_i, cur_j):
        if cur_i < 0 or cur_j < 0 or cur_i == len(grid) or cur_j == len(
                grid[0]) or grid[cur_i][cur_j] != 1:
            return 0
        grid[cur_i][cur_j] = 0
        ans = 1
        for mx, my in ([0, 1], [0, -1], [1, 0], [-1, 0]):
            next_i, next_j = cur_i + mx, cur_j + my
            ans += self.dfs(grid, next_i, next_j)
        return ans

    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = 0
        for i, l in enumerate(grid):
            for j, n in enumerate(l):
                ans = max(self.dfs(grid, i, j), ans)
        return ans
