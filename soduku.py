def print_grid(grid) :
    for row in grid :
        print(" ".join(str(num) if num != 0 else '.' for num in row))


def find_empty_location(grid) :
    for i in range(9) :
        for j in range(9) :
            if grid[i][j] == 0 :
                return i, j
    return None


def is_valid(grid, row, col, num) :
    # Check the row
    if num in grid[row] :
        return False

    # Check the column
    for i in range(9) :
        if grid[i][col] == num :
            return False

    # Check the 3x3 box
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3) :
        for j in range(start_col, start_col + 3) :
            if grid[i][j] == num :
                return False

    return True


def solve_sudoku(grid) :
    empty_location = find_empty_location(grid)
    if not empty_location :
        return True  # No more empty locations, puzzle solved

    row, col = empty_location

    for num in range(1, 10) :
        if is_valid(grid, row, col, num) :
            grid[row][col] = num
            if solve_sudoku(grid) :
                return True
            grid[row][col] = 0  # Backtrack

    return False


def input_grid() :
    print("Enter the Sudoku grid row by row. Use 0 for empty cells.")
    grid = []
    for i in range(9) :
        while True :
            try :
                row = list(map(int, input(f"Enter row {i + 1}: ").strip().split()))
                if len(row) != 9 or any(num < 0 or num > 9 for num in row) :
                    raise ValueError
                grid.append(row)
                break
            except ValueError :
                print("Invalid input. Please enter 9 integers between 0 and 9.")
    return grid


def main() :
    sudoku_grid = input_grid()

    print("\nUnsolved Sudoku:")
    print_grid(sudoku_grid)

    if solve_sudoku(sudoku_grid) :
        print("\nSolved Sudoku:")
        print_grid(sudoku_grid)
    else :
        print("No solution exists.")


if __name__ == "__main__" :
    main()
