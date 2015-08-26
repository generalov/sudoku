# coding=utf-8
import lxml.etree

__author__ = 'lucky'


class OpenSudokuFormat(object):
    """Фоомат OpenSudoku.

    Используется в gnome-sudoku.

    """

    def __init__(self, source):
        """
        :param source: file
        """
        self.doc = lxml.etree.parse(source).getroot()

    def list(self):
        for game_node in self.doc.xpath('/opensudoku/game'):
            gamestr = game_node.get('data').strip()
            yield gamestr
