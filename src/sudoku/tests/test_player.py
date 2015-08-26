from cStringIO import StringIO

from sudoku.players.BruteForceSudokuPlayer import BruteForceSudokuPlayer
from sudoku.formats.OpenSudokuFormat import OpenSudokuFormat
from sudoku.loaders.ClassicalSudoku import ClassicalSudoku

__author__ = 'lucky'


def test_player(opensudoku):
    loader = ClassicalSudoku(OpenSudokuFormat)
    board = next(loader.read_boards(StringIO(opensudoku)))
    player = BruteForceSudokuPlayer('Hero')
    res = player.play(board)
    assert res is True
