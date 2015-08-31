from sudoku.rules.ColumnRule import ColumnRule
from sudoku.rules.RowRule import RowRule
from sudoku.rules.SmallSquareRule import SmallSquareRule
from sudoku.SudokuBoard import SudokuBoard, SudokuCell

__author__ = 'lucky'


class ClassicalSudoku(object):

    def __init__(self, fmt_class):
        self._fmt_class = fmt_class

    def read_boards(self, source_file):
        game_collection = self._fmt_class(source_file)
        rules = self.get_rules()
        for game_description in game_collection.list():
            d = [int(x) for x in game_description]
            cells = [SudokuCell(i, value) if value in SudokuCell.POSSIBLE_VALUES else SudokuCell(i)
                     for i, value in enumerate(d)]
            board = SudokuBoard(cells, rules)
            yield board

    def get_rules(self):
        rules = [
            RowRule(),
            ColumnRule(),
            SmallSquareRule()
        ]
        return rules
