class Calculator:
    def calculate(self, a, b, operator):
        if operator == "add":
            return a + b
        elif operator == "subtract":
            return a - b
        elif operator == "multiply":
            return a * b
        elif operator == "divide":
            if b == 0:
                return "Cannot divide by zero"
            else:
                return a / b
        else:
            return "Invalid operation"


calc = Calculator()
print(calc.calculate(4, 2, "add"))        
print(calc.calculate(5, 2, "subtract"))   
print(calc.calculate(3, 6, "multiply"))   
print(calc.calculate(10, 2, "divide"))   
