class Student:
    def __init__(self, name, dept, roll):
        self.name = name
        self.dept = dept
        self.roll = roll

    def show(self):
        print(f"Name: {self.name}, Department: {self.dept}, Roll: {self.roll}")


s1 = Student("Anirban", "Computer Science", 1)
s2 = Student("Mehuli", "IT", 2)
s3 = Student("Rahul", "Mechanical", 3)
s4 = Student("Priya", "Civil", 4)
s5 = Student("Sneha", "Electronics", 5)


s1.show()
s2.show()
s3.show()
s4.show()
s5.show()
