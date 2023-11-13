def is_safe(board, row, col, n):
    # Check if a queen can be placed at board[row][col]
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(n):
    board = [[0] * n for _ in range(n)]
    solutions = []

    def backtrack(col):
        if col == n:
            solutions.append([row[:] for row in board])
            return

        for i in range(n):
            if is_safe(board, i, col, n):
                board[i][col] = 1
                backtrack(col + 1)
                board[i][col] = 0

    backtrack(0)
    return solutions

def solve_n_queens_with_csp(n):
    solutions = solve_n_queens(n)
    valid_solutions = []
    for solution in solutions:
        if all(sum(row) == 1 for row in solution) and all(sum(row) == 1 for row in zip(*solution)):
            valid_solutions.append(solution)
    return valid_solutions

n = int(input("Enter the board size (n): "))
solutions = solve_n_queens_with_csp(n)

print(f"Number of solutions for {n}-Queens: {len(solutions)}\n")

for idx, solution in enumerate(solutions, 1):
    print(f"Solution {idx}:")
    for row in solution:
        print(" ".join(["Q" if cell == 1 else "." for cell in row]))
    print("\n")
