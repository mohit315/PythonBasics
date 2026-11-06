"""Demonstrate indexing, insertion, and appending to lists."""


def insert_at(items: list[str | int], index: int, value: str) -> list[str | int]:
    """Return a copy with value inserted, leaving the original unchanged."""
    result = items.copy()
    result.insert(index, value)
    return result


def append_item(items: list[str | int], value: str) -> list[str | int]:
    """Return a new list with value appended."""
    return [*items, value]


def main() -> None:
    values: list[str | int] = [1, 2, "Mohit", 4, 5]
    print(f"Original: {values}")
    print(f"Index 3: {values[3]}")
    updated = insert_at(values, 3, "Adhiya")
    updated = append_item(updated, "End")
    print(f"Updated:  {updated}")
    print(f"Original remains unchanged: {values}")


if __name__ == "__main__":
    main()
