# coding=utf-8
import math


class SudokuBoard(object):
    """Игральная доска в Sudoku.

    :type cells: collections.Sized[SudokuCell]
    :type cell_value_rules: collections.Sized[AbstractRule]

    """

    def __init__(self, cells, rules):
        size = int(math.sqrt(len(cells)))
        self.cells = cells
        self.cell_value_rules = rules
        self.size = size
        assert self.size == 9
        assert len(self.cells) == self.size * self.size

    def assign(self, cell, value):
        """Записывает значение в клетку.

        :param cell: SudokuCell
        :param value: int
        :return: self

        """
        assert value in cell.POSSIBLE_VALUES and self.is_legal(cell, value)
        cell.assign(value)
        return self

    def clean(self, cell):
        """Записывает значение в клетку.

        :param cell: SudokuCell
        :return: self

        """
        cell.clean()
        return self

    def is_legal(self, cell, value):
        """Проверяет допустимость хода.

        Если запись значения value в указанную ячейку cell не противоречит ни какому из правил, возвращает True,
        иначе False.

        :param cell: SudokuCell
        :param value: int
        :return: boolean

        """
        res = all(rule.is_legal(self, cell, value)
                  for rule in self.cell_value_rules)
        return res

    def is_solved(self):
        """Возвращает True когда игра решена, иначе False.

        Игра заканчивается когда все клетки заполнены.

        :return: boolean

        """
        remains = len(list(self.take_empty_cells(self.iter_cells())))
        # print "Remains", remains
        return remains == 0

    def iter_cells(self):
        """Возвращает список всех клеток подряд.

        :return: collections.Iterable[SudokuCell]

        """
        return iter(self.cells)

    def iter_cell_region(self, col, row, width, height):
        """Возвращает итератор по прямоугольному диапазону ячеек с позиции
        (col, row), шириной width и высотой height.

        :param col: int
        :param row: int
        :param width: int
        :param height: int
        :return: collections.Iterable[SudokuCell]

        """
        if row < 0 or row + height > self.size:
            raise ValueError(row)
        if col < 0 or col + width > self.size:
            raise ValueError(col)

        for y in range(row, row + height):
            for x in range(col, col + width):
                idx = self.size * y + x
                yield self.cells[idx]

    def iter_cells_by_column(self, col):
        """Возвращает список всех клеток в столбце с индеком col.

        Индекс столбца col считается с нуля 0.

        :param col: int
        :return: collections.Iterable[SudokuCell]

        """
        if col < 0 or col >= self.size:
            raise ValueError(col)

        return self.iter_cell_region(col, 0, 1, self.size)

    def iter_cells_by_row(self, row):
        """Возвращает список всех клеток в строке с индексом row.

        Индекс строки row считается с нуля 0.

        :param row: int
        :return: collections.Iterable[SudokuCell]

        """
        if row < 0 or row >= self.size:
            raise ValueError(row)

        return self.iter_cell_region(0, row, self.size, 1)

    def get_cell_column(self, cell):
        """Врзвращает индекс столбца для указанной клетки.

        :param cell: SudokuCell
        :return: int

        """
        return cell.index % self.size

    def get_cell_row(self, cell):
        """Возвращает индекс строки для указанной клетки.

        :param cell: SudokuCell
        :return: int

        """
        return int(cell.index / self.size)

    def get_size(self):
        return self.size

    @staticmethod
    def take_all_filled_except_cell(it, cell):
        """Возвращает непустые клетки из итератора, кроме указанной.

        :type it: collections.Iterable[SudokuCell]
        :type cell: SudokuCell
        :return: collections.Iterable[SudokuCell]

        """
        return (c for c in it if c != cell and not c.is_empty())

    @staticmethod
    def take_empty_cells(it):
        """Возврщает только пустые клетки.

        :type it: collections.Iterable[SudokuCell]
        :return: collections.Iterable[SudokuCell]

        """
        return (c for c in it if c.is_empty())


class SudokuCell(object):
    """Клетка на доске Sudoku.

    :type index: int
    :type value: int

    """

    EMPTY_VALUE = object()
    POSSIBLE_VALUES = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def __init__(self, index, value=EMPTY_VALUE):
        """
        :type index: int
        :type value: int or Any
        :return:
        """
        self._index = index
        self._value = value

    @property
    def index(self):
        return self._index

    @property
    def value(self):
        return self._value

    def assign(self, value):
        """Установить значение клетки в value.

        :type value: int
        :return: self

        """
        if value not in self.POSSIBLE_VALUES:
            raise ValueError(value)

        self._value = value
        assert not self.is_empty()
        return self

    def clean(self):
        """Очистить клетку.

        :return: self

        """
        self._value = SudokuCell.EMPTY_VALUE
        assert self.is_empty()
        return self

    def is_empty(self):
        """Вернуть True если клетка пуста, иначе False.

        :return: boolean

        """
        return SudokuCell.EMPTY_VALUE is self._value
