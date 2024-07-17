from w6_employee import Employee
from w6_parttime import PartTime
from w6_company import Company

class CompanyProgram:
    def __init__(self):
        self.__company = Company('FPT')

    def run(self):
        # TODO: print menu

    def __add_employee(self):
        # TODO:
        # Ask user to choose to enter full-time or part-time employee
        # Ask user to enter employee's name and rate
        # If part-time, ask user to enter days
        # Create an employee object (Employee or PartTime) and add it to the company
        self.__company.add(e)
        print('Employee added')
    
    def __remove_employee(self):
        # TODO:
        # Ask user to enter employee ID
        # Remove the employee from the company by calling remove method

    def __raise_rate(self):
        # TODO:
        # Ask user to enter employee ID and new rate
        # Raise the rate of the employee by calling raise_rate method

    def __show_all(self):
        self.__company.show_all()