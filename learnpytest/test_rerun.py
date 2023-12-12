"""
command:
pytest -v -s --reruns {number_rerun} --reruns-delay {number_delay} {1 module or entire module}

rerun EACH METHOD yang fail akan di coba {number_rerun} sebelum ke method selanjutnya

"""

import pytest


@pytest.mark.flaky(reruns=5, reruns_delay=2)
def test_methodOne():
    var1 = 1
    var2 = 2
    assert var1 == var2


def test_methodTwo():
    var1 = "popo"
    var2 = "lala"
    assert var1 == var2

@pytest.mark.flaky(reruns=2, reruns_delay=2)
def test_methodThree():
    var1 = "lala"
    var2 = "loka"
    assert var1 == var2

def test_methodFour():
    var1 = "lala"
    var2 = "lala"
    assert var1 == var2

def test_methodFive():
    var1 = "lala"
    var2 = "lala"
    assert var1 == var2