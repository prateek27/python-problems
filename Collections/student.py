"""Create a class student, write a python method to sort students acoording to marks.
If marks are equal then sort according to name, both in ascending order"""

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

def sort_students(students):
    #todo
    sorted_students = sorted(students, key=lambda x: (x.marks, x.name))
    return sorted_students

# Example usage:
student1 = Student("Alice", 85)
student2 = Student("Bob", 75)
student3 = Student("Charlie", 85)
student4 = Student("David", 90)

students = [student1, student2, student3, student4]

sorted_students = sort_students(students)
for student in sorted_students:
    print(f"Name: {student.name}, Marks: {student.marks}")