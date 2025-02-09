from src.exceptions.duplicate_id import DuplicateRentalIdException
from src.exceptions.not_found import RentalNotFoundException, ClientNotFoundException, BookNotFoundException
from src.repository.binary_file_repository import RentalsBinaryFileRepository, BooksBinaryFileRepository, \
    ClientsBinaryFileRepository
from src.repository.memory_repository import RentalsMemoryRepository, BooksMemoryRepository, ClientsMemoryRepository
from src.repository.text_file_repository import RentalsTextFileRepository, BooksTextFileRepository, \
    ClientsTextFileRepository
from src.services.undo_service import UndoService, FunctionCall, Operation


class RentalsService:
    def __init__(self, undo_service, repo_type, books_path = None, clients_path = None, file_path=None):
        self._undo_service = undo_service
        if repo_type == 'in-memory':
            self._books_repo = BooksMemoryRepository()
            self._clients_repo = ClientsMemoryRepository()
            self._rentals_repo = RentalsMemoryRepository(self._books_repo, self._clients_repo)
        elif repo_type == 'text-file':
            if file_path is None:
                raise FileNotFoundError('No file path provided!')
            self._books_repo = BooksTextFileRepository(books_path)
            self._clients_repo = ClientsTextFileRepository(clients_path)
            self._rentals_repo = RentalsTextFileRepository(self._books_repo, self._clients_repo, file_path)
        elif repo_type == 'binary-file':
            if file_path is None:
                raise FileNotFoundError('No file path provided!')
            self._books_repo = BooksBinaryFileRepository(books_path)
            self._clients_repo = ClientsBinaryFileRepository(clients_path)
            self._rentals_repo = RentalsBinaryFileRepository(self._books_repo, self._clients_repo, file_path)
        else:
            raise ValueError('Invalid repository type! Repository type should be in-memory, text-file or binary-file.')

    def rent_book(self, rental_id, book_id, client_id, rented_date):
        self._rentals_repo.rent_book(rental_id, book_id, client_id, rented_date)

        undo = FunctionCall(self._rentals_repo.remove_rental, rental_id)
        redo = FunctionCall(self._rentals_repo.rent_book, rental_id, book_id, client_id, rented_date)

        operation = Operation(undo, redo)
        self._undo_service.record_operation(operation)

    def return_book(self, rental_id, returned_date):
        self._rentals_repo.return_book(rental_id, returned_date)

        undo = FunctionCall(self._rentals_repo.set_return_to_none, rental_id)
        redo = FunctionCall(self._rentals_repo.return_book, rental_id, returned_date)

        operation = Operation(undo, redo)
        self._undo_service.record_operation(operation)

    def list_rentals(self):
        rentals = self._rentals_repo.list_rentals()
        sorted_rentals = sorted(rentals, key=lambda rental: rental.rental_id)
        return sorted_rentals

    def find_rental_by_id(self, rental_id):
        try:
            return self._rentals_repo.find_rental(rental_id)
        except RentalNotFoundException:
            return None

    def remove_rental(self, rental_id):
        try:
            rental = self._rentals_repo.find_rental(rental_id)
            self._rentals_repo.remove_rental(rental_id)
        except RentalNotFoundException:
            raise RentalNotFoundException

    def is_book_available(self, book_id, rented_date, returned_date):
        return self._rentals_repo.is_book_available(book_id, rented_date, returned_date)

    def get_most_rented_books(self):
        book_rental_counts = self._rentals_repo.get_most_rented_books()
        most_rented_books = []
        for book_id, count in book_rental_counts:
            try:
                book = self._books_repo.find_book(book_id)
                most_rented_books.append((book_id, book.title, count))
            except BookNotFoundException:
                continue
        return most_rented_books

    def get_most_active_clients(self):
        client_rental_counts = self._rentals_repo.get_most_active_clients()
        most_active_clients = []
        for client_id, count in client_rental_counts:
            try:
                client = self._clients_repo.find_client(client_id)
                most_active_clients.append((client_id, client.name, count))
            except ClientNotFoundException:
                continue
        return most_active_clients

    def get_most_rented_authors(self):
        author_rental_counts = self._rentals_repo.get_most_rented_authors()
        most_rented_authors = []
        for name, count in author_rental_counts:
            most_rented_authors.append((name, count))
        return most_rented_authors