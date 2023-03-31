
from soduko_solver import Soduko_Solver

grid = [[3, 6, 0, 4, 5, 1, 7, 2, 0],
         [0, 0, 0, 0, 0, 2, 0, 0, 4],
         [4, 0, 2, 6, 3, 7, 0, 0, 0],
         [0, 0, 1, 0, 0, 0, 5, 0, 0],
         [0, 0, 4, 5, 1, 8, 2, 0, 3],
         [0, 0, 0, 0, 9, 0, 4, 6, 0],
         [2, 0, 0, 0, 7, 0, 0, 5, 0],
         [0, 7, 0, 1, 0, 0, 3, 0, 2],
         [0, 0, 5, 0, 0, 0, 0, 0, 7]]

game = Soduko_Solver(grid)

game.solve()
