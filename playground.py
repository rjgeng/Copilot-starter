import random
import copy 
# from models_practice import *

class Playground:
    "An object to represent a 2-Dimensional rectangular board"    
    def __init__(self, width=10, height=20, cell_item=None, grid=None):
        assert width is not None and height is not None
        assert type(width) == int and type(height) == int
        assert width >= 0 and height >= 0
        self.height = height
        self.width = width
        if grid:
            assert width * height == len(grid)
            self.grid = grid[:]
        else:
            self.grid = [cell_item for _ in range(width * height)]

    def get_height(self):
        return self.height

    def get_width(self):
        return self.width
    
    def update_grid(self, new_grid):
        assert len(new_grid) == len(self.grid), 'unequal grid lengths'
        self.grid = new_grid
    
    def __eq__(self, other):
        assert type(self) == type(other), 'Must compare two Board objects'
        return self.width == other.width and self.height == other.height and self.grid == other.grid

    def __repr__(self):
        return f'<Board width: {self.width} height: {self.height}>'

    def __str__(self):
        s = '=' * (self.width * 2 - 1) + '\n'
        for i, val in enumerate(self.grid):
            s += str(val)
            if (i + 1) % self.width != 0:
                s += ' '
            if (i + 1) % self.width == 0:
                s += '\n'
        s += '=' * (self.width * 2 - 1)
        return s
    
def pop_row(board,y):
    start_index = y * board.width
    before = board.grid[0:start_index]
    after = board.grid[start_index + board.width:]
    new_zero = [0 for _ in range(board.width)]
    new_grid = before + after + new_zero
    board.update_grid(new_grid)

def get_board_item(board, x, y):    
    return board.grid[board.get_width() * y + x]

def set_board_item(board, x, y, item):
    new_board = copy.deepcopy(board) 
    new_board.grid[board.get_width() * y + x] = item
    return new_board

def valid_coordinate(board, coordinate):
    return  0 <= coordinate[0] < board.get_height() and 0 <=  coordinate[1] < board.get_width()

def get_row(board, y):
    assert 0 <= y < board.height, f'Invalid y: {y}' # validating the row number
    return [get_board_item(board, x, y) for x in range(board.width)]
     
def check_row_full(board, y):   
   return all(list(0 if x == 0 else 1 for x in get_row(board, y)))