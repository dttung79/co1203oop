from w7_functions import add

# Test sum of 2 negatives
def test_add_01():
    a = -3
    b = -5
    expected = -8
    actual = add(a, b)

    assert expected == actual

# Test sum of 2 positives
def test_add_02():
    a = 3
    b = 5
    expected = 8
    actual = add(a, b)

    assert expected == actual

# Test sum of 1 positive and 1 negative
def test_add_03():
    a = 3
    b = -5
    expected = -2
    actual = add(a, b)

    assert expected == actual

# Test sum of 1 negative and 1 positive
def test_add_04():
    a = -3
    b = 5
    expected = 2
    actual = add(a, b)

    assert expected == actual

# Test sum of 0 and 0
def test_add_05():
    a = 0
    b = 0
    expected = 0
    actual = add(a, b)

    assert expected == actual