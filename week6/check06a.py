class Book:
    def __init__(self) -> None:
        self.title: str = ""
        self.author: str = ""
        self.publication_year: int = 1900

    def prompt_book_info(self):
        self.title = input('Title: ')
        self.author = input('Author: ')
        self.publication_year = int(input('Publication Year: '))

    def display_book_info(self):

        print(f'{self.title} ({self.publication_year}) by {self.author}')


class TextBook(Book):
    def __init__(self) -> None:
        super().__init__()
        self.subject: str = ""

    def prompt_subject(self):
        self.subject = input('Subject: ')

    def display_subject(self):
        print(f'Subject: {self.subject}')


class PictureBook(Book):
    def __init__(self) -> None:
        super().__init__()
        self.illustrator: str = ""

    def prompt_illustrator(self):
        self.illustrator = input('Illustrator: ')

    def display_illustrator(self):

        print(f'Illustrated by {self.illustrator}')


def main():
    book = Book()
    book.prompt_book_info()
    print()

    book.display_book_info()
    print()

    text_book = TextBook()

    text_book.prompt_book_info()

    text_book.prompt_subject()

    print()
    text_book.display_book_info()

    text_book.display_subject()

    print()
    picture_book = PictureBook()
    picture_book.prompt_book_info()

    picture_book.prompt_illustrator()
    print()

    picture_book.display_book_info()

    picture_book.display_illustrator()


if __name__ == "__main__":
    main()
