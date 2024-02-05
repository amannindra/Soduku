import random

def generate_grid():
    grid = []
    i = 0
    j = 0
    while i < 10:
        row = []
        while j < 10:
            num = random.randint(1, 9)
            if num in row:
                break
            else:
                row.append(num)
                j += 1
        grid.append(row)
        i += 1
    return grid 


print(generate_grid())        




