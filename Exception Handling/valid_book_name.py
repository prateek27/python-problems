class InvalidBookNameException(Exception):
    pass

class BookNameValidator:
    @staticmethod
    def validate(book_name):
        """
        Validates the book name.

        Args:
        - book_name: A string representing the book name.

        Raises:
        - InvalidBookNameException: If the book name does not start with "Scaler Java".
        - print("Book created!:", book_name) otherwise
        """

        # todo
        if not book_name.startswith("Scaler Java"):
            raise InvalidBookNameException("Book name doesn't start with Scaler Java")
        else:
            print("Book created!:", book_name)


