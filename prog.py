def calculate_grade(mark):
    if mark >= 90:
        return "A"
    if mark >= 80:
        return "B"
    if mark >= 70:
        return "C"
    if mark >= 60:
        return "D"
    return "F"


students = []

for student_number in range(1, 6):
    name = input(f"Enter the name of student {student_number}: ").strip()

    while True:
        mark_input = input(f"Enter {name}'s mark (0-100): ")
        try:
            mark = float(mark_input)
        except ValueError:
            print("Invalid input. Please enter a numeric mark.")
            continue

        if not 0 <= mark <= 100:
            print("Mark must be between 0 and 100. Please try again.")
            continue

        students.append((name, mark, calculate_grade(mark)))
        break

print("\nStudent Results")
print(f"{'Name':<20}{'Mark':>10}{'Grade':>10}")
print("-" * 40)
for name, mark, grade in students:
    print(f"{name:<20}{mark:>10.1f}{grade:>10}")
