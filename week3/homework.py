def main():
    odd = []
    even = []
    number = 5

    while(number != 0):
        number = int(input('enter a number (0 to quit) '))
        print(number % 2)
        print(number % 2 == 0)
        if (number % 2 == 0):
            even.append(number)
        else:
            odd.append(number)
    print('Even numbers')
    for i in even:
        print(i)
    print('Odd numbers')
    for j in odd:
        print(j)


if __name__ == "__main__":
    main()
