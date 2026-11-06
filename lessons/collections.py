"""Lists, tuples, sets, and dictionaries."""


def unique_items(items: list[str]) -> list[str]:
    """Remove duplicates without changing the original order."""
    return list(dict.fromkeys(items))


def count_words(words: list[str]) -> dict[str, int]:
    """Count how many times each word occurs."""
    counts: dict[str, int] = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts


def main() -> None:
    languages = ["Python", "Go", "Python", "Rust"]
    print(f"List: {languages}")
    print(f"Unique, ordered: {unique_items(languages)}")
    print(f"Counts: {count_words(languages)}")
    print(f"Tuple: {('Python', 3)}")
    print(f"Set (unordered): {set(languages)}")


if __name__ == "__main__":
    main()
