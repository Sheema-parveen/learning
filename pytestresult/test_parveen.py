import pytest
from parveen import Add
from parveen import Mul

#test case1:
def test_add_1():
    assert Add(3,5) == 8

#test case2:
def test_add_2():
    assert Add(3,5)==2