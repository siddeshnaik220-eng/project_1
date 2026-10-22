"""Collect marks for five students and display a grade report."""

STUDENT_COUNT = 5
SUBJECTS = ("Maths", "Science", "English", "Social Studies", "Computer")
MAX_MARK = 100


def is_valid_mark(mark):
    """Check that a mark is between 0 and 100, inclusive."""
    return 0 <= mark <= MAX_MARK


def grade_for(percentage):
    """Assign a grade using the specified percentage boundaries."""
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


def get_mark(subject):
    """Prompt again until a valid numeric mark is entered."""
    while True:
        try:
            mark = float(input(f"  {subject} marks (0-100): "))
        except ValueError:
            print("  Invalid input. Please enter a number.")
            continue

        if is_valid_mark(mark):
            return mark
        print("  Mark must be between 0 and 100.")


def main():
    # Keep one result tuple per student for the final report.
    results = []

    for student_number in range(1, STUDENT_COUNT + 1):
        name = input(f"\nEnter the name of student {student_number}: ").strip()
        if not name:
            name = f"Student {student_number}"

        marks = []
        for subject in SUBJECTS:
            marks.append(get_mark(subject))

        total = sum(marks)
        percentage = total / len(SUBJECTS)
        results.append((name, total, percentage, grade_for(percentage)))

    # Display each student's total, percentage, and grade in aligned columns.
    maximum_total = len(SUBJECTS) * MAX_MARK
    print("\nSTUDENT MARKS REPORT")
    print("-" * 66)
    print(f"{'Name':<22}{'Total':>12}{'Percentage':>18}{'Grade':>9}")
    print("-" * 66)
    for name, total, percentage, grade in results:
        print(
            f"{name:<22}{total:>8.1f}/{maximum_total:<3}"
            f"{percentage:>14.2f}%{grade:>9}"
        )
    print("-" * 66)


if __name__ == "__main__":
    main()