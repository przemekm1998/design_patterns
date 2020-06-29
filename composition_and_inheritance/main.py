import json

from employees import EmployeeDatabase
from hr import PayrollSystem
from productivity import ProductivitySystem


class Main:

    @staticmethod
    def main():
        for employee in EmployeeDatabase().employees:
            Main.print_dict(employee.to_dict())
        # productivity_system = ProductivitySystem()
        # payroll_system = PayrollSystem()
        # employee_database = EmployeeDatabase()
        # employees = employee_database.employees
        # productivity_system.track(employees, 40)
        # payroll_system.calculate_payroll(employees)

    @staticmethod
    def print_dict(d):
        print(json.dumps(d, indent=2))


if __name__ == '__main__':
    Main.main()
