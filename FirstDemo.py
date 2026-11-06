"""First Python examples: values, variables, and types."""


def main() -> None:
    print("hello")
    number = 3
    message = "hello world"
    integer_value, decimal_value, description = 3, 4.5, "Great"

    print(number)
    print(message)
    print(f"{integer_value} + {decimal_value} = {integer_value + decimal_value} ({description})")
    print(f"Value is {integer_value}")
    for value in (integer_value, decimal_value, description):
        print(type(value).__name__)


if __name__ == "__main__":
    main()
