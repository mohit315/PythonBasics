"""Variables, numeric types, and readable string formatting."""


def describe(value: object) -> str:
    """Describe the type of a value without relying on print side effects."""
    return f"{value!r} has type {type(value).__name__}"


def main() -> None:
    name = "Ada"
    completed = 3
    total = 5
    print(f"{name} completed {completed} of {total} exercises.")
    for value in (name, completed, 2.5, True, None):
        print(describe(value))


if __name__ == "__main__":
    main()
