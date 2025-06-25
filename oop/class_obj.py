class Calculator:
    def __init__(self):
        self.num1 = int(input("Enter the first number: "))
        self.num2 = int(input("Enter the second number: "))

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

calc = Calculator()
print("Addition:", calc.add())
print("Subtraction:", calc.subtract())
