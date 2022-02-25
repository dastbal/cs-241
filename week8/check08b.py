class GPA():
    def __init__(self):
        self._gpa: float = 0.0

    def _get_gpa(self):
        return self._gpa

    def _set_gpa(self, gpa):
        if (gpa > 4):
            self._gpa = 4
        elif (gpa < 0):
            self._gpa = 0
        else:
            self._gpa = gpa

    def _get_letter(self):
        if (self._get_gpa() < 1):
            return 'F'
        elif (self._get_gpa() < 2):
            return 'D'
        elif (self._get_gpa() < 3):
            return 'C'
        elif (self._get_gpa() < 4):
            return 'B'
        elif (self._get_gpa() == 4):
            return 'A'

    def _set_letter(self, letter):
        if (letter == 'F'):
            self._set_gpa(0)
        elif (letter == 'D'):
            self._set_gpa(1)
        elif (letter == 'C'):
            self._set_gpa(2)
        elif (letter == 'B'):
            self._set_gpa(3)
        elif (letter == 'A'):
            self._set_gpa(4)
    gpa = property(_get_gpa, _set_gpa)

    @property
    def letter(self):
        return self._get_letter()

    @letter.setter
    def letter(self, letter):
        self._set_letter(letter)


def main():
    student = GPA()

    print("Initial values:")
    print("GPA: {:.2f}".format(student.gpa))
    print("Letter: {}".format(student.letter))

    value = float(input("Enter a new GPA: "))

    student.gpa = value

    print("After setting value:")
    print("GPA: {:.2f}".format(student.gpa))
    print("Letter: {}".format(student.letter))

    letter = input("Enter a new letter: ")

    student.letter = letter

    print("After setting letter:")
    print("GPA: {:.2f}".format(student.gpa))
    print("Letter: {}".format(student.letter))


if __name__ == "__main__":
    main()
