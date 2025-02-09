import os
import pickle
from collections import defaultdict
from datetime import timedelta, datetime
from random import choice, randint

from faker import Faker
from src.domain.book import Book
from src.domain.client import Client
from src.domain.rental import Rental
from src.exceptions.duplicate_id import DuplicateBookIdException, DuplicateClientIdException, DuplicateRentalIdException
from src.exceptions.not_found import BookNotFoundException, ClientNotFoundException, RentalNotFoundException
from src.exceptions.rentals_returns_exceptions import BookAlreadyReturnedException, SmallerReturnDateException
from src.repository.repository_iterator import RepositoryIterator

class BooksBinaryFileRepository:
    def __init__(self, file_name: str) -> None:
        """
        Constructor for BooksBinaryFileRepository class
        :param file_name: The name of the file to store books (str)
        """
        self._file_name = file_name
        self._books = []
        if self._file_exists() and not self._is_file_empty():
            self._read_books_from_file()
        else:
            self._generate_books()
            self._save_books_to_file()

    def _read_books_from_file(self) -> None:
        """
        Reads books from the file and loads them into the repository
        :return: None
        """
        with open(self._file_name, 'rb') as file:
            self._books = pickle.load(file)

    def _save_books_to_file(self) -> None:
        """
        Saves the books in the repository to the file
        :return: None
        """
        with open(self._file_name, 'wb') as file:
            pickle.dump(self._books, file)

    def _generate_books(self) -> None:
        """
        Generates 20 random books using the Faker library
        :return: None
        """
        fake = Faker()
        for i in range(20):
            title = fake.text(max_nb_chars=20).strip('.')
            author = fake.name()
            self._books.append(Book(i + 1, title, author))

    def find_book(self, book_id: int) -> Book:
        """
        Finds a book by its id in the repository
        :param book_id: The id of the book to find (int)
        :return: The book with the given id if it exists
        """
        for book in self._books:
            if book.book_id == book_id:
                return book
        raise BookNotFoundException(book_id=book_id)

    def add_book(self, book_id: int, title: str, author: str) -> None:
        """
        Adds a book to the repository
        :param book_id: The id of the book to add (int)
        :param title: The title of the book to add (str)
        :param author: The author of the book to add (str)
        :return: None
        """
        try:
            self.find_book(book_id)
            raise DuplicateBookIdException(book_id=book_id)
        except BookNotFoundException:
            self._books.append(Book(book_id, title, author))
            self._save_books_to_file()

    def remove_book(self, book_id: int) -> None:
        """
        Removes a book from the repository
        :param book_id: The id of the book to remove (int)
        :return: None
        """
        try:
            book = self.find_book(book_id)
            self._books.remove(book)
            self._save_books_to_file()
        except ValueError:
            raise BookNotFoundException(book_id=book_id)

    def update_book(self, book_id: int, new_title: str, new_author: str) -> None:
        """
        Updates the title and author of a book in the repository
        :param book_id: The id of the book to update (int)
        :param new_title: The new title of the book (str)
        :param new_author: The new author of the book (str)
        :return: None
        """
        try:
            book = self.find_book(book_id)
            book.title = new_title
            book.author = new_author
            self._save_books_to_file()
        except ValueError:
            raise BookNotFoundException(book_id=book_id)

    def list_books(self) -> list:
        """
        Returns a list of all books in the repository
        :return: The list of books
        """
        return self._books

    def __iter__(self) -> RepositoryIterator:
        """
        Iterator method
        :return: RepositoryIterator object
        """
        return RepositoryIterator(self._books)

    def _file_exists(self) -> bool:
        """
        Checks if the file exists
        :return: True if the file exists, False otherwise
        """
        return os.path.exists(self._file_name)

    def _is_file_empty(self) -> bool:
        """
        Checks if the file is empty
        :return: True if the file is empty, False otherwise
        """
        return self._file_exists() and os.path.getsize(self._file_name) == 0


class ClientsBinaryFileRepository:
    def __init__(self, file_name: str) -> None:
        """
        Constructor for ClientsBinaryFileRepository class
        :param file_name: The name of the file to store clients (str)
        """
        self._file_name = file_name
        self._clients = []
        if self._file_exists() and not self._is_file_empty():
            self._read_clients_from_file()
        else:
            self._generate_clients()
            self._save_clients_to_file()

    def _read_clients_from_file(self) -> None:
        """
        Reads clients from the file and loads them into the repository
        :return: None
        """
        with open(self._file_name, 'rb') as file:
            self._clients = pickle.load(file)

    def _save_clients_to_file(self) -> None:
        """
        Saves the clients in the repository to the file
        :return: None
        """
        with open(self._file_name, 'wb') as file:
            pickle.dump(self._clients, file)

    def _generate_clients(self) -> None:
        """
        Generates 20 random clients using the Faker library
        :return: None
        """
        fake = Faker()
        for i in range(20):
            name = fake.name()
            self._clients.append(Client(i + 1, name))

    def find_client(self, client_id: int) -> Client:
        """
        Finds a client by its id in the repository
        :param client_id: The id of the client to find (int)
        :return: The client with the given id if it exists
        """
        for client in self._clients:
            if client.client_id == client_id:
                return client
        raise ClientNotFoundException(client_id=client_id)

    def add_client(self, client_id: int, name: str) -> None:
        """
        Adds a client to the repository
        :param client_id: The id of the client to add (int)
        :param name: The name of the client to add (str)
        :return: None
        """
        try:
            self.find_client(client_id)
            raise DuplicateClientIdException(client_id=client_id)
        except ClientNotFoundException:
            self._clients.append(Client(client_id, name))
            self._save_clients_to_file()

    def remove_client(self, client_id: int) -> None:
        """
        Removes a client from the repository
        :param client_id: The id of the client to remove (int)
        :return: None
        """
        try:
            client = self.find_client(client_id)
            self._clients.remove(client)
            self._save_clients_to_file()
        except ValueError:
            raise ClientNotFoundException(client_id=client_id)

    def update_client(self, client_id: int, new_name: str) -> None:
        """
        Updates the name of a client in the repository
        :param client_id: The id of the client to update (int)
        :param new_name: The new name of the client (str)
        :return: None
        """
        try:
            client = self.find_client(client_id)
            client.name = new_name
            self._save_clients_to_file()
        except ValueError:
            raise ClientNotFoundException(client_id=client_id)

    def list_clients(self) -> list:
        """
        Returns a list of all clients in the repository
        :return: The list of clients
        """
        return self._clients

    def __iter__(self) -> RepositoryIterator:
        """
        Iterator method
        :return: RepositoryIterator object
        """
        return RepositoryIterator(self._clients)

    def _file_exists(self) -> bool:
        """
        Checks if the file exists
        :return: True if the file exists, False otherwise
        """
        return os.path.exists(self._file_name)

    def _is_file_empty(self) -> bool:
        """
        Checks if the file is empty
        :return: True if the file is empty, False otherwise
        """
        return self._file_exists() and os.path.getsize(self._file_name) == 0

class RentalsBinaryFileRepository:
    def __init__(self, books_repo: BooksBinaryFileRepository, clients_repo: ClientsBinaryFileRepository, file_name: str) -> None:
        """
        Constructor for RentalsBinaryFileRepository class
        :param books_repo: The repository of books (BooksTextFileRepository)
        :param clients_repo: The repository of clients (ClientsTextFileRepository)
        :param file_name: The name of the file to store rentals (str)
        """
        self._file_name = file_name
        self._rentals = []
        self._books_repo = books_repo
        self._clients_repo = clients_repo
        if self._file_exists() and not self._is_file_empty():
            self._read_rentals_from_file()
        else:
            self._generate_rentals()
            self._save_rentals_to_file()

    def _generate_rentals(self) -> None:
        fake = Faker()
        for i in range(20):
            book = choice(self._books_repo.list_books())
            client = choice(self._clients_repo.list_clients())
            rented_date = fake.date_this_year()
            if randint(0, 1):
                returned_date = rented_date + timedelta(days=randint(1, 30))
            else:
                returned_date = None

            while not self.is_book_available(book.book_id, rented_date, returned_date):
                book = choice(self._books_repo.list_books())
                rented_date = fake.date_this_year()
                if randint(0, 1):
                    returned_date = rented_date + timedelta(days=randint(1, 30))
                else:
                    returned_date = None

            self._rentals.append(Rental(i + 1, book.book_id, client.client_id, rented_date, returned_date))

    def find_rentals_by_client_id(self, client_id: int) -> list:
        """
        Finds all rentals for a client by their id
        :param client_id: The id of the client (int)
        :return: The list of rentals
        """
        return [rental for rental in self._rentals if rental.client_id == client_id]

    def is_book_available(self, book_id, rented_date, returned_date):
        for rental in self._rentals:
            if rental.book_id == book_id:
                if rental.is_active():
                    if returned_date is None or rented_date <= rental.rented_date:
                        return False
                else:
                    if rental.returned_date is not None:
                        if rented_date < rental.returned_date and (
                                returned_date is None or returned_date > rental.rented_date):
                            return False
                    else:
                        if rented_date >= rental.rented_date:
                            continue
                        if returned_date is not None and returned_date <= rental.rented_date:
                            continue
                        return False
        return True

    def set_return_to_none(self, rental_id):
        for rental in self._rentals:
            if rental.rental_id == rental_id:
                rental.returned_date = None
                return
        raise RentalNotFoundException(rental_id=rental_id)

    def find_rentals_by_book_id(self, book_id: int) -> list:
        """
        Finds all rentals for a book by its id
        :param book_id: The id of the book (int)
        :return: The list of rentals
        """
        return [rental for rental in self._rentals if rental.book_id == book_id]

    def _read_rentals_from_file(self) -> None:
        """
        Reads rentals from the file and loads them into the repository
        :return: None
        """
        with open(self._file_name, 'rb') as file:
            self._rentals = pickle.load(file)

    def _save_rentals_to_file(self) -> None:
        """
        Saves the rentals in the repository to the file
        :return: None
        """
        with open(self._file_name, 'wb') as file:
            pickle.dump(self._rentals, file)

    def _file_exists(self) -> bool:
        """
        Checks if the file exists
        :return: True if the file exists, False otherwise
        """
        return os.path.exists(self._file_name)

    def _is_file_empty(self) -> bool:
        """
        Checks if the file is empty
        :return: True if the file is empty, False otherwise
        """
        return self._file_exists() and os.path.getsize(self._file_name) == 0

    def find_rental(self, rental_id: int) -> Rental:
        """
        Finds a rental by its id in the repository
        :param rental_id: The id of the rental to find (int)
        :return: The rental with the given id if it exists
        """
        for rental in self._rentals:
            if rental.rental_id == rental_id:
                return rental
        raise RentalNotFoundException(rental_id=rental_id)

    def rent_book(self, rental_id, book_id, client_id, rented_date):
        """
        Rent a book to a client.
        :param rental_id: ID for the rental (int)
        :param book_id: The book ID (int)
        :param client_id: The client ID (int)
        :param rented_date: The date the book is rented (datetime.date)
        :return: None
        """
        try:
            existing_rental = self.find_rental(rental_id)
            raise DuplicateRentalIdException(rental_id=rental_id)
        except RentalNotFoundException:
            new_rental = Rental(rental_id, book_id, client_id, rented_date, None)
            self._rentals.append(new_rental)
            self._save_rentals_to_file()

    def return_book(self, rental_id, returned_date):
        """
        Returns a rented book.
        :param rental_id: The id of the rental (int)
        :param returned_date: The date when the book is returned (datetime.date)
        :return: None
        """
        try:
            rental = self.find_rental(rental_id)

            if rental is None:
                raise RentalNotFoundException(rental_id=rental_id)

            if rental.returned_date is not None:
                raise BookAlreadyReturnedException(rental_id=rental_id)

            if rental.rented_date is None:
                raise ValueError(f"Rental with ID {rental_id} has no rented date set.")

            returned_date = returned_date.date() if isinstance(returned_date, datetime) else returned_date
            rented_date = rental.rented_date.date() if isinstance(rental.rented_date, datetime) else rental.rented_date

            if returned_date < rented_date:
                raise SmallerReturnDateException(rented_date)

            rental.returned_date = returned_date
            self._save_rentals_to_file()
        except RentalNotFoundException as e:
            raise e
        except ValueError as e:
            raise e

    def remove_rental(self, rental_id: int) -> None:
        """
        Removes a rental from the repository
        :param rental_id: The id of the rental to remove (int)
        :return: None
        """
        try:
            rental = self.find_rental(rental_id)
            self._rentals.remove(rental)
            self._save_rentals_to_file()
        except ValueError:
            raise RentalNotFoundException(rental_id=rental_id)

    def list_rentals(self) -> list:
        """
        Returns a list of all rentals in the repository
        :return: The list of rentals
        """
        return self._rentals

    def get_most_rented_books(self) -> list:
        """
        Returns a list of tuples containing the book id and the number of times they were rented
        :return: The list of tuples
        """
        book_rental_counts = defaultdict(int)

        for rental in self._rentals:
            book_rental_counts[rental.book_id] += 1

        all_books = self._books_repo.list_books()
        for book in all_books:
            if book.book_id not in book_rental_counts:
                book_rental_counts[book.book_id] = 0

        return sorted(book_rental_counts.items(), key=lambda x: x[1], reverse=True)

    def get_most_active_clients(self) -> list:
        """
        Returns a list of tuples containing the client id and their book rental days
        :return: The list of tuples
        """
        clients_rental_days = defaultdict(int)

        for rental in self._rentals:
            if rental.returned_date is not None:
                rental_days = (rental.returned_date - rental.rented_date).days
            else:
                rental_days = (datetime.now().date() - rental.rented_date).days
            clients_rental_days[rental.client_id] += rental_days

        all_clients = self._clients_repo.list_clients()
        for client in all_clients:
            if client.client_id not in clients_rental_days:
                clients_rental_days[client.client_id] = 0

        return sorted(clients_rental_days.items(), key=lambda x: x[1], reverse=True)

    def get_most_rented_authors(self) -> list:
        """
        Returns a list of tuples containing the author id and the number of times their books were rented.
        :return: The list of tuples
        """
        author_rental_counts = defaultdict(int)

        for rental in self._rentals:
            try:
                book = self._books_repo.find_book(rental.book_id)
                if book:
                    author_rental_counts[book.author] += 1
            except BookNotFoundException:
                continue

        all_books = self._books_repo.list_books()
        for book in all_books:
            if book.author not in author_rental_counts:
                author_rental_counts[book.author] = 0

        return sorted(author_rental_counts.items(), key=lambda x: x[1], reverse=True)

    def __iter__(self) -> RepositoryIterator:
        """
        Iterator method
        :return: RepositoryIterator object
        """
        return RepositoryIterator(self._rentals)

    def __len__(self) -> int:
        """
        Returns the number of rentals in the repository
        :return: The number of rentals
        """
        return len(self._rentals)


