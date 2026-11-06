"""Conditions, loops, and basic input validation."""


def grade_label(score: int) -> str:
    """Return a simple grade label for scores from 0 to 100."""
    if not 0 <= score <= 100:
        raise ValueError("score must be between 0 and 100")
    if score >= 90:
        return "excellent"
    if score >= 70:
        return "good"
    if score >= 50:
        return "pass"
    return "try again"


def even_numbers(limit: int) -> list[int]:
    """Return non-negative even numbers smaller than limit."""
    return [number for number in range(limit) if number % 2 == 0]


def main() -> None:
    for score in (42, 75, 95):
        print(f"{score}: {grade_label(score)}")
    print(f"Even numbers below 10: {even_numbers(10)}")


if __name__ == "__main__":
    main()
