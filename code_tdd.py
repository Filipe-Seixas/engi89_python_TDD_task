class Calculator:

    def remainder(self, num1, num2):
        return num1 % num2

    def percentage(self, num1, num2):
        quo = num1 / num2
        return quo * 100

    def is_positive(self, num1):
        return num1 > 0
