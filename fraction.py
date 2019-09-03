#! usr/lib/python3
# coding:utf-8
import math


def simplify(numerator, denominator):
    smallest = min(numerator, denominator)
    for i in range(smallest, 1, -1):
        if numerator % i == 0 and denominator % i == 0:
            return int(numerator / i), int(denominator / i)


class Fraction:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, fraction):
        self.numerator = fraction.denominator * self.numerator + fraction.numerator * self.denominator
        self.denominator = self.denominator * fraction.denominator
        return simplify(self.numerator, self.denominator)

    def __sub__(self, fraction):
        self.numerator = self.numerator * fraction.denominator - self.denominator * fraction.numerator
        self.denominator = self.denominator * fraction.denominator
        return simplify(self.numerator, self.denominator)

    def __mul__(self, fraction):
        self.numerator = self.numerator * fraction.numerator
        self.denominator = self.denominator * fraction.denominator
        return simplify(self.numerator, self.denominator)

    def __truediv__(self, fraction):
        self.numerator = self.numerator * fraction.denominator
        self.denominator = self.denominator * fraction.numerator
        return simplify(self.numerator, self.denominator)
