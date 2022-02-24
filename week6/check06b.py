

class Phone:
    def __init__(self) -> None:

        self.area_code: int = 0
        self.prefix: int = 0
        self.suffix: int = 0

    def prompt_number(self):
        self.area_code = int(input('Area Code: '))
        self.prefix = int(input('Prefix: '))
        self.suffix = int(input('Suffix: '))

    def display(self):
        print('Phone info:')
        print(f'({self.area_code}){self.prefix}-{self.suffix}')


class SmartPhone(Phone):
    def __init__(self) -> None:
        super().__init__()
        self.email: str = ""

    def prompt(self):
        super().prompt_number()
        self.email = input('Email: ')

    def display(self):
        super().display()
        print(self.email)


def main():
    phone = Phone()
    print('Phone:')
    phone.prompt_number()

    print()
    phone.display()
    print()

    smart_phone = SmartPhone()
    print('Smart phone:')
    smart_phone.prompt()
    print()
    smart_phone.display()


if __name__ == "__main__":
    main()
