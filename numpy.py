import numpy as np

marks = np.array([
    [50, 85, 90],
    [60, 95, 35],
    [70, 65, 68],
    [85, 55, 65],
    [45, 35, 35]
])

print("Maximum marks:", np.max(marks))

print("Minimum marks:", np.min(marks))

print("Average marks:", np.mean(marks))


student_id = np.argmax(marks[:, 1])
print("Student ID with maximum marks in Subject 1:", student_id)
print("Marks:", marks[student_id, 1])

print("Maximum marks subject-wise:", np.max(marks, axis=0))

print("Average marks subject-wise:", np.mean(marks, axis=0))
