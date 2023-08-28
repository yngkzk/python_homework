class Calculator:
    exponentiation = 0
    remainder = 0
    percentage = 0
    addition = 0
    subtraction = 0
    multiplication = 0
    division = 0

    def __init__(self, exponentiation, remainder, percentage, addition, subtraction, multiplication, division):
        self.exponentiation = exponentiation
        self.remainder = remainder
        self.percentage = percentage
        self.addition = addition
        self.subtraction = subtraction
        self.multiplication = multiplication
        self.division = division

    def exponent(self, exponentiation):
        message = 'Your number to the power of %s - ' % exponentiation
        return message + str(self ** exponentiation)

    def find_remainder(self, remainder):
        last_number = 10 ** remainder
        number = self % last_number
        message = 'Remainder of %s - %s' % (self, number)
        return message

    def percentage(self, number):
        percent = number / 100
        percentage = self * percent
        return '%s percent of %s - %s' % (number, self, percentage)

    def addition(self, number):
        result = self + number
        message = '%s + %s = %s' % (self, number, result)
        return message

    def subtraction(self, number):
        result = self - number
        message = '%s - %s = %s' % (self, number, result)
        return message

    def multiplication(self, number):
        result = self * number
        message = '%s * %s = %s' % (self, number, result)
        return message

    def division(self, number):
        if number != 0:
            result = self / number
            message = '%s / %s = %s' % (self, number, result)
            return message
        else:
            return 'You can not divide by 0'


print(Calculator.exponent(2, 6))
print(Calculator.find_remainder(3213, 2))
print(Calculator.percentage(100, 20))
print(Calculator.addition(2, 6))
print(Calculator.subtraction(6, 5))
print(Calculator.multiplication(2, 7))
print(Calculator.division(6, 2))

# VN: Нет создания экземпляра класса. Получается, что все методы у вас статические,
# и self внутри методов используется просто как число - один из аргументов