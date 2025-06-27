from numb3rs import validate

def main():
    test_format()
    test_range()
    test_invalid_characters()

def test_format():
    assert validate('1.2.3.4') == True
    assert validate('1.2.3') == False
    assert validate('1.2') == False
    assert validate('1') == False
    assert validate('1.2.3.4.5') == False
    assert validate('') == False

def test_range():
    assert validate('255.255.255.255') == True
    assert validate('0.0.0.0') == True
    assert validate('256.255.255.255') == False
    assert validate('255.256.255.255') == False
    assert validate('255.255.256.255') == False
    assert validate('255.255.255.256') == False
    assert validate('275.3.6.28') == False
    assert validate('192.168.1.1') == True
    assert validate('10.0.0.1') == True

def test_invalid_characters():
    assert validate('a.b.c.d') == False
    assert validate('123.456.789.0') == False
    assert validate('192.168.one.1') == False
    assert validate('192.168.1.1abc') == False

if __name__ == "__main__":
    main()
