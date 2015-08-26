# coding=utf-8
from sudoku.rules.AbstractRule import AbstractRule

__author__ = 'lucky'


class RowRule(AbstractRule):
    """
    Правило: не должно быть одинаковых значений в одной строке.
    """

    def is_legal(self, board, cell, value):
        cells_in_same_row = board.iter_cells_by_row(board.get_cell_row(cell))
        taken = (cell.value for cell in board.take_all_filled_except_cell(
            cells_in_same_row, cell))
        res = value not in taken
        return res
