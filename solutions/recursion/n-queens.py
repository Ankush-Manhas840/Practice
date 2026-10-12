class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        arr = [[False] * n for _ in range(n)]
        result = []

        def is_safe(row, col):
            # Check column above
            for r in range(row):
                if arr[r][col]:
                    return False

            # Check upper-left diagonal
            r, c = row - 1, col - 1
            while r >= 0 and c >= 0:
                if arr[r][c]:
                    return False
                r -= 1
                c -= 1

            # Check upper-right diagonal
            r, c = row - 1, col + 1
            while r >= 0 and c < n:
                if arr[r][c]:
                    return False
                r -= 1
                c += 1

            return True

        def checker(row):
            if row == n:
                result.append(["".join("Q" if cell else "." for cell in line) for line in arr])
                return

            for col in range(n):
                if is_safe(row, col):
                    arr[row][col] = True
                    checker(row + 1)
                    arr[row][col] = False

        checker(0)
        return result
