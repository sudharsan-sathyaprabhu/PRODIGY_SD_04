# Define the size of the Sudoku grid (9x9)
N = 9

# Function to print the Sudoku grid
def print_grid(grid):
    for row in grid:
        print(row)

# Function to check if it's safe to place a number in a specific position
def is_safe(grid, row, col, num):
    # Check if the number is already in the row
    for x in range(N):
        if grid[row][x] == num:
            return False

    # Check if the number is already in the column
    for x in range(N):
        if grid[x][col] == num:
            return False

    # Check if the number is already in the 3x3 box
    start_row, start_col = row - row % 3, col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + start_row][j + start_col] == num:
                return False

    return True

# Function to solve the Sudoku puzzle using backtracking
def solve_sudoku(grid):
    for row in range(N):
        for col in range(N):
            # Find an empty cell (denoted by 0)
            if grid[row][col] == 0:
                # Try placing numbers 1-9 in the empty cell
                for num in range(1, N + 1):
                    if is_safe(grid, row, col, num):
                        grid[row][col] = num

                        # Recursively attempt to solve the puzzle
                        if solve_sudoku(grid):
                            return True

                        # Backtrack if the solution is not valid
                        grid[row][col] = 0

                return False

    return True

# Input Sudoku puzzle (0 represents empty cells)
puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Solve the puzzle and display the result
if solve_sudoku(puzzle):
    print("Sudoku puzzle solved:")
    print_grid(puzzle)
else:
    print("No solution exists")
