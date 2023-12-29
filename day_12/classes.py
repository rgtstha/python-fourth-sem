# Create a class named Calculator

# create methods: add, subtract, multiply, divide

class Calculator:
    def __init__(self, a , b):
        self.num_1 = a
        self.num_2 = b

    def addition(self):
        # print(f"Add: {self.num_1 + self.num_2}")
        return self.num_1 + self.num_2

    def substraction(self):
        # print(f"Sub: {self.num_1 - self.num_2}")
        return self.num_1 - self.num_2

    def multiplication(self):
        # print(f"Mul: {self.num_1 * self.num_2}")
        return self.num_1 * self.num_2
    
    def division(self):
        # print(f"Div: {self.num_1 / self.num_2}")
        return self.num_1 / self.num_2

calculator = Calculator(a= 10, b = 5)
print(calculator.addition())
print(calculator.substraction())
print(calculator.multiplication())
print(calculator.division())