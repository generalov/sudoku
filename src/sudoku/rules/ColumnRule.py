# coding=utf-8
from sudoku.rules.AbstractRule import AbstractRule

__author__ = 'lucky'


class ColumnRule(AbstractRule):
    """
    Правило: не должно быть одинаковых значений в одном столбце.
    """

    def is_legal(self, board, cell, value):
        cells_in_same_column = board.iter_cells_by_column(
            board.get_cell_column(cell))
        taken = (cell.value for cell in board.take_all_filled_except_cell(
            cells_in_same_column, cell))
        res = value not in taken
        return res
