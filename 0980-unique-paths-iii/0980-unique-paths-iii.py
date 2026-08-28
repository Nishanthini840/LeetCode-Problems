class Solution(object):

    def uniquePathsIII(self, grid):

        self.rows = len(grid)
        self.cols = len(grid[0])
        empty = 0
        start_row = 0
        start_col = 0

        for r in range(self.rows):
            for c in range(self.cols):

                if grid[r][c] == 0:
                    empty += 1

                if grid[r][c] == 1:
                    start_row = r
                    start_col = c

        return self.dfs(grid, start_row, start_col, empty)

    def dfs(self, grid, r, c, empty):

        if (r < 0 or r >= self.rows or
            c < 0 or c >= self.cols or
            grid[r][c] == -1):
            return 0

        if grid[r][c] == 2:
            if empty == 0:
                return 1
            return 0

        temp = grid[r][c]

        if grid[r][c] == 0:
            empty -= 1

        grid[r][c] = -1

        paths = (
            self.dfs(grid, r + 1, c, empty) +
            self.dfs(grid, r - 1, c, empty) +
            self.dfs(grid, r, c + 1, empty) +
            self.dfs(grid, r, c - 1, empty)
        )

        grid[r][c] = temp

        return paths
        