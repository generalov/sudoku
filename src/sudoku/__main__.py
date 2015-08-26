#!/usr/bin/env python
import argparse
import sys

from sudoku.players.BruteForceSudokuPlayer import BruteForceSudokuPlayer
from sudoku.formats.OpenSudokuFormat import OpenSudokuFormat
from sudoku.formats.TxtFormat import TxtFormat
from sudoku.loaders.ClassicalSudoku import ClassicalSudoku
from sudoku.loaders.UnsupportedVariantException import UnsupportedVariantException
from sudoku.output.SdkWriter import SdkWriter
from sudoku.output.TxtWriter import TxtWriter
from sudoku.SudokuGame import SudokuGame

__author__ = 'lucky'

game = SudokuGame()
game.register_game_variant('opensudoku', ClassicalSudoku(OpenSudokuFormat))
game.register_game_variant('txt', ClassicalSudoku(TxtFormat))
game.register_output('sdk', SdkWriter(sys.stdout))
game.register_output('txt', TxtWriter(sys.stdout))


def main(args=None):
    if args is None:
        args = sys.argv[1:]
    parser = argparse.ArgumentParser(description='Sudoku solver')
    parser.add_argument('-i', dest='sourcefile', action='store', required=True,
                        help='source file')
    parser.add_argument('-o', dest='output_format', action='store', choices=game.get_output_formats(), default='sdk',
                        help='output format')

    cfg = parser.parse_args(args)
    try:
        variant = SudokuGame.guess_variant(cfg.sourcefile)
    except UnsupportedVariantException:
        print 'File format {} is not supported'.format(cfg.sourcefile)
        sys.exit(1)

    player = BruteForceSudokuPlayer('Chuck Norris')
    game.set_player(player)
    game.set_output_format(cfg.output_format)
    game.set_game_variant(variant)
    game.set_source_file(cfg.sourcefile)
    game.run()


if __name__ == '__main__':
    main()
