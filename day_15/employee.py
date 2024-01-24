# Base Class
class Employee:
    def __init__(self, name , address, salary):
        self.name = name 
        self.address = address
        self.salary = salary

    def print_details(self):
        print("Name:", self.name)
        print("Address:", self.address)
        print("Salary:", self.salary)