import subprocess

__author__ = 'lucky'


def test_should_be_runnable():
    exit_code = subprocess.call(['sudoku'])
    assert exit_code == 0

def test_should_display_help_message(capfd):
    subprocess.call(['sudoku'])
    out, err = capfd.readouterr()
    assert 'Help' in out
