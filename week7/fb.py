def fb(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n < 1:
        return
    return fb(n-1) + fb(n-2)


def main():
    n = int(input(' number : '))
    print(fb(n))


if __name__ == '__main__':
    main()
