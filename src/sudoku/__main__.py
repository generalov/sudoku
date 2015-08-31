#!/usr/bin/env python

"""Sudoku solver."""

from __future__ import print_function

import signal
import sys

from sudoku import _version
from sudoku.formats.OpenSudokuFormat import OpenSudokuFormat
from sudoku.formats.TxtFormat import TxtFormat
from sudoku.loaders.ClassicalSudoku import ClassicalSudoku
from sudoku.loaders.UnsupportedVariantException import UnsupportedVariantException
from sudoku.output.SdkWriter import SdkWriter
from sudoku.output.TxtWriter import TxtWriter
from sudoku.players.BruteForceSudokuPlayer import BruteForceSudokuPlayer
from sudoku.SudokuGame import SudokuGame

__author__ = 'lucky'

game = SudokuGame()
game.register_game_variant('opensudoku', ClassicalSudoku(OpenSudokuFormat))
game.register_game_variant('txt', ClassicalSudoku(TxtFormat))
game.register_output('sdk', SdkWriter(sys.stdout))
game.register_output('txt', TxtWriter(sys.stdout))


def _main(argv, standard_out, standard_error):
    import argparse
    parser = argparse.ArgumentParser(
        description=__doc__, prog='sudoku', version=_version.get_versions()['version'])
    parser.add_argument('-i', dest='sourcefile', action='store', required=True,
                        help='source file')
    parser.add_argument('-o', dest='output_format', action='store', choices=game.get_output_formats(), default='sdk',
                        help='output format')

    cfg = parser.parse_args(argv[1:])

    try:
        variant = SudokuGame.guess_variant(cfg.sourcefile)
    except UnsupportedVariantException:
        print('File format {} is not supported'.format(
            cfg.sourcefile), file=standard_error)
        return 1

    player = BruteForceSudokuPlayer('Chuck Norris')
    game.set_player(player)
    game.set_game_variant(variant)
    game.set_source_file(cfg.sourcefile)
    game.set_output_format(cfg.output_format)
    game.run()
    return 0


def main():
    """Main entry point."""
    try:
        # Exit on broken pipe.
        signal.signal(signal.SIGPIPE, signal.SIG_DFL)
    except AttributeError:  # pragma: no cover
        # SIGPIPE is not available on Windows.
        pass

    try:
        return _main(sys.argv,
                     standard_out=sys.stdout,
                     standard_error=sys.stderr)
    except KeyboardInterrupt:  # pragma: no cover
        return 2  # pragma: no cover


if __name__ == '__main__':
    sys.exit(main())
