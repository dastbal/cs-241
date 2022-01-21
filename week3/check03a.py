

class Student:
    def __init__(self, first_name, last_name, id):

        self.first_name = first_name
        self.last_name = last_name
        self.id = id


def prompt_student():
    first_name = input('Please enter your first name: ')
    last_name = input('Please enter your last name: ')
    id = int(input('Please enter your id number: '))
    student = Student(first_name, last_name, id)
    return student


def display_student(student):
    print(f'{student.id} - {student.first_name} {student.last_name}')


def main():
    student = prompt_student()
    print()
    print('Your information:')
    display_student(student)


main()
