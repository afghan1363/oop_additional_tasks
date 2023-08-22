"""
Напишите класс Fraction, представляющий собой дробь, имеющий следующие методы:

- __init__(self, numerator, denominator): конструктор, принимающий числитель и знаменатель дроби;
- __repr__(self): магический метод, возвращающий строковое представление дроби,
которое можно использовать для создания нового объекта класса Fraction;
- __str__(self): магический метод, возвращающий строковое представление дроби;
- __add__(self, other): магический метод, который позволяет складывать дроби и возвращать новую дробь.
"""


class Fraction:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __repr__(self):
        return f"{__class__.__name__}({self.numerator}, {self.denominator})"

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        temp_numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        temp_denominator = self.denominator * other.denominator
        while temp_numerator % 10 == 0 and temp_denominator % 10 == 0:
            temp_numerator /= 10
            temp_denominator /= 10
        for x in range(2, 3):
            while temp_numerator % x != 0 and temp_denominator % x != 0:
                temp_numerator /= x
                temp_denominator /= x
            # if temp_numerator % x == 0 and temp_denominator % x == 0:
            #     temp_numerator /= x
            #     temp_denominator /= x
        return f"{temp_numerator}/{temp_denominator}"


fraction1 = Fraction(1, 2)
print(repr(fraction1))  # Fraction(1, 2)
print(str(fraction1))  # 1/2

fraction2 = Fraction(3, 4)
fraction3 = fraction1 + fraction2
print(fraction3)  # 5/4
