"""Validate a student's mark and display the corresponding result."""


def validate_mark(value):
    """Return the result message for a mark, or an input error message."""
    try:
        mark = float(value)
    except (TypeError, ValueError):
        return "Invalid numeric input"

    # Marks outside the inclusive 0-100 range are not eligible for a result.
    if not 0 <= mark <= 100:
        return "Invalid input"

    if mark >= 75:
        return "Grade boundary reached"
    if mark >= 40:
        return "Pass"
    return "Fail"


def main():
    # Read text first so invalid numeric input can be reported without crashing.
    entered_mark = input("Enter student marks: ")
    print(validate_mark(entered_mark))


if __name__ == "__main__":
    main()