__author__ = 'Daniel Sarmiento'

# Backtracking function
def solveSudoku(puzzle):
    flag, row, col = findUnassignedLocation(puzzle)

    # If all cells are filled return true
    if not flag:
        return True

    # Try all numbers for the cell
    for num in range(1, 10):
        # If number can be put in cell do so
        if isSafe(puzzle, row, col, num):
            puzzle[row][col] = num
            # Call backtracking function
            if solveSudoku(puzzle):
                return True
            # If puzzle wasn't solved try a new number
            puzzle[row][col] = 0
    # Puzzle can not be solved
    return False

# Finding an box with 0, return a tuple if found and location
def findUnassignedLocation(puzzle):
    for row in range(0, 9):
        for col in range(0, 9):
            if puzzle[row][col] == 0:
                return (True, row, col)
    return (False, -1, -1)

# Is number in row
def usedInRow(puzzle, row, num):
    for col in range(0, 9):
        if puzzle[row][col] == num:
            return True
    return False

# Is number in col
def usedInCol(puzzle, col, num):
    for row in range(0, 9):
        if puzzle[row][col] == num:
            return True
    return False

# Is number in box
def usedInBox(puzzle, boxRow, boxCol, num):
    for row in range(0, 3):
        for col in range(0, 3):
            if puzzle[row + boxRow][col + boxCol] ==  num:
                return True
    return False

# Can the number go in the cell
def isSafe(puzzle, row, col, num):
    return (not usedInRow(puzzle, row, num)) and (not usedInCol(puzzle, col, num)) and (not usedInBox(puzzle, row - row%3, col - col%3, num))

# Print the sudoku puzzle
def printPuzzle(puzzle):
    for x in range(0, 9):
        if x%3 == 0:
            print "|-----------------------|"
        for y in range(0, 9):
            if y%3 == 0:
                print "|",
            if puzzle[x][y] != 0:
                print puzzle[x][y],
            else:
                print " ",
            if y == 8:
                print "|"

    print "|-----------------------|"
    return

def main():
    # Unsolved puzzle
    puzzle =[[8, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 3, 6, 0, 0, 0, 0, 0],
             [0, 7, 0, 0, 9, 0, 2, 0, 0],
             [0, 5, 0, 0, 0, 7, 0, 0, 0],
             [0, 0, 0, 0, 4, 5, 7, 0, 0],
             [0, 0, 0, 1, 0, 0, 0, 3, 0],
             [0, 0, 1, 0, 0, 0, 0, 6, 8],
             [0, 0, 8, 5, 0, 0, 0, 1, 0],
             [0, 9, 0, 0, 0, 0, 4, 0, 0]]

    # Print before puzzle
    print "Before:"
    printPuzzle(puzzle)
    print

    # Solve the puzzle
    print "After:"
    if solveSudoku(puzzle) == True:
        printPuzzle(puzzle)
    else:
        print "No solution exists"
    print "Done"

main()