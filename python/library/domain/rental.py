class Rental:
    def __init__(self, rental_id, book_id, client_id, rented_date, returned_date = None):
        self.__rental_id = rental_id
        self.__book_id = book_id
        self.__client_id = client_id
        self.__rented_date = rented_date
        self.__returned_date = returned_date

    @property
    def rental_id(self):
        return self.__rental_id

    @property
    def book_id(self):
        return self.__book_id

    @book_id.setter
    def book_id(self, book_id):
        self.__book_id = book_id

    @property
    def client_id(self):
        return self.__client_id

    @client_id.setter
    def client_id(self, client_id):
        self.__client_id = client_id

    @property
    def rented_date(self):
        return self.__rented_date

    @rented_date.setter
    def rented_date(self, rented_date):
        self.__rented_date = rented_date

    @property
    def returned_date(self):
        return self.__returned_date

    @returned_date.setter
    def returned_date(self, returned_date):
        self.__returned_date = returned_date

    def is_active(self):
        return self.__returned_date is None

    def __str__(self):
        rented_date = self.__rented_date.strftime("%Y-%m-%d")
        returned_date = self.__returned_date.strftime("%Y-%m-%d") if self.__returned_date is not None else "N/A"
        return (f"Rental id: {self.__rental_id}; Book id: {self.__book_id};"
                f" Client id: {self.__client_id}; Rented date: {rented_date}; Returned date: {returned_date}")