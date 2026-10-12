class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        result = False
        def checker(row, col, i):
            nonlocal result
            if i == len(word):
                result = True
                return

            # up
            if row > 0:
                if board[row-1][col] == word[i]:
                    element = board[row-1][col]
                    board[row-1][col] = 0
                    checker(row-1, col, i+1)
                    board[row-1][col] = element

            # down
            if row < len(board) - 1:
                if board[row+1][col] == word[i]:
                    a = board[row+1][col]
                    board[row+1][col] = 0
                    checker(row+1, col, i+1)
                    board[row+1][col] = a

            # right
            if col < len(board[0]) - 1:
                if board[row][col+1] == word[i]:
                    b = board[row][col+1]
                    board[row][col+1] = 0
                    checker(row, col+1, i+1)
                    board[row][col+1] = b

            # left
            if col > 0:
                if board[row][col-1] == word[i]:
                    x = board[row][col-1]
                    board[row][col-1] = 0
                    checker(row, col-1, i+1)
                    board[row][col-1] = x

            return

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    y = board[row][col]
                    board[row][col] = 0
                    checker(row, col, 1)
                    board[row][col] = y
                    if result:
                        break

        return result
