# coding=utf-8
__author__ = 'lucky'


class BruteForceSudokuPlayer(object):
    """Простой, но упорный игрок в Sudoku. Играет перебором всех вариантов, до.

    самого конца.

    Начинает играть с первой попавшейся непустой клетки и пробует подставлять в неё все возможные значения подряд.
    Если значение подходит, тогда записывает его в клетку и переходит к следующей непустой клетке.
    Игра закончится когда на доске не останется ни одной пустой клетки.

    Если Игрок заходит в тупик - на доске остались пустые клетки, но ни какой вариант не подходит - он откатывается
    на ход назад и пробует другое подходящее значение.

    Не самая быстрая стратегия. Зато в ней есть рекурсия, а рекусрии, как известно - божественны. ;)

    :type nickname: str

    """

    def __init__(self, nickname):
        """У каждого игрока должен быть ник. Никаких исключений.

        :type nickname: str

        """
        self._nickname = nickname

    @property
    def nickname(self):
        return self._nickname

    def play(self, board):
        res = self._guess_solution(board)
        return res

    def _guess_solution(self, board):
        """
        :type board: sudoku.SudokuBoard.SudokuBoard
        :return: boolean
        """
        solution_found = False
        if board.is_solved():
            solution_found = True
        else:
            cell = next(board.take_empty_cells(board.iter_cells()))
            # print 'cell', cell.index
            possible_values = iter(cell.POSSIBLE_VALUES)
            end_of_data = object()
            trial_value = next(possible_values, end_of_data)
            while (not solution_found) and trial_value is not end_of_data:
                # print 'trial value', trial_value,
                if board.is_legal(cell, trial_value):
                    board.assign(cell, trial_value)
                    if self._guess_solution(board):
                        solution_found = True
                        continue
                    else:
                        # print 'rollback', cell.index, cell.value
                        board.clean(cell)
                trial_value = next(possible_values, end_of_data)
                # print '++', trial_value
        return solution_found
