import random
import pygame

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

        


'''    def checkNumInWholeGrid(self, row, col, num):
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
'''

sudoku = Sudoku()
sudoku.create_grid()

# sudoku.makeSudokuGrid()
sudoku.print_grid()
