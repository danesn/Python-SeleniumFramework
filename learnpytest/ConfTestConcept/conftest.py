import pytest

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