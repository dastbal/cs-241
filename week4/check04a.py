"""
File: check04a.py

Purpose: create two classes Person and Book
"""


# TODO: display  the data of a book


class person():
    def __init__(self) -> None:
        self.name = 'anonymous'
        self.birht_year = 'unknown'

    def display(self):
        print('Author:')
        print(f'{self.name} (b. {self.birht_year})')


class Book():
    def __init__(self) -> None:
        self.tile = 'untitled'
        self.author = person()
        self.publisher = 'unpublished'

    def display(self):
        print(self.tile)
        print('Publisher:')
        print(self.publisher)
        self.author.display()


def main():
    new_book = Book()
    new_book.display()
    print()
    print('Please enter the following:')
    name = input('Name: ')
    birth_year = input('Year: ')
    title = input('Title: ')
    publisher = input('Publisher: ')
    new_book.tile = title
    new_book.publisher = publisher
    new_book.author.birht_year = birth_year
    new_book.author.name = name
    print()
    new_book.display()


if __name__ == "__main__":
    main()
