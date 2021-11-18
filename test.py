from calculator import Calc
ca = Calc()
def test_multiply_positive_test():
    x = 3
    y = 3
    result = 9
    assert ca.multiply(x, y) == result, f'Проверка умножения провалена :( (введёный пример {x}*{y}={result})'
def test_multiply_negative_test():
    assert ca.multiply(3, 3) != 8
def test_adding_positive_test():
    x = 15
    y = 15
    result = 30
    assert ca.add(x, y) == result, f'Проверка сложения провалена :( (введёный пример {x}*{y}={result})'
def test_adding_negative_test():
    assert ca.add(5, 5) != 30
def test_division_positive_test():
    x = 49
    y = 7
    result = 7
    assert ca.div(x, y) == result, f'Проверка деления провалена :( (введёный пример {x}*{y}={result})'
def test_division_negative_test():
    assert ca.div(49, 7) != 9
def test_subtraction_positive():
    x = 150
    y = 25
    result = 125
    assert ca.sub(x, y) == result, f'Проверка вычитания провалена :( (введёный пример {x}*{y}={result})'
def test_subtraction_negative():
    assert ca.sub(150, 25) != 100
