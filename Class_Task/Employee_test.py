from unittest import TestCase
from Class_Task.Employee import Employee


class EmployeeTest(TestCase):
    def setUp(self) -> None:
        self.employee = Employee("Edmund", "Udeh", "Software", "1234")

    def test_Employee_salary(self):
        self.employee.calculate_emp_salary(10)
        self.assertEqual(self.employee.salary, 100.0)

    def test_to_get_employee_details(self):
        self.employee.employee_details('Edmund Udeh', 'Software', '1234')
        check = 'Edmund Udeh Software 1234'
        self.assertEqual(self.employee.get_employee_details(), check)
