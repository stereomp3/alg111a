# content of test_sample.py
from factor import *
def test_factorial():
    assert factorial(5) == 120

if __name__ == '__main__':
    test_factorial()