import pytest

from DataTypeOperations import append_item, insert_at
from lessons.collections import count_words, unique_items
from lessons.control_flow import even_numbers, grade_label
from lessons.errors import parse_positive_int
from lessons.functions import average, greet
from lessons.variables import describe


def test_insert_at_does_not_mutate():
    original = [1, "Python"]
    assert insert_at(original, 1, "Go") == [1, "Go", "Python"]
    assert original == [1, "Python"]


def test_append_does_not_mutate():
    original = ["Python"]
    assert append_item(original, "Rust") == ["Python", "Rust"]
    assert original == ["Python"]


def test_insert_at_out_of_bounds_uses_list_semantics():
    assert insert_at(["A"], 100, "B") == ["A", "B"]


def test_unique_items_preserves_order():
    assert unique_items(["a", "b", "a", "c"]) == ["a", "b", "c"]


def test_unique_items_empty():
    assert unique_items([]) == []


def test_count_words():
    assert count_words(["go", "go", "python"]) == {"go": 2, "python": 1}


@pytest.mark.parametrize(
    ("score", "expected"),
    [(0, "try again"), (50, "pass"), (70, "good"), (90, "excellent"), (100, "excellent")],
)
def test_grade_label(score, expected):
    assert grade_label(score) == expected


@pytest.mark.parametrize("score", [-1, 101])
def test_grade_label_invalid(score):
    with pytest.raises(ValueError):
        grade_label(score)


def test_even_numbers():
    assert even_numbers(7) == [0, 2, 4, 6]
    assert even_numbers(-2) == []


def test_average():
    assert average([1, 2, 3]) == 2


def test_average_empty():
    with pytest.raises(ValueError):
        average([])


def test_greet():
    assert greet("Ada", excited=True) == "Hello, Ada!"


@pytest.mark.parametrize("text", ["0", "-3", "hello", "3.5"])
def test_parse_positive_int_invalid(text):
    with pytest.raises(ValueError):
        parse_positive_int(text)


def test_parse_positive_int_valid():
    assert parse_positive_int(" 42 ") == 42


def test_describe():
    assert describe(3) == "3 has type int"
