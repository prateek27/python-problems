import unittest
import io
from unittest.mock import patch

class User:
    def __init__(self, username, email):
        self._username = username
        self._email = email

    def displayInfo(self):
        print(f"Username: {self._username}")
        print(f"Email: {self._email}")

    def getUsername(self):
        return self._username

    def getEmail(self):
        return self._email


class Student(User):
    def __init__(self, username, email, studentId, course):
        super().__init__(username, email)
        self._studentId = studentId
        self._course = course

    def displayInfo(self):
        super().displayInfo()
        print(f"Student ID: {self._studentId}")
        print(f"Course: {self._course}")

    def getStudentId(self):
        return self._studentId

    def getCourse(self):
        return self._course


class Employee(User):
    def __init__(self, username, email, employeeId, department):
        super().__init__(username, email)
        self._employeeId = employeeId
        self._department = department

    def displayInfo(self):
        super().displayInfo()
        print(f"Employee ID: {self._employeeId}")
        print(f"Department: {self._department}")

    def getEmployeeId(self):
        return self._employeeId

    def getDepartment(self):
        return self._department


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User("test_user", "test@example.com")

    def test_displayInfo(self):
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            self.user.displayInfo()
            self.assertEqual(mock_stdout.getvalue(), "Username: test_user\nEmail: test@example.com\n")

    def test_getUsername(self):
        self.assertEqual(self.user.getUsername(), "test_user")

    def test_getEmail(self):
        self.assertEqual(self.user.getEmail(), "test@example.com")


class TestStudent(unittest.TestCase):
    def setUp(self):
        self.student = Student("test_student", "student@example.com", "S123", "Computer Science")

    def test_displayInfo(self):
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            self.student.displayInfo()
            self.assertEqual(mock_stdout.getvalue(),
                             "Username: test_student\nEmail: student@example.com\nStudent ID: S123\nCourse: Computer Science\n")

    def test_getStudentId(self):
        self.assertEqual(self.student.getStudentId(), "S123")

    def test_getCourse(self):
        self.assertEqual(self.student.getCourse(), "Computer Science")


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee("test_employee", "employee@example.com", "E456", "Human Resources")

    def test_displayInfo(self):
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            self.employee.displayInfo()
            self.assertEqual(mock_stdout.getvalue(),
                             "Username: test_employee\nEmail: employee@example.com\nEmployee ID: E456\nDepartment: Human Resources\n")

    def test_getEmployeeId(self):
        self.assertEqual(self.employee.getEmployeeId(), "E456")

    def test_getDepartment(self):
        self.assertEqual(self.employee.getDepartment(), "Human Resources")


if __name__ == '__main__':
    unittest.main()