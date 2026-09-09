class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def dfs(row: int, column: int, dist: int):
            if (
                row < 0
                or row >= len(grid)
                or column < 0
                or column >= len(grid[row])
                or grid[row][column] == -1
                or (dist > grid[row][column])
            ):
                return

            grid[row][column] = dist

            dfs(row - 1, column, dist + 1)
            dfs(row, column - 1, dist + 1)
            dfs(row + 1, column, dist + 1)
            dfs(row, column + 1, dist + 1)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    dfs(i, j, 0)