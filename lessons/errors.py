"""Validate user input and raise meaningful exceptions."""


def parse_positive_int(text: str) -> int:
    """Parse a positive whole number, or raise ValueError."""
    try:
        value = int(text)
    except ValueError as exc:
        raise ValueError("enter a whole number") from exc
    if value <= 0:
        raise ValueError("number must be positive")
    return value


def main() -> None:
    for text in ("12", "-4", "oops"):
        try:
            print(f"{text!r} -> {parse_positive_int(text)}")
        except ValueError as exc:
            print(f"{text!r} -> {exc}")


if __name__ == "__main__":
    main()
