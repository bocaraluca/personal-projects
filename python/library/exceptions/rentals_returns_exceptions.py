class BookAlreadyReturnedException(Exception):
    def __init__(self, rental_id):
        super().__init__(f"Book with id {rental_id} already returned")

class SmallerReturnDateException(Exception):
    def __init__(self, rented_date):
        super().__init__(f"Return date cannot be smaller than rental date: {rented_date}")
