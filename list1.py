sudoku_puzzle = [
    [5, 3, 0, 0, 7, 0, 6, 0, 8],
    [6, 0, 0, 1, 9, 0, 0, 0, 7],
    [9, 9, 8, 3, 5, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 6, 8, 3, 9, 2, 8, 1],
    [7, 0, 3, 0, 2, 0, 5, 0, 6],
    [1, 6, 9, 5, 4, 0, 2, 8, 0],
    [0, 0, 7, 4, 1, 9, 0, 0, 5],
    [3, 4, 5, 0, 8, 0, 0, 7, 9]
]

def check_row(number, row):
    if number in sudoku_puzzle[row]:
        print("It is in Row")
def check_column(number, column):
    for row in sudoku_puzzle:
        if row[column] == number:
            print("It is in Column")


check_row(5,0)




