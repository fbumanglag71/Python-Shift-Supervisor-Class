## Author: Francisco Bumanglag
## Project: Shift Supervisor Class
## Assignment: Module 6 Project 1
## Course: Python Santa Ana College
## Class: CMPR114 Jason Sim
## Date: July 17, 2023



# Assuming this is the Employee class from Programming Exercise 1
class Employee:
    def __init__(self, name, employee_number):
        self.name = name
        self.employee_number = employee_number


# ShiftSupervisor class (subclass of Employee)
class ShiftSupervisor(Employee):
    def __init__(self, name, employee_number, annual_salary, annual_bonus):
        # Call the constructor of the parent class (Employee) using super()
        super().__init__(name, employee_number)
        # Set data attributes specific to the ShiftSupervisor class
        self.annual_salary = annual_salary
        self.annual_bonus = annual_bonus

    def __str__(self):
        return f"Name: {self.name}, Employee Number: {self.employee_number}, Annual Salary: {self.annual_salary}, Annual Bonus: {self.annual_bonus}"

# Create a ShiftSupervisor instance
shift_supervisor = ShiftSupervisor("John Doe", "12345", 60000, 5000)

# Access attributes
print(shift_supervisor.name)          # Output: John Doe
print(shift_supervisor.employee_number)  # Output: 12345
print(shift_supervisor.annual_salary)  # Output: 60000
print(shift_supervisor.annual_bonus)   # Output: 5000

# Using the __str__ method to display all attributes
print(shift_supervisor)
# Output: Name: John Doe, Employee Number: 12345, Annual Salary: 60000, Annual Bonus: 5000
