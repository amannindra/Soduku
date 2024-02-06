import random
import pygame
from list1 import sudoku_puzzle
'''
WIDTH = 550
background_color = (251, 247, 245)

def main ( ):
    pygame.init
    win = pygame.display.set_mode((WIDTH, WIDTH))
    pygame.display.set_caption ("Sudoku")
    while True:
        for event in pygame.event.get():
            if event.type == pygame. QUIT:
                pygame.quit
                return
main()
'''


class SudokuSolve:
    def __init__(self, grid):
        self.check_grid = list(map(list, grid))
        self.grid = list(map(list, grid))
        self.num = 0

    def check_row(self, number, rows):
        if number in self.grid[rows]:
            return True
        return False

    def check_col(self, number, column):
        for row in sudoku_puzzle:
            if row[column] == number:
                return True
        return False

    def check_around(self, row, col, number):
        for i in range(row//3*3, row//3*3+3):
            for j in range(col//3*3, col//3*3+3):
                if number == self.grid[i][j]:
                    return True
        return False

    def print_grid(self):
        for row in range(9):
            print(self.grid[row])

    def check_full(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid)):
                if self.grid[i][j] == 0:
                    return True
        return False

    def check(self):
        if self.grid == self.check_grid:
            return True
        return False

    def main(self):
        print(self.num)
        self.print_grid()
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                for i in range(9):
                    if not (self.check_row(i+1, row) and self.check_col(i+1, col) and self.check_around(row, col, i+1)):
                        self.grid[row][col] = i

        if (self.check_full() and self.num < 100):
            print("--------------------------------------------------------")
            self.num += 1
            if (self.check()):
                print("There is a difference")
            else:
                print("There is no difference")
            self.main()



print(sudoku_puzzle)

Solve = SudokuSolve(sudoku_puzzle)
Solve.main()


'''        




class Sudoku:
    def __init__(self):
        self.grid = []

    def create_grid(self):
        num = list()
        for row in range(9):
            num2 = []
            for col in range(9):
                num2.append(0)
            self.grid.append(num2)

    def print_grid(self):
        for row in range(9):
            print(self.grid[row])

    def check_amount(self, num):
        amount = 0
        for row in range(9):
            for col in range(9):
                if self.grid[row][col] == num:
                    amount += 1
        if (amount < 10):
            return False
        else:
            return True

    def column(self, colum, number):
        for col in self.grid[colum]:
            if self.grid[colum][col] == number:
                return True

    def rows(self, rowm, number):
        if number in self.grid[rowm]:
            return True
        else:
            return False

 #   def make(self):

        


     def checkNumInWholeGrid(self, row, col, num):
        for ncol in range(9):
            if self.grid[row][ncol] == num:
                return False
        for nrow in range(9):
            if self.grid[nrow][col] == num:
                return False
        return True



    def checkSubGrid(self):
        pass



    def makeSudokuGrid(self):
        numlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        #numlist = []
        #for i in range(9):
         ##
        #      numlist.append(mylist[j])              
        random.shuffle(numlist)
        for row in range(9):
            for col in range(9):
                    for num in numlist:
                        if self.checkNumInWholeGrid(row, col, num):
                            self.grid[row][col] = num


sudoku = Sudoku()
sudoku.create_grid()

# sudoku.makeSudokuGrid()
sudoku.print_grid()
'''
