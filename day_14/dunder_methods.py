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

class Designer(Employee):
    def __init__(self, name, address, salary, tool) :
        super().__init__(name, address , salary) 
        self.tool = tool 

    def print_details(self):
        super().print_details()
        print("Tool:", self.tool)

class Developer(Employee):
    def __init__(self, name, address, salary, programming_lang):
        super().__init__(name, address, salary)
        self.programming_lang = programming_lang

    def print_details(self):
        super().print_details()
        print("Programming Lang", self.programming_lang)


designer1 = Designer(
    name = "Binaya",
    address= "Kathmandu",
    salary= 50000,
    tool= 'figma',
)

developer1 = Developer(
    name = "Charitra",
    address="bhaktapur",
    salary=60000,
    programming_lang= "Python"
)

designer1.print_details()
developer1.print_details()

        