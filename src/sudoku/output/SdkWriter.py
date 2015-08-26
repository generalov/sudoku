__author__ = 'lucky'


class SdkWriter(object):

    def __init__(self, output):
        self.output = output
        self.eol = '\n'
        self.small_square_size = 3

    def write(self, board):
        cells = board.iter_cells()
        size = board.get_size()
        self.output.write(';{}x{}'.format(size, size))
        self.output.write(self.eol)
        self._write_hsep(size)
        for i in range(0, size):
            self._write_vsep()
            for j in range(0, size):
                cell = next(cells)
                value = cell.value if not cell.is_empty() else ' '
                self.output.write('%s' % value)
                self.output.write(' ')
                if (j + 1) % self.small_square_size == 0:
                    self._write_vsep()
            self.output.write(self.eol)
            if (i + 1) % self.small_square_size == 0:
                self._write_hsep(size)

    def _write_vsep(self):
        self.output.write('| ')

    def _write_hsep(self, size):
        self.output.write('+')
        for i in range(0, size * 2 + self.small_square_size):
            self.output.write('-')
            if (i + 1) % (self.small_square_size * 2 + 1) == 0:
                self.output.write('+')
        self.output.write(self.eol)
