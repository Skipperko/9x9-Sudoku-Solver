def print_sudoku(puzzle):
    for i in range(9):
        if i % 3 == 0:
            print("+-------+-------+-------+")
        for j in range(9):
            if j % 3 == 0:
                print("|", end=" ")
            if puzzle[i][j] == 0:
                print(".", end=" ")
            else:
                print(puzzle[i][j], end=" ")
        print("|")
    print("+-------+-------+-------+")

def is_valid_move(puzzle, row, col, num):
    return (
        all(puzzle[row][i] != num for i in range(9)) and
        all(puzzle[i][col] != num for i in range(9)) and
        all(
            puzzle[r][c] != num
            for r in range(row - row % 3, row - row % 3 + 3)
            for c in range(col - col % 3, col - col % 3 + 3)
        )
    )

def find_empty_cell(puzzle):
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == 0:
                return row, col
    return None

def solve():
    empty_cell = find_empty_cell(puzzle)
    if not empty_cell:
        return True

    row, col = empty_cell
    for num in range(1, 10):
        if is_valid_move(puzzle, row, col, num):
            puzzle[row][col] = num
            if solve():
                return True
            puzzle[row][col] = 0

    return False

def sudoku(puzzle):
    if solve():
        print_sudoku(puzzle)
    else:
        return None
    
puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

sudoku(puzzle)