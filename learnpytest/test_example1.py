"""
naming convention -
test_method
test_filename

3 way of executing the code in pytest -
py.test
py.test -v -s filepath          # run all tests in spesific file_path
py.test -v -s test_mod.py       # run tests in module or in test file
py.test -v -s test_module.py::test_method    # only run test_method in test_module.py

-v : verbose - verbose is argument which is used to report more information about an operation in your program
-s : to print statements
"""

def test_methodA():
    print("this is method A")

def test_methodB():
    print("this is method B")