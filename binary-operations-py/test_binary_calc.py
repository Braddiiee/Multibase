import pytest
from operations import arithmetic, evaluate_signed

# --------------------------
# Arithmetic Tests
# --------------------------

def test_addition(capsys):
    arithmetic(5, "+", 3)
    captured = capsys.readouterr()
    assert "Result (decimal): 8" in captured.out

def test_subtraction(capsys):
    arithmetic(10, "-", 4)
    captured = capsys.readouterr()
    assert "Result (decimal): 6" in captured.out

def test_multiplication(capsys):
    arithmetic(7, "*", 2)
    captured = capsys.readouterr()
    assert "Result (decimal): 14" in captured.out

def test_division_integer(capsys):
    arithmetic(8, "/", 2)
    captured = capsys.readouterr()
    assert "Result (decimal): 4.0" in captured.out

def test_division_float_problem():
    with pytest.raises(TypeError):
        # bin() cannot handle floats -> should raise error
        arithmetic(7, "/", 2)

def test_invalid_operator_defaults_to_division(capsys):
    # Any operator not + - * defaults to /
    arithmetic(9, "%", 3)
    captured = capsys.readouterr()
    assert "Result (decimal)" in captured.out


# --------------------------
# Type Safety Tests
# --------------------------

def test_string_inputs_fail():
    with pytest.raises(TypeError):
        arithmetic("1011", "+", "1111")

def test_mixed_types_fail():
    with pytest.raises(TypeError):
        arithmetic(5, "+", "3")


# --------------------------
# Signed Evaluation Tests
# --------------------------

def test_evaluate_signed_positive():
    binary, is_negative = evaluate_signed("0111")
    assert binary == "111"
    assert is_negative is False

def test_evaluate_signed_negative():
    binary, is_negative = evaluate_signed("1111")
    assert binary == "111"
    assert is_negative is True

def test_evaluate_signed_empty():
    binary, is_negative = evaluate_signed("")
    # Should just return empty string, False
    assert binary == ""
    assert isinstance(is_negative, bool)


# --------------------------
# Edge Case Tests
# --------------------------

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        arithmetic(5, "/", 0)

def test_large_numbers(capsys):
    arithmetic(2**10, "+", 2**10)
    captured = capsys.readouterr()
    assert "Result (decimal): 2048" in captured.out

def test_binary_output_matches_decimal(capsys):
    arithmetic(5, "+", 3)  # Expect 8 -> binary 1000
    captured = capsys.readouterr()
    assert "Result (binary): 1000" in captured.out

