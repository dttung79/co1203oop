from w8_fraction import Fraction

def test_fraction_01(capsys):
    f = Fraction(2, 3)
    f.show()
    expected = '2/3'
    actual = capsys.readouterr().out
    assert expected == actual

def test_fraction_02(capsys):
    f = Fraction(-2, -3)
    f.show()
    expected = '2/3'
    actual = capsys.readouterr().out
    assert expected == actual

def test_fraction_03(capsys):
    f = Fraction(-2, 3)
    f.show()
    expected = '-2/3'
    actual = capsys.readouterr().out
    assert expected == actual

def test_fraction_04(capsys):
    f = Fraction(2, -3)
    f.show()
    expected = '-2/3'
    actual = capsys.readouterr().out
    assert expected == actual

def test_fraction_05(capsys):
    f = Fraction(0, 3)
    f.show()
    expected = '0'
    actual = capsys.readouterr().out
    assert expected == actual

def test_fraction_06(capsys):
    f = Fraction(0, -3)
    f.show()
    expected = '0'
    actual = capsys.readouterr().out
    assert expected == actual

def test_fraction_07():
    try:
        f = Fraction(2, 0)
        assert False
    except ZeroDivisionError as e:
        assert str(e) == 'Denominator cannot be zero'
        assert True
    except Exception:
        assert False

def test_fraction_08():
    try:
        f = Fraction(-2, 0)
        assert False
    except ZeroDivisionError as e:
        assert str(e) == 'Denominator cannot be zero'
        assert True
    except Exception:
        assert False

def test_fraction_09():
    try:
        f = Fraction(0, 0)
        assert False
    except ZeroDivisionError as e:
        assert str(e) == 'Denominator cannot be zero'
        assert True
    except Exception:
        assert False