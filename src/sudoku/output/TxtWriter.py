__author__ = 'lucky'


class TxtWriter(object):

    def __init__(self, output):
        self.output = output
        self.eol = '\n'

    def write(self, board):
        cells = board.iter_cells()
        self.output.write(
            ''.join([str(cell.value) if not cell.is_empty() else '0' for cell in cells]))
        self.output.write(self.eol)
