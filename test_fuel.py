import pytest
from fuel import convert, gauge

def test_convert_valid_fraction():
    assert convert("1/2") == 50

def test_convert_invalid_format():
    with pytest.raises(ValueError):
        convert("1/2/3")

def test_convert_non_integer_values():
    with pytest.raises(ValueError):
        convert("1.5/2")

def test_convert_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_convert_percentage_out_of_range():
    with pytest.raises(ValueError):
        convert("2/1")

def test_gauge_empty():
    assert gauge(0) == "E"

def test_gauge_full():
    assert gauge(100) == "F"

def test_gauge_percentage():
    assert gauge(50) == "50%"

def test_gauge_one_percent():
    assert gauge(1) == "E"

def test_gauge_ninety_nine_percent():
    assert gauge(99) == "F"

