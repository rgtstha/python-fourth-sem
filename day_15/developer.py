from employee import Employee

class Developer(Employee):
    def __init__(self, name, address, salary, programming_lang):
        super().__init__(name, address, salary)
        self.programming_lang = programming_lang

    def print_details(self):
        super().print_details()
        print("Programming Lang", self.programming_lang)
