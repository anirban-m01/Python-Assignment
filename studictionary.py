student = {
    1: {"name": "Amit", "dept": "CSE", "marks": 85},
    2: {"name": "Riya", "dept": "ECE", "marks": 92},
    3: {"name": "Ranit", "dept": "IT", "marks": 76},
    4: {"name": "Mehuli", "dept": "CSE", "marks": 95},
    5: {"name": "Anirban", "dept": "CSE", "marks": 88},
  }

# a. Sort according to marks highest to lowest
# b. Print the student with maximum marks
# c. Find average marks of the student
# d. Print the students who scored more than average marks

sorted_students = dict(sorted(student.items(), key=lambda x: x[1]['marks'], reverse=True))
print("Sorted by marks:", sorted_students)

top_student = max(student.items(), key=lambda x: x[1]['marks'])
print("Topper:", top_student)

avg_marks = sum(s['marks'] for s in student.values()) / len(student)
print("Average marks:", avg_marks)

above_avg = {roll: info for roll, info in student.items() if info['marks'] > avg_marks}
print("Students above average:", above_avg)
