# This is my first Coding Project. It is a Sudoku Solver using the backtracing method.


# checks if the inserted num is correct and all of the constraints are fullfilled.
def isValid(grid, num, row, column):
   return checkRow(grid, num, row, column) & checkColumn(grid, num, row, column) & checkSquare(grid, num, row, column);


def checkRow(grid, num, row, column):
    # checks the constraints inside a certain row.
    for i in range(0, len(grid[0])):
        if grid[row][i] == num and column != i:
            return False;
    return True;


def checkColumn(grid, num, row, column):
    # checks the constraints inside a certain column.
    for i in range(0, len(grid)):
        if grid[i][column] == num and row != i:
            return False;
    return True;


def checkSquare(grid, num, row, column):
    # checks the constraints inside a certain 3 x 3 block.

    # 3 x 3 blocks:
    quadrantR = row // 3;
    quadrantC = column // 3;
    
    for i in range(quadrantR * 3, ((quadrantR + 1) * 3)):
        for j in range(quadrantC * 3, ((quadrantC + 1) * 3)):
            if grid[i][j] == num and i != row and j != column:
                return False;
    return True;

def emptyPos(grid):
    # finds the next available empty position, which is loaded with a zero.
    for i in range(0, len(grid)):
        for j in range(0, len(grid)):
            if grid[i][j] == 0:
                return (i, j);
    return None;
    
def solve(grid):
    # main method, which is solving the sudoku
    pos = emptyPos(grid)
    if not pos:
        return True;
    else:
        row, column = pos;

    for i in range(1, 10):
        if isValid(grid, i, row, column):
            grid[row][column] = i;
            if solve(grid):
                return True;

            grid[row][column] = 0;
    return False;

def print_grid(grid):
    # method to print a given grid formatted in the console.
    for i in range(0, len(grid)):
        if i % 3 == 0 and i != 0:
            print("-----------------------");

        for j in range(0, len(grid[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="");

            if j == len(grid) - 1:
                print(grid[i][j]);
            else:
                print(str(grid[i][j]) + " ", end="");


# This is a testing grid, just comment all of the code below out to test.
"""

grid = [
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 6, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 9, 0, 2, 0, 0],
        [0, 5, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 4, 5, 7, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 3, 0],
        [0, 0, 1, 0, 0, 0, 0, 6, 8],
        [0, 0, 8, 5, 0, 0, 0, 1, 0],
        [0, 9, 0, 0, 0, 0, 4, 0, 0]
        ];


solve(grid)
print_grid(grid);

"""