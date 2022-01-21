
def prompt_number():
    number = -2

    while number <= 0:
        number = int(input('Enter a positive number: '))
        if number < 0:
            print('Invalid entry. The number must be positive.')
    print()
    return number


def compute_sum(number1, number2, number3):
    sum = number1 + number2 + number3
    return sum


def main():
    number1 = prompt_number()
    number2 = prompt_number()
    number3 = prompt_number()
    sum = compute_sum(number1, number2, number3)
    print(f'The sum is: {sum}')


if __name__ == "__main__":
    main()



