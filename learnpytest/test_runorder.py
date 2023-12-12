import pytest

@pytest.mark.run(order=4)
def test_methodA():
    print("method A")

@pytest.mark.run(order=3)
def test_methodB():
    print("method B")

@pytest.mark.run(order=1)
def test_methodC():
    print("method C")

@pytest.mark.run(order=2)
def test_methodD():
    print("method D")