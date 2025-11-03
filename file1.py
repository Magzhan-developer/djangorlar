# calculator.py
# Простой калькулятор с базовыми операциями

class Calculator:
    def __init__(self):
        self.history = []

    def add(self, a, b):
        result = a + b
        self._save(f"{a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        result = a - b
        self._save(f"{a} - {b} = {result}")
        return result

    def multiply(self, a, b):
        result = a * b
        self._save(f"{a} * {b} = {result}")
        return result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        self._save(f"{a} / {b} = {result}")
        return result

    def power(self, a, b):
        result = a ** b
        self._save(f"{a} ** {b} = {result}")
        return result

    def _save(self, record):
        self.history.append(record)

    def show_history(self):
        for line in self.history:
            print(line)

if __name__ == "__main__":
    calc = Calculator()
    calc.add(5, 3)
    calc.subtract(10, 4)
    calc.multiply(2, 8)
    calc.divide(9, 3)
    calc.power(2, 5)
    calc.show_history()
