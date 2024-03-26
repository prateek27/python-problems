import unittest
from student import Student, sort_students

class TestSortStudents(unittest.TestCase):
    def test_sort_students(self):
        student1 = Student("Alice", 85)
        student2 = Student("Bob", 75)
        student3 = Student("Charlie", 85)
        student4 = Student("David", 90)

        students = [student1, student2, student3, student4]

        sorted_students = sort_students(students)

        # Ensure the sorted_students list has the correct length
        self.assertEqual(len(sorted_students), 4)

        # Ensure the students are sorted by marks first, then by name if marks are equal
        expected_order = ["Bob", "Alice", "Charlie", "David"]
        actual_order = [student.name for student in sorted_students]
        self.assertEqual(actual_order, expected_order)

if __name__ == "__main__":
    unittest.main()