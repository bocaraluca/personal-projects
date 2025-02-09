import unittest
from src.services.books_service import BooksService
from src.services.clients_service import ClientsService

class TestBooksService(unittest.TestCase):
    def setUp(self):
        self._reset_file('files/test_books.txt')
        self._reset_file('files/test_books.pickle')
        self.memory_service = BooksService('in-memory')
        self.text_service = BooksService('text-file', 'files/test_books.txt')
        self.binary_service = BooksService('binary-file', 'files/test_books.pickle')

    @staticmethod
    def _reset_file(file_path):
        with open(file_path, 'w') as file:
            file.truncate(0)

    def test_add_book(self):
        self.memory_service.add_book(21, 'Ion', 'Liviu Rebreanu')
        self.text_service.add_book(21, 'Ion', 'Liviu Rebreanu')
        self.binary_service.add_book(21, 'Ion', 'Liviu Rebreanu')
        self.assertEqual(len(self.memory_service.list_books()), 21)
        new_book = self.memory_service.find_book_by_id(21)
        self.assertEqual(new_book.title, 'Ion')
        self.assertEqual(new_book.author, 'Liviu Rebreanu')
        self.assertEqual(len(self.text_service.list_books()), 21)
        new_book = self.text_service.find_book_by_id(21)
        self.assertEqual(new_book.title, 'Ion')
        self.assertEqual(new_book.author, 'Liviu Rebreanu')
        self.assertEqual(len(self.binary_service.list_books()), 21)
        new_book = self.binary_service.find_book_by_id(21)
        self.assertEqual(new_book.title, 'Ion')
        self.assertEqual(new_book.author, 'Liviu Rebreanu')

    def test_remove_book(self):
        self.memory_service.remove_book(20)
        self.text_service.remove_book(20)
        self.binary_service.remove_book(20)
        self.assertEqual(len(self.memory_service.list_books()), 19)
        self.assertEqual(len(self.text_service.list_books()), 19)
        self.assertEqual(len(self.binary_service.list_books()), 19)

    def test_update_book(self):
        self.memory_service.update_book(1, 'Ion', 'Liviu Rebreanu')
        self.text_service.update_book(1, 'Ion', 'Liviu Rebreanu')
        self.binary_service.update_book(1, 'Ion', 'Liviu Rebreanu')
        book = self.memory_service.find_book_by_id(1)
        self.assertEqual(book.title, 'Ion')
        self.assertEqual(book.author, 'Liviu Rebreanu')
        book = self.text_service.find_book_by_id(1)
        self.assertEqual(book.title, 'Ion')
        self.assertEqual(book.author, 'Liviu Rebreanu')
        book = self.binary_service.find_book_by_id(1)
        self.assertEqual(book.title, 'Ion')
        self.assertEqual(book.author, 'Liviu Rebreanu')

class TestClientsService(unittest.TestCase):
    def setUp(self):
        self._reset_file('files/test_clients.txt')
        self._reset_file('files/test_clients.pickle')
        self.memory_service = ClientsService('in-memory')
        self.text_service = ClientsService('text-file', 'files/test_clients.txt')
        self.binary_service = ClientsService('binary-file', 'files/test_clients.pickle')

    @staticmethod
    def _reset_file(file_path):
        with open(file_path, 'w') as file:
            file.truncate(0)

    def test_add_client(self):
        self.memory_service.add_client(21, 'Ana Popescu')
        self.text_service.add_client(21, 'Ana Popescu')
        self.binary_service.add_client(21, 'Ana Popescu')
        self.assertEqual(len(self.memory_service.list_clients()), 21)
        new_client = self.memory_service.find_client_by_id(21)
        self.assertEqual(new_client.name, 'Ana Popescu')
        self.assertEqual(len(self.text_service.list_clients()), 21)
        new_client = self.text_service.find_client_by_id(21)
        self.assertEqual(new_client.name, 'Ana Popescu')
        self.assertEqual(len(self.binary_service.list_clients()), 21)
        new_client = self.binary_service.find_client_by_id(21)
        self.assertEqual(new_client.name, 'Ana Popescu')

    def test_remove_client(self):
        self.memory_service.remove_client(20)
        self.text_service.remove_client(20)
        self.binary_service.remove_client(20)
        self.assertEqual(len(self.memory_service.list_clients()), 19)
        self.assertEqual(len(self.text_service.list_clients()), 19)
        self.assertEqual(len(self.binary_service.list_clients()), 19)

    def test_update_client(self):
        self.memory_service.update_client(1, 'Ana Popescu')
        self.text_service.update_client(1, 'Ana Popescu')
        self.binary_service.update_client(1, 'Ana Popescu')
        client = self.memory_service.find_client_by_id(1)
        self.assertEqual(client.name, 'Ana Popescu')
        client = self.text_service.find_client_by_id(1)
        self.assertEqual(client.name, 'Ana Popescu')
        client = self.binary_service.find_client_by_id(1)
        self.assertEqual(client.name, 'Ana Popescu')
