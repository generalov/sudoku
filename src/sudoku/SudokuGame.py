import os.path

from sudoku.loaders.UnsupportedVariantException import UnsupportedVariantException

__author__ = 'lucky'


class SudokuGame(object):

    def __init__(self):
        self._variants = {}
        self._outputs = {}
        self._output = None
        self._variant = None
        self._player = None
        self._source_file = None

    def register_game_variant(self, name, loader):
        self._variants[name] = loader

    def register_output(self, name, fmt):
        self._outputs[name] = fmt

    def set_output_format(self, value):
        self._output = value

    def set_game_variant(self, value):
        if value not in self._variants:
            raise UnsupportedVariantException(value)
        self._variant = value

    def set_player(self, player):
        self._player = player

    def set_source_file(self, value):
        self._source_file = value

    def run(self):
        with open(self._source_file) as f:
            loader = self._get_loader(self._variant)
            for board in loader.read_boards(f):
                self._player.play(board)
                if board.is_solved():
                    self._get_output().write(board)
                else:
                    pass

    def _get_output(self):
        return self._outputs[self._output]

    def _get_loader(self, fmt):
        if fmt not in self._variants:
            raise UnsupportedVariantException(fmt)
        return self._variants[fmt]

    @staticmethod
    def guess_variant(filename):
        return os.path.splitext(filename)[1][1:]

    def get_variants(self):
        return self._variants.keys()

    def get_output_formats(self):
        return self._outputs.keys()
