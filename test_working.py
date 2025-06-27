import pytest
from working import convert

def test_convert_12to24():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"

def test_convert_12to24_no_minutes():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_convert_invalid_time():
    with pytest.raises(ValueError):
        convert("12:60 AM to 5:00 PM")

def test_convert_invalid_format():
    with pytest.raises(ValueError):
        convert("9:00 AM - 5:00 PM")
