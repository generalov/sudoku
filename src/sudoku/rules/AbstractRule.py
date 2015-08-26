# coding=utf-8
from abc import ABCMeta, abstractmethod

__author__ = 'lucky'


class AbstractRule(object):
    """Правило игры в Sudoku."""
    __metaclass__ = ABCMeta

    @abstractmethod
    def is_legal(self, board, cell, value):
        """Возвращает True если допустимо записать указанное значение value в.

        ячейку cell на доске board, иначе False.

        :type board: sudoku.SudokuBoard.SudokuBoard
        :type cell: sudoku.SudokuBoard.SudokuCell
        :type value: int
        :return: boolean

        """
        pass
