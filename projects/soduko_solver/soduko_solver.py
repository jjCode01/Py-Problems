import numpy as np

class Soduko_Solver():
    def __init__(self, grid):
        self.grid = grid

    def check_num(self, num, pos_row, pos_col):

        # Check Row
        if num in self.grid[pos_row]:
            return False

        # Check Column
        for row in self.grid:
            if num == row[pos_col]:
                return False

        # Check 3x3 Square
        sqr_row = (pos_row // 3) * 3
        sqr_col = (pos_col // 3) * 3
        for row in self.grid[sqr_row:sqr_row + 3]:
            for col in row[sqr_col:sqr_col + 3]:
                if num == col:
                    return False

        return True


    def solve(self):
        for r in range(9):
            for c in range(9):
                if self.grid[r][c] == 0:
                    for num in range(1, 10):
                        if self.check_num(num, r, c):
                            self.grid[r][c] = num
                            self.solve()
                            self.grid[r][c] = 0
                    return
        print(np.matrix(self.grid))
        input("More?")

