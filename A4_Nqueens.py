def is_safe(board, row, col):
    n = len(board)
    # Check left in the same row
    for i in range(col):
        if board[row][i] == 1:
            return False
    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    # Check lower left diagonal
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve_n_queens_util(board, col, n):
    if col == n:
        return True
    for i in range(n):
        if is_safe(board, i, col):
            board[i][col] = 1
            if solve_n_queens_util(board, col + 1, n):
                return True
            board[i][col] = 0
    return False

def print_solution(board):
    for row in board:
        print(row)

def solve_n_queens(n):
    board = [[0] * n for _ in range(n)]
    if not solve_n_queens_util(board, 0, n):
        print("Solution does not exist")
        return False
    print_solution(board)
    return True

solve_n_queens(8)
