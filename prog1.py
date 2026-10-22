"""Collect marks for five students and print a grade report."""

STUDENT_COUNT = 5
SUBJECTS = ["Maths", "Science", "English", "Social Studies", "Computer"]
MAX_MARK = 100


def is_valid_mark(mark):
    """Return True only when a mark is between 0 and 100, inclusive."""
    return 0 <= mark <= MAX_MARK


def grade_for(percentage):
    """Return a grade using the cutoffs: 90, 80, 70, 60, and 40 percent."""
    if percentage >= 90:
        return "A"
    if percentage >= 80:
        return "B"
    if percentage >= 70:
        return "C"
    if percentage >= 60:
        return "D"
    if percentage >= 40:
        return "E"
    return "F"


def get_mark(student_name, subject):
    """Keep asking until the user enters a valid number from 0 to 100."""
    while True:
        try:
            mark = float(input(f"  {subject} marks (0-100): "))
        except ValueError:
            print("  Invalid input. Enter a number, such as 75 or 82.5.")
            continue

        if is_valid_mark(mark):
            return mark
        print("  Marks must be between 0 and 100.")


def main():
    # Save one summary row for each student's marks.
    results = []

    for student_number in range(1, STUDENT_COUNT + 1):
        name = input(f"\nEnter the name of student {student_number}: ").strip()
        if not name:
            name = f"Student {student_number}"

        marks = []
        for subject in SUBJECTS:
            marks.append(get_mark(name, subject))

        total = sum(marks)
        percentage = total / len(SUBJECTS)
        results.append((name, total, percentage, grade_for(percentage)))

    # Print the results in aligned columns for easy comparison.
    print("\nSTUDENT MARKS REPORT")
    print("-" * 68)
    print(f"{'Name':<22}{'Total':>12}{'Percentage':>16}{'Grade':>10}")
    print("-" * 68)
    for name, total, percentage, grade in results:
        print(
            f"{name:<22}{total:>9.1f}/{len(SUBJECTS) * MAX_MARK:<3}"
            f"{percentage:>13.2f}%{grade:>10}"
        )
    print("-" * 68)


if __name__ == "__main__":
    main()
