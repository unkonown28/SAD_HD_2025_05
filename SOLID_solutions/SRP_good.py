class Employee:
    def __init__(self, name):
        self.name = name

class SalaryCalculator:
    def calculate(self, employee):
        print(f"Calculating salary for {employee.name}")

class EmployeeRepository:
    def save(self, employee):
        print(f"Saving {employee.name} to the database")
