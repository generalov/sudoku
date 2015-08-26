from cStringIO import StringIO

from sudoku.formats.OpenSudokuFormat import OpenSudokuFormat

__author__ = 'lucky'


def test_should_list_games(opensudoku):
    game_collection = OpenSudokuFormat(StringIO(opensudoku))
    games = game_collection.list()
    assert len(list(games))== 2
