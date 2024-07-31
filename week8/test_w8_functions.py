from w8_functions import hello

# To CAPture SYStem output, we use capsys fixture
def test_hello_01(capsys):
    hello('Alice', 20)
    captured = capsys.readouterr()
    expected = 'Hello, I am Alice and I am 20 years old\n'
    actual = captured.out
    assert expected == actual

def test_hello_02(capsys):
    hello('Alice', 75)
    captured = capsys.readouterr()
    expected = 'Hello, I am Alice and I am 75 years old\n'
    actual = captured.out
    assert expected == actual

def test_hello_03(capsys):
    hello('Alice', 120)
    captured = capsys.readouterr()
    expected = 'Hello, I am Alice and I am 120 years old\n'
    actual = captured.out
    assert expected == actual