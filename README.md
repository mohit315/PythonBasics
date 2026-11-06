# Python Basics

Small, runnable Python lessons and exercises, with automated tests.

## Getting started

Python 3.11 or newer is recommended.

```bash
python FirstDemo.py
python DataTypeOperations.py
python -m lessons.variables
python -m lessons.collections
python -m lessons.control_flow
python -m lessons.functions
python -m lessons.errors
```

The lessons use only the Python standard library. To run tests and checks:

```bash
python -m pip install -e ".[dev]"
python -m pytest
ruff check .
ruff format --check .
```

## Learning path

| Lesson | Topic | What you will learn |
| --- | --- | --- |
| `lessons/variables.py` | Variables | Types, names, f-strings |
| `lessons/collections.py` | Collections | Lists, tuples, sets, dictionaries |
| `lessons/control_flow.py` | Control flow | Conditions and loops |
| `lessons/functions.py` | Functions | Arguments, returns, type hints |
| `lessons/errors.py` | Errors | Validation and exceptions |

Each lesson has runnable examples. The `tests/` directory checks behavior and edge cases.

## Practice

Try these changes before looking at the tests:

1. Add a floating-point value to `FirstDemo.py` and print its type.
2. Change `insert_at` to insert at the start of a list.
3. Extend `grade_label` to return a distinct label for scores of 100.
4. Add a test for an empty list in `unique_items`.
5. Build a small CLI program using the functions in these lessons.

## Contributing

Keep examples small, readable, and compatible with Python 3.11+. Add tests for new behavior, run the checks above, and explain why each change helps someone learning Python.

## Scope

This is a beginner learning repository, not a complete Python curriculum. More topics and projects can be added incrementally.
