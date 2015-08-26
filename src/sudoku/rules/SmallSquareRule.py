# coding=utf-8
from sudoku.rules.AbstractRule import AbstractRule

__author__ = 'lucky'


class SmallSquareRule(AbstractRule):
    """
    Правило: не должно быть одинаковых значений в пределах малого квадрата.
    """
    # TODO: рассказать, что такое малый квадрат.

    def __init__(self, side_length=3):
        self.side_length = side_length

    def is_legal(self, board, cell, value):
        col = board.get_cell_column(cell)
        row = board.get_cell_row(cell)
        square_col = int(col - col % self.side_length)
        square_row = int(row - row % self.side_length)
        cells_in_same_square = board.iter_cell_region(
            square_col, square_row, self.side_length, self.side_length)
        taken = (cell.value for cell in board.take_all_filled_except_cell(
            cells_in_same_square, cell))
        res = value not in taken
        return res
