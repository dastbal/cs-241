from re import X


class Fraction:
    def __init__(self, numerator=0, denominator=1) -> None:
        self.numerator = numerator
        self.denominator = denominator

    def display(self):
        print(f'{self.numerator}/{self.denominator}')

    def display_decimal(self):
        print(float(self.numerator/self.denominator))

    def prompt(self):
        self.numerator = int(input('Enter the numerator: '))
        self.denominator = int(input('Enter the denominator: '))


def main():
    x = Fraction()
    x.display()
    x.prompt()
    x.display()
    x.display_decimal()


main()
