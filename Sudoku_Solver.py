__author__ = 'Daniel Sarmiento'

import numpy as np

def solveSudoku(puzzle):
    flag, row, col = findUnassignedLocation(puzzle)
    if not flag:
        return True
    for num in range(1, 10):
        if isSafe(puzzle, row, col, num):
            puzzle[row][col] = num
            if solveSudoku(puzzle):
                return True
            puzzle[row][col] = 0
    return False

def findUnassignedLocation(puzzle):
    for row in range(0, 9):
        for col in range(0, 9):
            if puzzle[row][col] == 0:
                return (True, row, col)
    return (False, 0, 0)

def usedInRow(puzzle, row, num):
    for col in range(0, 9):
        if puzzle[row][col] == num:
            return True
    return False

def usedInCol(puzzle, col, num):
    for row in range(0, 9):
        if puzzle[row][col] == num:
            return True
    return False

def usedInBox(puzzle, boxRow, boxCol, num):
    for row in range(0, 3):
        for col in range(0, 3):
            if puzzle[row + boxRow][col + boxCol] ==  num:
                return True
    return False

def isSafe(puzzle, row, col, num):
    return (not usedInRow(puzzle, row, num)) and (not usedInCol(puzzle, col, num)) and (not usedInBox(puzzle, row - row%3, col - col%3, num))

def printPuzzle(puzzle):
    for row in puzzle:
        print row
    return

def main():
    puzzle =[[0, 0, 0, 2, 6, 0, 7, 0, 1],
             [6, 8, 0, 0, 7, 0, 0, 9, 0],
             [1, 9, 0, 0, 0, 4, 5, 0, 0],
             [8, 2, 0, 1, 0, 0, 0, 4, 0],
             [0, 0, 4, 6, 0, 2, 9, 0, 0],
             [0, 5, 0, 0, 0, 3, 0, 2, 8],
             [0, 0, 9, 3, 0, 0, 0, 7, 4],
             [0, 4, 0, 0, 5, 0, 0, 3, 6],
             [7, 0, 3, 0, 1, 8, 0, 0, 0]]

    if solveSudoku(puzzle) == True:
        printPuzzle(puzzle)
    else:
        print "No solution exists"
    print "Done"

main()