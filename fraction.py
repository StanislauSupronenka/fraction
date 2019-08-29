#! usr/lib/python3
# coding:utf-8


class Fraction:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def simplify(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        if numerator != denominator:
            divider = 2
            while divider <= self.denominator:
                if self.numerator % divider == 0:
                    if self.denominator % divider == 0:
                        self.numerator /= divider
                        self.denominator /= divider
                        divider = 2
                divider += 1
            return str(int(self.numerator)) + '/' + str(int(self.denominator))
        else:
            return numerator

    def __add__(self, fraction):
        self.numerator = fraction.denominator*self.numerator + fraction.numerator * self.denominator
        self.denominator = self.denominator * fraction.denominator
        return self.simplify(self.numerator, self.denominator)

    def __sub__(self, fraction):
        self.numerator = self.numerator * fraction.denominator - self.denominator * fraction.numerator
        self.denominator = self.denominator * fraction.denominator
        return self.simplify(self.numerator, self.denominator)

    def __mul__(self, fraction):
        self.numerator = self.numerator * fraction.numerator
        self.denominator = self.denominator * fraction.denominator
        return self.simplify(self.numerator, self.denominator)

    def __truediv__(self, fraction):
        self.numerator = self.numerator * fraction.denominator
        self.denominator = self.denominator * fraction.numerator
        return self.simplify(self.numerator, self.denominator)
