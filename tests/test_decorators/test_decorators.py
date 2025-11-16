
import pytest
import os
from src.decorators.decorators import log


# Тест для вывода в консоль
def test_log_to_console(capsys):
    @log()
    def successful_function(x, y):
        return x + y

    successful_function(3, 4)
    captured = capsys.readouterr()
    assert "successful_function ok" in captured.out


def test_log_to_console_with_error(capsys):
    @log()
    def failing_function():
        raise ValueError("Test error")

    with pytest.raises(ValueError):
        failing_function()

    captured = capsys.readouterr()
    assert "failing_function error: ValueError" in captured.out
    assert "Inputs: (), {}" in captured.out


# Тест для записи в файл
@pytest.fixture
def log_file():
    filename = "test_log.txt"
    if os.path.exists(filename):
        os.remove(filename)
    yield filename
    if os.path.exists(filename):
        os.remove(filename)  # Удаляем после теста


def test_log_to_file_success(log_file):
    @log(filename=log_file)
    def my_function(a, b):
        return a * b

    my_function(2, 5)

    assert os.path.exists(log_file)
    with open(log_file, "r", encoding="utf-8") as f:
        content = f.read()
    assert "my_function ok" in content


def test_log_to_file_with_error(log_file):
    @log(filename=log_file)
    def broken_function():
        raise TypeError("Something went wrong")

    with pytest.raises(TypeError):
        broken_function()

    assert os.path.exists(log_file)
    with open(log_file, "r", encoding="utf-8") as f:
        content = f.read()
    assert "broken_function error: TypeError" in content
    assert "Inputs: (), {}" in content