class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # O(N * M) complexity, O(N) space

        # store the numbers of paths to get to cell (X.Y), we only need to cache 1 row at a time
        # For any cell in the first row, it only takes 1 path to get there (the robot only moves right)
        pathRow = [1] * n 

        # We will iterate for m - 1 rows, and n - 1 cols, starting at indices 1 for both rows and columns, because 
        # the results for the first row and first column are already determined (only 1 path to get to those cells)

        # During every iteration, the unique paths to get to the current cell Row,Col is the sum of the unique
        # paths of cell Row,Col-1 (the cell to the left) and cell Row-1,Col (the cell above), because the robot can
        # only move right (robot moves right from the previous left cell to get here) or the robot moves down
        # (robot moves down from the previous above cell to get here).
        for i in range(1, m):
            # Initialize all cells for the current row by 1
            # the cell at column 0 has only 1 path to get there (robot can only move down)
            # the other cells' values will be overwritten during iteration
            newPathRow = [1] * n 
            for j in range(1, n):
                # newPathRow[j-1] is cell to the left, pathRow[j] is the cell above
                newPathRow[j] = newPathRow[j-1] + pathRow[j]
            pathRow = newPathRow
        return pathRow[-1] # return the last element in pathRow, this should be cell m-1,n-1