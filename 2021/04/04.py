from aocd.models import Puzzle
from aocd import submit
# from aocd import numbers
from aocd import lines
from copy import copy

puzzle = Puzzle(2021, 4)

import math

class BingoBoard:
    def __init__(self, board):
        self.board = board
        self.dim = int(math.sqrt(len(board)))
        self.num2grid = {n:idx for idx, n in enumerate(board)}
        self.grid2num = {idx:int(n) for idx, n in enumerate(board)}
        self.grid = [False] * len(board)
        self.last_num = None
        self.won = False
    
    def apply(self, n):
        self.last_num = int(n)
        idx = self.num2grid.get(n, -1)
        if idx >= 0:
            self.grid[idx] = True
    
    def isWin(self):
        if self.won:
            return self.won
        won = False
        for n in range(self.dim):
            # horizontal
            won = won or \
                all([self.grid[self.dim * n + idx] for idx in range(self.dim)])
            # verticle
            won = won or \
                all([self.grid[self.dim * idx + n] for idx in range(self.dim)])
        # # Diagonals don't count
        # won = won or \
        #     all([self.grid[n * (self.dim + 1)] for n in range(self.dim)])
        # won = won or \
        #     all([self.grid[n * (self.dim - 1)] for n in range(1, self.dim + 1)])
        self.won = won
        return won
    
    def score(self):
        return self.last_num * sum([self.grid2num[idx] for idx, marked in enumerate(self.grid) if not marked])
    
    def printGrid(self):
        out = ''
        for i in range(len(self.board)):
            out += 'X' if self.grid[i] else 'O'
            if (i + 1) % self.dim == 0:
                out += '\n'
        print(out)
    
    def printBoard(self):
        out = ''
        for i in range(len(self.board)):
            out += f'{self.grid2num[i]:2d} ' if not self.grid[i] else 'XX '
            if (i + 1) % self.dim == 0:
                out += '\n'
        print(out)

    def __str__(self):
        out = ''
        for i in range(len(self.board)):
            out += f'{self.grid2num[i]:2d} ' if not self.grid[i] else 'XX '
            if (i + 1) % self.dim == 0:
                out += '\n'
        return out
    
    def __repr__(self):
        return self.__str__()


def checkBoards(boards):
    winner_boards = []
    for board in boards:
        if board.isWin():
            winner_boards.append(board)
    return winner_boards, [board for board in boards if not board.won]

called_nums = lines.pop(0).split(',')
lines.pop(0)
boards = []
board = []
for line in lines:
    if line.strip() == '':
        boards.append(BingoBoard(board))
        board = []
        continue
    else:
        board += [x for x in line.strip().split(' ') if x != ""]

if len(board) != 0:
    boards.append(BingoBoard(board))

winning_boards = []
for idx, num in enumerate(called_nums):
    for board in boards:
        board.apply(num)
    # Can't win without 5 numbers called
    if idx > 4:
        new_winning_boards, boards = checkBoards(boards)
        winning_boards += new_winning_boards
        # if len(winner_boards) == 1:
        #     winner = winner_boards[0]
        #     score = winner.score()
        #     print()
        #     winner.printBoard()
        #     print(winner.last_num, score)
        #     break
        # elif len(winner_boards) > 1:
        #     print("Multiple winning boards")

# submit(winning_boards[0].score(), part="a")
# submit(winning_boards[-1].score(), part="b")