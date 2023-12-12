import pytest

# @pytest.fixture()
# def setUp(): # Whatever name
#     print("before a method")

@pytest.fixture(scope='module') # Scope Module, akan di jalankan sebelum semua method dijalankan dan setelah semua method selesai
def beforeClass(): # Whatever name
    print("before a CLASS")
    yield
    print("after CLASS")

@pytest.fixture() # Sedangkan secara default, akan di jalankan setiap eacb method dan setelah method tersebut
def setUp(): # Whatever name
    print("before a METHOD")
    yield
    print("after METHOD")

@pytest.fixture()
def lala():
    print("LALA")
    yield
    print("LALA YIELD")

def test_methodA(beforeClass, setUp, lala):
    print("this is method A")

def test_methodB(beforeClass, setUp):
    print("this is method B")