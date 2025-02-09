from src.exceptions.not_found import BookNotFoundException
from src.repository.binary_file_repository import BooksBinaryFileRepository
from src.repository.memory_repository import BooksMemoryRepository
from src.repository.text_file_repository import BooksTextFileRepository
from src.services.undo_service import FunctionCall, Operation, CascadedOperation


class BooksService:
    def __init__(self, undo_service, rentals_service, repo_type, file_path=None):
        self._undo_service = undo_service
        self._rentals_service = rentals_service
        if repo_type == 'in-memory':
            self._books_repo = BooksMemoryRepository()
        elif repo_type == 'text-file':
            if file_path is None:
                raise FileNotFoundError('No file path provided!')
            self._books_repo = BooksTextFileRepository(file_path)
        elif repo_type == 'binary-file':
            if file_path is None:
                raise FileNotFoundError('No file path provided!')
            self._books_repo = BooksBinaryFileRepository(file_path)
        else:
            raise ValueError('Invalid repository type! Repository type should be in-memory, text-file or binary-file.')

    def add_book(self, book_id, title, author):
        self._books_repo.add_book(book_id, title, author)
        undo = FunctionCall(self._books_repo.remove_book, book_id)
        redo = FunctionCall(self._books_repo.add_book, book_id, title, author)
        operation = Operation(undo, redo)
        self._undo_service.record_operation(operation)

    def remove_book(self, book_id):
        book = self._books_repo.find_book(book_id)
        if book is None:
            raise BookNotFoundException

        rentals_to_remove = [rental for rental in self._rentals_service.list_rentals() if rental.book_id == book_id]

        undo_remove_book = FunctionCall(self._books_repo.add_book, book_id, book.title, book.author)
        redo_remove_book = FunctionCall(self._books_repo.remove_book, book_id)

        cascaded_op = CascadedOperation()
        cascaded_op.add_undo_function(undo_remove_book)
        cascaded_op.add_redo_function(redo_remove_book)

        for rental in rentals_to_remove:
            undo_remove_rental = FunctionCall(self._rentals_service.rent_book, rental.rental_id, rental.book_id, rental.client_id, rental.rented_date)
            redo_remove_rental = FunctionCall(self._rentals_service.remove_rental, rental.rental_id)
            cascaded_op.add_undo_function(undo_remove_rental)
            cascaded_op.add_redo_function(redo_remove_rental)

        self._books_repo.remove_book(book_id)
        for rental in rentals_to_remove:
            self._rentals_service.remove_rental(rental.rental_id)

        self._undo_service.record_operation(cascaded_op)


    def update_book(self, book_id, new_title, new_author):
        book = self.find_book_by_id(book_id)
        old_title = book.title
        old_author = book.author
        if book:
            self._books_repo.update_book(book_id, new_title, new_author)
            undo = FunctionCall(self._books_repo.update_book, book_id, old_title, old_author)
            redo = FunctionCall(self._books_repo.update_book, book_id, new_title, new_author)
            operation = Operation(undo, redo)
            self._undo_service.record_operation(operation)

    def list_books(self):
        books = self._books_repo.list_books()
        sorted_books = sorted(books, key=lambda book: book.book_id)
        return sorted_books

    def find_book_by_id(self, book_id):
        for book in self._books_repo.list_books():
            if book.book_id == book_id:
                return book
        return None

    def find_books_by_title(self, title):
        return [book for book in self._books_repo.list_books() if title.lower() in book.title.lower()]

    def find_books_by_author(self, author):
        return [book for book in self._books_repo.list_books() if author.lower() in book.author.lower()]
