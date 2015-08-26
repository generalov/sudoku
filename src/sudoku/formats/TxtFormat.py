# coding=utf-8
__author__ = 'lucky'


class TxtFormat(object):
    """Простой формат где в каждоый строке файла записаны значения клеток.

    Строки, начинающиеся с символа # считаются комментариями и не
    участвуют в разборе.

    """

    def __init__(self, source):
        self.source = source

    def list(self):
        for line in self.source.readlines():
            line = line.strip()
            if line.startswith('#'):
                continue
            yield line
