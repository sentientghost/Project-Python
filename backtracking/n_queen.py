class solution:
    def __init__(self):
        self.location = []

    def nQueen(self, n):
        for i in range(n):
            board = [[0 for _ in range(n)] for _ in range(n)]
            board[i][0] = 1
            self.solve_nQueen(board, 1)

        return (self.location)

    def solve_location(self, board):
        location = [0]*len(board)
        for i in range(len(board)):
            for j in range(len(board)):
                if (board[i][j] == 1):
                    location[j] = i+1
        return location

    def solve_nQueen(self, board, col):
        flag = False
        if (col >= len(board)):
            self.location.append(self.solve_location(board))
            return True

        for i in range(len(board)):
            if (self.validate(board, i, col) == True):
                board[i][col] = 1

                flag = self.solve_nQueen(board, col+1) or flag

                board[i][col] = 0

        return flag

    def validate(self, board, row, col):
        for i in range(col):
            if (board[row][i] == 1):
                return False

        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if (board[i][j] == 1):
                return False

        for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
            if (board[i][j] == 1):
                return False

        return True
