student = {
    "name": "Alice",
    "age": 21,
    "course": "Computer Science",
    "grades": [85, 90, 92]
}
student["name"] = "Bob"
del student["age"]
print(student)

student = student.pop("grades")
print(student)