class GPA():
    def __init__(self):
        self._gpa: float = 0.0

    def get_gpa(self):
        return self._gpa

    def set_gpa(self, gpa):
        if (gpa > 4):
            self._gpa = 4
        elif (gpa < 0):
            self._gpa = 0
        else:
            self._gpa = gpa

    def get_letter(self):
        if (self.get_gpa() < 1):
            return 'F'
        elif (self.get_gpa() < 2):
            return 'D'
        elif (self.get_gpa() < 3):
            return 'C'
        elif (self.get_gpa() < 4):
            return 'B'
        elif (self.get_gpa() == 4):
            return 'A'

    def set_letter(self, letter):
        if (letter == 'F'):
            self.set_gpa(0)
        elif (letter == 'D'):
            self.set_gpa(1)
        elif (letter == 'C'):
            self.set_gpa(2)
        elif (letter == 'B'):
            self.set_gpa(3)
        elif (letter == 'A'):
            self.set_gpa(4)


def main():
    student = GPA()

    print("Initial values:")
    print("GPA: {:.2f}".format(student.get_gpa()))
    print("Letter: {}".format(student.get_letter()))

    value = float(input("Enter a new GPA: "))

    student.set_gpa(value)

    print("After setting value:")
    print("GPA: {:.2f}".format(student.get_gpa()))
    print("Letter: {}".format(student.get_letter()))

    letter = input("Enter a new letter: ")

    student.set_letter(letter)

    print("After setting letter:")
    print("GPA: {:.2f}".format(student.get_gpa()))
    print("Letter: {}".format(student.get_letter()))


if __name__ == "__main__":
    main()
