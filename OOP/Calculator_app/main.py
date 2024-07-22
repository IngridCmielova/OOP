class Calculator:
    def __init__(self):
        self.last_result = None

    def addition(self, a, b):
        self.last_result = a + b
        return self.last_result

    def subtraction(self, a, b):
        self.last_result = a - b
        return self.last_result

    def multiplication(self, a, b):
        self.last_result = a * b
        return self.last_result

    def division(self, a, b):
        if b != 0:
            self.last_result = a / b
            return self.last_result
        else:
            self.last_result = None
            return "Division by zero is not allowed"

    def save_result(self, file):
        if self.last_result is not None:
            try:
                with open(file, 'w') as f:
                    f.write(str(self.last_result))
                return "Result saved to file"
            except Exception as e:
                return f"Error saving to file: {e}"
        else:
            return "No result to save"

calculator = Calculator()
print(10 + 5-7)  # 15
print(calculator.subtraction(10, 5))  # 5
print(calculator.multiplication(10, 5))  # 50
print(calculator.division(10, 5))  # 2.0
