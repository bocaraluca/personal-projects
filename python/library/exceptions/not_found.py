class BookNotFoundException(Exception):
    def __init__(self, book_id: int):
        super().__init__(f"Book with id {book_id} not found")

class ClientNotFoundException(Exception):
    def __init__(self, client_id: int):
        super().__init__(f"Client with id {client_id} not found")

class RentalNotFoundException(Exception):
    def __init__(self, rental_id: int):
        super().__init__(f"Rental with id {rental_id} not found")