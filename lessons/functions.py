"""Function parameters, return values, and type hints."""


def average(numbers: list[float]) -> float:
    """Calculate the arithmetic mean of a non-empty list."""
    if not numbers:
        raise ValueError("cannot average an empty list")
    return sum(numbers) / len(numbers)


def greet(name: str, *, excited: bool = False) -> str:
    """Show a keyword-only argument with a default."""
    ending = "!" if excited else "."
    return f"Hello, {name}{ending}"


def main() -> None:
    print(greet("Ada", excited=True))
    print(f"Average: {average([10, 20, 30])}")


if __name__ == "__main__":
    main()
