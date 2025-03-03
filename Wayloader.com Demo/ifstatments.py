students = {
    "Alice": [85, 90, 92],
    "Bob": [78, 80, 85],
    "Charlie": [88, 87, 85]
}

for student, grades in students.items():
    avg_grade = sum(grades) / len(grades)
    print(f"{student}'s average grade: {avg_grade:.2f}")
