import pytest

__author__ = 'lucky'


@pytest.fixture
def opensudoku():
    return """<?xml version="1.0" encoding="UTF-8"?>
<opensudoku>
  <name>Gnome-Sudoku Easy</name>
  <author>romario333</author>
  <description></description>
  <comment></comment>
  <created>2009-09-16</created>
  <source>gnome-sudoku</source>
  <level>easy</level>
  <sourceURL>http://opensudoku.eu/puzzles</sourceURL>
  <game data="379000014060010070080009005435007000090040020000800436900700080040080050850000249" />
  <game data="070000810000318902281470005400060000690103027000090006900054681106982000057000040" />
</opensudoku>
"""
