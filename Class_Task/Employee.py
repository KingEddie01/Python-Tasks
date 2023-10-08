class Employee:
    Hourly_rate = 10

    def __init__(self, emp_firstName, emp_lastName, emp_department, emp_id):
        self.emp_fullName = emp_firstName + " " + emp_lastName
        self.salary = 0.0
        self.emp_department = emp_department
        self.total_hours_worked = 0
        self.emp_id = emp_id

    def calculate_emp_salary(self, total_hours_worked):
        self.total_hours_worked = total_hours_worked
        self.salary = self.Hourly_rate * self.total_hours_worked
        return self.salary

    def emp_assign_department(self, department):
        self.emp_department = department
        return self.emp_department

    def emp_assign_id(self, emp_id):
        self.emp_id = emp_id
        return self.emp_id

    def employee_details(self, emp_fullName, emp_department, emp_assign_id):
        self.emp_fullName = emp_fullName
        self.emp_department = emp_department
        self.emp_id = emp_assign_id
        return self.emp_fullName, self.emp_department, self.emp_id

    def get_employee_details(self):
        return self.emp_fullName + " " + self.emp_department + " " + self.emp_id

    def to_get_employee_salary(self):
        return self.salary
