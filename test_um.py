import pytest
from um import count

def test_count_um():
    assert count("hello, um, world") == 1

def test_count_no_um():
    assert count("yummy") == 0

def test_count_multiple_um():
    assert count("um, hello, um, world") == 2

def test_count_um_case_insensitive():
    assert count("Um, hello, uM, world") == 2
