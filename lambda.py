student = {
    "A1": {"name": "Akash", "dept": "CSE", "marks": 85},
    "A2": {"name": "Mehu", "dept": "AIML", "marks": 92},
    "A3": {"name": "Asish", "dept": "ECE", "marks": 78},
    "A4": {"name": "Ani", "dept": "CSE", "marks": 88},
    "A5": {"name": "Rima", "dept": "AIML", "marks": 75}
}

# a. Sort according to marks highest to lowest
sorted_student = dict(
    sorted(student.items(), key=lambda x: x[1]["marks"], reverse=True)
)

print("Students sorted by marks:")
for roll, details in sorted_student.items():
    print(roll, details)


# b. Print the student with maximum marks
maximum = max(student.items(), key=lambda x: x[1]["marks"])

print("\nStudent with maximum marks:")
print(maximum)


# c. Find average marks
total = sum(map(lambda x: x["marks"], student.values()))
average = total / len(student)

print("\nAverage marks:", average)


# d. Print students who scored more than average
print("\nStudents scoring more than average:")
for roll, details in student.items():
    if details["marks"] > average:
        print(roll, details)