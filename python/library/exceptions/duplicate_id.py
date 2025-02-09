class DuplicateBookIdException(Exception):
    def __init__(self, book_id: int):
        self.message = f"Book with id {book_id} already exists"
        super().__init__(self.message)

class DuplicateClientIdException(Exception):
    def __init__(self, client_id: int):
        self.message = f"Client with id {client_id} already exists"
        super().__init__(self.message)

class DuplicateRentalIdException(Exception):
    def __init__(self, rental_id: int):
        self.message = f"Rental with id {rental_id} already exists"
        super().__init__(self.message)